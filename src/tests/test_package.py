#!/usr/bin/env python3
"""Offline structural tests. No system modification, no external downloads."""
from pathlib import Path
import re
import subprocess
import tempfile
import shutil

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
    env = dict(__import__('os').environ, PATH=str(temp / 'bin') + ':' + __import__('os').environ.get('PATH',''))
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

print('PASS: syntax, immutable source pins, cleanup, freeze guard, APT fallback, and simulated DKMS update scenarios')
