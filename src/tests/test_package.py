#!/usr/bin/env python3
"""Offline structural tests. No system modification, no external downloads."""
from pathlib import Path
import subprocess
import tempfile
import os

ROOT = Path(__file__).resolve().parents[1]
MAIN = (ROOT / 'usr/bin/mbp132-support').read_text()
GUARD = (ROOT / 'usr/lib/mbp132-support/update-guard').read_text()
FALLBACK = (ROOT / 'usr/lib/mbp132-support/fallback').read_text()

def assert_ok(cond, message):
    if not cond:
        raise AssertionError(message)

for filename in [
    'usr/bin/mbp132-support',
    'usr/lib/mbp132-support/fallback',
    'usr/lib/mbp132-support/update-guard',
    'debian/postinst', 'debian/prerm', 'debian/postrm'
]:
    subprocess.run(['bash','-n',str(ROOT / filename)],check=True)

for sha in [
    '3414707841e7a518707be4748cd8787794e19045',
    '20d65c7b0fe6d05ea9734f869b27384a62de5109',
    'c005707321186f6ac6ac81fbe577226189568f69',
]:
    assert_ok(sha in MAIN, f'Missing source pin {sha}')
assert_ok('TOUCH_REF=main' not in MAIN, 'Touch Bar still references moving main')
assert_ok("trap 'rm -rf \"$work\"' EXIT" not in MAIN, 'Original unbound work cleanup bug remains')
assert_ok('"${MBP132_WORKDIR:-}"' in MAIN, 'Cleanup guard missing')
assert_ok('skip_acpi_power=1' in MAIN, 'T1 ACPI freeze protection missing')
assert_ok('sudo mbp132-support repair' in MAIN, 'Repair interface missing')
assert_ok('APT::NeverAutoRemove' in FALLBACK, 'Fallback protection missing')
assert_ok('apt-mark hold' not in FALLBACK, 'Kernel security updates must not be held')
assert_ok('systemctl enable' in (ROOT / 'debian/postinst').read_text(), 'Boot monitor not installed')
assert_ok('DPkg::Post-Invoke' in (ROOT / 'etc/apt/apt.conf.d/99mbp132-update-monitor').read_text(), 'APT check missing')

# Run health monitor against a simulated /boot and /var/lib, plus mock executables.
with tempfile.TemporaryDirectory() as td:
    temp = Path(td)
    (temp / 'boot').mkdir()
    (temp / 'state').mkdir()
    (temp / 'bin').mkdir()
    (temp / 'state/attempted').write_text('')
    (temp / 'state/known-good-kernel').write_text('7.0.0-30-generic\n')
    (temp / 'boot/vmlinuz-7.0.0-30-generic').touch()
    for cmd, content in {
        'uname': '#!/bin/sh\necho 7.0.0-30-generic\n',
        'dkms': '#!/bin/sh\ncase "$*" in *7.0.0-30-generic*) echo "module/0.1, 7.0.0-30-generic, x86_64: installed";; esac\n',
        'dpkg-query': '#!/bin/sh\necho 7.0.0-30.30\n',
    }.items():
        target = temp / 'bin' / cmd
        target.write_text(content)
        target.chmod(0o755)
    script = GUARD.replace('STATE=/var/lib/mbp132-support', f'STATE={temp}/state')
    script = script.replace('for path in /boot/vmlinuz-', f'for path in {temp}/boot/vmlinuz-')
    script = script.replace('k=${path#/boot/vmlinuz-}', f'k=${{path#{temp}/boot/vmlinuz-}}')
    script = script.replace('cat /sys/class/dmi/id/product_name 2>/dev/null || true', "printf 'MacBookPro13,2\\n'")
    program = temp / 'guard.sh'
    program.write_text(script)
    program.chmod(0o755)
    env = dict(os.environ, PATH=str(temp / 'bin') + ':' + os.environ.get('PATH',''))
    def guard():
        p = subprocess.run(['bash',str(program),'--report'],text=True,capture_output=True,env=env)
        assert_ok(p.returncode == 0, f'guard returned {p.returncode}: {p.stderr}')
        return p.stdout
    out=guard()
    assert_ok('KNOWN WORKING' in out, 'Known good kernel absent from report')
    assert_ok('DKMS presence checks: PASS' in out, 'Good modules treated as broken')
    (temp / 'boot/vmlinuz-7.0.0-31-generic').touch()
    out=guard()
    assert_ok('UNTESTED' in out and 'MISSING or build failed' in out, 'Failed to flag newer kernel without DKMS')
    (temp / 'boot/vmlinuz-7.3.0-1-generic').touch()
    out=guard()
    assert_ok('OUTSIDE our supported' in out, 'New kernel family should be flagged')
    (temp / 'state/attempted').unlink()
    assert_ok('not yet installed' in guard(), 'Uninitialized state should not be reported as installed')
    (temp / 'state/attempted').touch()
    (temp / 'state/install-model').write_text('MacBookPro14,3\n')
    program.write_text(script.replace("printf 'MacBookPro13,2\\n'", "printf 'MacBookPro14,3\\n'"))
    out = guard()
    assert 'Touch Bar beta on MacBookPro14,3' in out and 'apple-ib-drv' in out
    assert 'snd_hda_macbookpro' not in out and 'Protected fallback' not in out

