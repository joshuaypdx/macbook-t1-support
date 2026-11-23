# Install and test the beta

Use Ubuntu 26.04 LTS on an [eligible MacBook Pro](COMPATIBILITY.md). Back up important files, keep a recovery boot option available, and have an internet connection. Keep external GPUs disconnected during the initial test.

1. Download [the 0.6.0 beta package](../packages/mbp132-support_0.6.0_all.deb?raw=1) to Downloads. The [SHA-256 checksums](../packages/SHA256SUMS) are available alongside it.
2. In Terminal, install the utility and run its read-only preflight.

   ```bash
   sudo apt install ~/Downloads/mbp132-support_0.6.0_all.deb
   sudo mbp132-support preflight
   ```

3. If preflight reports PASS, run `sudo mbp132-support install`. Read the displayed profile before confirming. Enter `INSTALL` on MacBookPro13,2 for the full profile. Enter `INSTALL-TOUCHBAR` on MacBookPro13,3, MacBookPro14,2 or MacBookPro14,3 for the hardware-unverified Touch Bar preview. A STOPPED result is a reason to [send a report](../../issues/new/choose).
4. Reboot after the installer finishes. Check Touch Bar Esc, Fn/function keys, brightness and media keys, FaceTime camera, keyboard and trackpad. On MacBookPro13,2, also check speakers, microphone and Wi-Fi. Run `mbp132-support status` for diagnostics.
5. Report the model identifier, Ubuntu version, `uname -r`, installation profile, reboot result, and the features you checked. [Open a test report](../../issues/new/choose). Redact device identifiers and share only relevant log lines.

If you already have a working full installation, upgrading the utility preserves the installed drivers. Use `status` and hardware checks after upgrading. The install command refuses to overlay a recorded installation.

## Recovery

If boot hangs after the Touch Bar install, edit the boot entry in GRUB for one boot and append `modprobe.blacklist=apple_ibridge,apple_touchbar` to the Linux kernel line. If necessary, use a recovery or live Ubuntu boot option. [Upstream recovery instructions](https://github.com/AJ-dev-i60/t1-touchbar/tree/20d65c7b0fe6d05ea9734f869b27384a62de5109#troubleshooting)

From the installed Ubuntu system, run `sudo mbp132-support remove` before removing the package itself, then reboot. For the full profile, driver and firmware removal is best effort. See [troubleshooting](TROUBLESHOOTING.md) and [kernel updates](UPDATES.md).
