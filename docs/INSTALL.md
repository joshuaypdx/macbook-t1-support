# Install and test the beta

Use Ubuntu 26.04 LTS on an [eligible MacBook Pro](COMPATIBILITY.md). Back up important files, keep a recovery boot option available, and have an internet connection. Keep external GPUs disconnected during the initial test.

1. Download [the 0.6.1 beta package](../packages/mbp132-support_0.6.1_all.deb?raw=1) to Downloads. The [SHA-256 checksums](../packages/SHA256SUMS) are available alongside it.
2. In Terminal, install the utility and run its read-only preflight.

   ```bash
   sudo apt install ~/Downloads/mbp132-support_0.6.1_all.deb
   sudo mbp132-support preflight
   ```

3. If preflight reports PASS, run `sudo mbp132-support install`. Read the displayed profile before confirming. Enter `INSTALL` on MacBookPro13,2 for the full profile. Enter `INSTALL-TOUCHBAR` on MacBookPro13,3, MacBookPro14,2 or MacBookPro14,3 for the hardware-unverified Touch Bar preview. A STOPPED result is a reason to [send a report](../../issues/new/choose).
4. Reboot after the installer finishes. Run `mbp132-support testing` for Touch Bar, stock Wi-Fi and audio tests on every model. Run `mbp132-support status` for diagnostics.
5. Report the model identifier, Ubuntu version, `uname -r`, installation profile, reboot result, and the features you checked. [Open a test report](../../issues/new/choose). Redact device identifiers and share only relevant log lines.

If you already have a working full installation, upgrading the utility preserves the installed drivers. Use `status` and hardware checks after upgrading. The install command refuses to overlay a recorded installation.

## Individual trials

After upgrading the package, owners of MacBookPro13,3, 14,2 or 14,3 can select each trial independently, including on an existing 0.6.0 Touch Bar installation. Keep a working recovery boot option. Run one trial at a time, reboot, and record results before adding another.

| Command | When to use it | Undo |
| --- | --- | --- |
| `sudo mbp132-support trial-audio` | CS8409 with subsystem 106b3600 on 14,2 or 106b3900 on either 15-inch model. Requires matching Ubuntu source. Test speakers at low desktop volume, headphones and microphone individually. Stop if distorted. | `sudo mbp132-support undo-audio` |
| `sudo mbp132-support trial-wifi` | Only after stock Wi-Fi fails on 14,2 with Broadcom 14e4:43ba and Apple 106b:0157. Records a backup before changing calibration. On the two 15-inch models, test stock connectivity on both bands. | `sudo mbp132-support undo-wifi` |
| `sudo mbp132-support trial-backlight` | Optional if the SPI keyboard brightness control exists. Check after a cold boot. | `sudo mbp132-support undo-backlight` |

Each command displays its confirmation phrase. Reboot after undoing a trial. After a kernel upgrade, trial audio can be rebuilt with `sudo mbp132-support repair` once exact matching source is available. A quick camera preview before and after Touch Bar installation checks the shared iBridge. Report physical keyboard or trackpad regressions only.

## Recovery

If boot hangs after the Touch Bar install, edit the boot entry in GRUB for one boot and append `modprobe.blacklist=apple_ibridge,apple_touchbar` to the Linux kernel line. If necessary, use a recovery or live Ubuntu boot option. [Upstream recovery instructions](https://github.com/AJ-dev-i60/t1-touchbar/tree/20d65c7b0fe6d05ea9734f869b27384a62de5109#troubleshooting)

From the installed Ubuntu system, run `sudo mbp132-support remove` before removing the package itself, then reboot. For the full profile, driver and firmware removal is best effort. See [troubleshooting](TROUBLESHOOTING.md) and [kernel updates](UPDATES.md).