print('PASS: syntax, immutable source pins, cleanup, freeze guard, APT fallback, and simulated DKMS update scenarios')

# Exercise real shell routing and validation with fixtures. Replace sysfs and
# command responses only in this test copy, never in the installed command.
with tempfile.TemporaryDirectory() as td:
    temp = Path(td)
    for directory in ['efi', 'modules/7.0.0-43-generic', 'net', 'state', 'logs']:
        (temp / directory).mkdir(parents=True)
    fixture = MAIN[:MAIN.rindex('case "${1:-help}" in')]
    for original, replacement in {
        '/sys/firmware/efi': f'{temp}/efi',
        '/sys/class/net/wlp2s0': f'{temp}/net/wlp2s0',
        '/lib/modules/': f'{temp}/modules/',
        '/var/lib/mbp132-support': f'{temp}/state',
        '/var/log/mbp132-support': f'{temp}/logs',
        '/var/tmp/mbp132-support.XXXXXX': f'{temp}/work.XXXXXX',
        '/sys/module/': f'{temp}/module/',
        '/usr/src/': f'{temp}/usr/src/',
        '/etc/modprobe.d/': f'{temp}/etc/modprobe.d/',
        '/etc/modules-load.d/': f'{temp}/etc/modules-load.d/',
        '/etc/udev/rules.d/': f'{temp}/etc/udev/rules.d/',
        '/usr/lib/mbp132-support/fallback protect': 'record fallback',
        '/usr/lib/mbp132-support/update-guard --apt': 'record update-guard',
    }.items():
        fixture = fixture.replace(original, replacement)
    program = temp / 'installer.sh'
    program.write_text('uname(){ echo 7.0.0-43-generic; }\n' + fixture + r'''
model(){ printf '%s\n' "$TEST_MODEL"; }
os(){ echo "${TEST_OS:-ubuntu:26.04}"; }
kernel(){ echo "$KERNEL"; }
dpkg(){ echo "${TEST_ARCH:-amd64}"; }
lsusb(){ [ "${TEST_BRIDGE:-active}" = active ] && echo '05ac:8600'; }
lspci(){ [ "${TEST_WIFI:-present}" = present ] && echo '14e4:43ba'; }
secureboot(){ echo "${TEST_SB:-disabled}"; }
root(){ :; }
lock_install(){ :; }
dkms(){ echo "${TEST_DKMS:-}"; }
print_source(){ record source-check; }
readmac(){ return 0; }
record(){ printf 'action: %s\n' "$*"; }
get_repo(){
  record "fetch ${3##*/}"
  mkdir -p "$3/apple-ib-drv" "$3/firmware"
  echo skip_acpi_power > "$3/apple-ib-drv/apple-ibridge.c"
  echo fixture > "$3/install.cirrus.driver.sh"
  echo fixture > "$3/firmware/brcmfmac43602-pcie.txt"
}
install_prereqs(){ record full-prereqs; }
install_headers(){ record headers; }
choosemac(){ echo 02:00:00:00:00:01; }
install_t1(){ record touchbar; }
install_wifi(){ record wifi; }
install_audio(){ record audio; }
install_keyboard_backlight(){ record keyboard; }
"$1"
''')
    def run(model, action='preflight', consent='', **settings):
        env = dict(os.environ, TEST_MODEL=model, **settings)
        return subprocess.run(['bash', str(program), action], input=consent,
                              text=True, capture_output=True, env=env)

    (temp / 'net/wlp2s0').touch()
    assert run('MacBookPro13,2').returncode == 0
    assert run('MacBookPro13,2', TEST_WIFI='missing').returncode != 0
    (temp / 'net/wlp2s0').unlink()
    for model in ['MacBookPro13,3', 'MacBookPro14,2', 'MacBookPro14,3']:
        result = run(model, TEST_WIFI='missing')
        assert result.returncode == 0 and 'touchbar-beta' in result.stdout, result
        assert 'hardware-unverified' in result.stderr
    for model in ['MacBookPro13,1', 'MacBookPro14,1', 'MacBookPro15,1', 'MacBookPro14,3x', '']:
        result = run(model, 'install_all', 'INSTALL-TOUCHBAR\n')
        assert result.returncode != 0 and 'allowlist' in result.stderr and 'action:' not in result.stdout
    for setting, value, message in [
        ('TEST_BRIDGE', 'recovery', 'iBridge'),
        ('TEST_OS', 'ubuntu:24.04', 'Ubuntu 26.04'),
        ('TEST_ARCH', 'arm64', 'amd64'),
        ('TEST_SB', 'enabled', 'Secure Boot enabled'),
        ('TEST_SB', 'unknown', 'Secure Boot status'),
    ]:
        result = run('MacBookPro14,3', **{setting: value})
        assert result.returncode != 0 and message in result.stderr, result
    (temp / 'efi').rmdir()
    assert 'EFI boot' in run('MacBookPro14,2').stderr
    (temp / 'efi').mkdir()
    result = run('MacBookPro13,3', 'install_all', 'INSTALL-TOUCHBAR\n',
                 TEST_DKMS='apple-ib-drv/0.1: added')
    assert result.returncode != 0 and 'overlay' in result.stderr
    result = run('MacBookPro13,3', 'install_all', 'INSTALL\n')
    assert result.returncode != 0 and 'Cancelled' in result.stderr and 'action:' not in result.stdout
    result = run('MacBookPro14,2', 'install_all', 'INSTALL-TOUCHBAR\n')
    assert result.returncode == 0, result
    actions = {line for line in result.stdout.splitlines() if line.startswith('action:')}
    assert actions == {'action: fetch touch', 'action: headers', 'action: touchbar', 'action: update-guard'}, actions
    assert (temp / 'state/install-model').read_text() == 'MacBookPro14,2\n'
    result = run('MacBookPro14,3', 'remove_all')
    assert result.returncode != 0 and 'different model' in result.stderr
    (temp / 'state/attempted').unlink()
    (temp / 'net/wlp2s0').touch()
    result = run('MacBookPro13,2', 'install_all', 'INSTALL\n')
    assert result.returncode == 0, result
    actions = {line for line in result.stdout.splitlines() if line.startswith('action:')}
    assert actions == {f'action: {action}' for action in [
        'fetch touch', 'fetch audio', 'fetch wifi', 'full-prereqs', 'touchbar',
        'keyboard', 'wifi', 'audio', 'fallback', 'update-guard',
    ]}, actions

print('PASS: model routing, blocked hardware and platforms, consent, no preview audio/Wi-Fi, full profile and model-bound removal')
