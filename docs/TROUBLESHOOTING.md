# Troubleshooting without becoming a Linux expert

Most problems can be reported in ordinary language. Tell us **which step you reached**, **what you saw**, and **what stopped working**. A photo of the screen can help.

## If the installer says STOPPED

This is intentional. It may have found an unsupported model, kernel, Secure Boot state or an existing driver install. **Do not remove the safety checks or rerun the installer repeatedly.** Copy the message and open a [help request](../.github/ISSUE_TEMPLATE/help.yml).

## If Ubuntu doesn't start after driver installation

If your Mac has a working backup boot option, use that to return to a previously working kernel. Do not attach or detach an eGPU while the system is frozen. Seek assistance rather than changing GRUB settings at random. The installer does not provide automatic rollback.

## If you have no sound

First check **Settings → Sound** and ensure the internal speakers are selected. Check volume and whether sound works through headphones or Bluetooth. The `status` command alone does not prove the speakers work.

If you are comfortable using Terminal, these are **read-only**:

```bash
uname -r
sudo dkms status
modinfo -n snd_hda_codec_cs8409
cat /proc/asound/cards
```

If `dkms status` reports installed and `modinfo -n` points into `/updates/dkms/`, a report claiming the module is broken may simply be a v0.5.0 status bug. See [Known issues](KNOWN_ISSUES.md).

## If your Touch Bar doesn't work

Shut down normally and restart once. Do not reset the T1 USB bridge or run experimental modprobe commands based on unrelated Mac models. Tell us whether the keyboard, Escape key, Touch Bar, and camera work separately.

## If Wi-Fi can't connect

If possible use Ethernet temporarily. Tell us whether Wi-Fi networks are visible, whether a connection fails, or whether the Wi-Fi device is missing. Don't share your router password or MAC address. Avoid installing another model's Wi-Fi NVRAM.

## Reporting a problem safely

The [GitHub issue form](../.github/ISSUE_TEMPLATE/bug-report.yml) asks for the model, Ubuntu version, kernel and a description of the problem. This usually suffices.

You may be asked for logs. **Before posting**, remove serial numbers, MAC addresses, public IP addresses, disk UUIDs, usernames, file paths containing personal names, Wi-Fi network names, passwords, tokens and other private information. If you're unsure, ask first rather than publishing an unredacted log.

Remember: the original package has a known status-reporting bug. Describe physical behavior as well as any warning shown.
