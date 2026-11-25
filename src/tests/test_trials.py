"""Exercise public 0.6.1 commands with isolated hardware, firmware and DKMS fixtures."""
from pathlib import Path
import re
import os
import subprocess
import tempfile

main = (Path(__file__).resolve().parents[1] / 'usr/bin/mbp132-support').read_text()
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    main = re.sub(r'(?<![A-Za-z0-9])/(?:sys|etc|lib|proc|usr/src|var|boot)/', lambda match: str(root) + match[0], main)
    for directory in ['etc/udev/rules.d', 'sys/class/leds/spi::kbd_backlight',
                      'usr/src', 'proc/asound/card0', 'var/tmp', 'lib/firmware/brcm']:
        (root / directory).mkdir(parents=True)
    net = root / 'sys/class/net/wlan1'
    (net / 'wireless').mkdir(parents=True)
    dev = net / 'device'
    dev.mkdir()
    for key, value in [('vendor', '0x14e4'), ('device', '0x43ba'),
                       ('subsystem_vendor', '0x106b'), ('subsystem_device', '0x0157')]:
        (dev / key).write_text(value)
    codec = root / 'proc/asound/card0/codec#0'
    fw = root / 'lib/firmware/brcm/brcmfmac43602-pcie.txt'
    state = root / 'var/lib/mbp132-support'
    mocks = r"""
model(){ echo "$MODEL_ID"; }
validate(){ require_profile; }
root(){ :; }
lock_install(){ :; }
modinfo(){ echo "ROOT/lib/modules/fixture/kernel/audio.ko"; }
dkms(){ echo "$*" >> "ROOT/dkms-calls"; }
get_repo(){
  mkdir -p "$3/firmware"
  echo 'macaddr=00:00:00:00:00:00' > "$3/firmware/brcmfmac43602-pcie.txt"
  echo 'AUTOINSTALL="yes"' > "$3/dkms.conf"
}
install_prereqs(){ echo exact-source >> "ROOT/dkms-calls"; }
choosemac(){ [ "$WIFI_IFACE" = wlan1 ] && echo 02:01:02:03:04:05; }
dracut(){ :; }
udevadm(){ :; }
""".replace('ROOT', str(root))
    main = main.replace('case "${1:-help}" in', mocks + '\ncase "${1:-help}" in')
    script = root / 'test-installer'
    script.write_text(main)

    def run(model, command, ok=True, confirm=True):
        result = subprocess.run(['bash', str(script), command], text=True, capture_output=True,
                                env=dict(os.environ, MODEL_ID='MacBookPro' + model),
                                input=(command.upper() if confirm else '') + '\n')
        assert (result.returncode == 0) == ok, (command, result.stdout, result.stderr)

    for model, subsystem in [('14,2', '3600'), ('13,3', '3900'), ('14,3', '3900')]:
        codec.write_text('Vendor Id: 0x10138409\nSubsystem Id: 0x106b0000\n')
        run(model, 'trial-audio', False)
        codec.write_text('Vendor Id: 0x10138409\nSubsystem Id: 0x106b' + subsystem + '\n')
        run(model, 'trial-audio', False, confirm=False)
        run(model, 'trial-audio')
        assert 'AUTOINSTALL="no"' in (state / 'trial-audio/source/dkms.conf').read_text()
        run(model, 'trial-audio', False)
        run('14,3' if model == '14,2' else '14,2', 'undo-audio', False)
        run(model, 'undo-audio')
    assert 'exact-source' in (root / 'dkms-calls').read_text()
    for model in ['13,3', '14,3', '13,2']:
        run(model, 'trial-wifi', False)
    board = dev / 'subsystem_device'
    board.write_text('0x0173')
    run('14,2', 'trial-wifi', False)
    board.write_text('0x0157')
    for original in [None, 'saved original calibration']:
        if original:
            fw.write_text(original)
        run('14,2', 'trial-wifi')
        assert fw.read_text().strip() == 'macaddr=02:01:02:03:04:05'
        run('14,2', 'undo-wifi')
        assert (fw.read_text() if fw.exists() else None) == original
    run('14,2', 'trial-wifi')
    installed = fw.read_bytes()
    fw.write_text('user change')
    run('14,2', 'undo-wifi', False)
    assert fw.read_text() == 'user change'
    fw.write_bytes(installed)
    run('14,2', 'undo-wifi')
    assert fw.read_text() == 'saved original calibration'
    run('13,3', 'trial-backlight')
    run('13,3', 'undo-backlight')
    print('PASS: model and component IDs, consent, audio source policy, add-on upgrades and standalone rollback')
