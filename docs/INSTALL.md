# Installation: one step at a time

This is written for Mac owners who are new to Linux. You need a **MacBookPro13,2**, Ubuntu **26.04 LTS**, an internet connection and a backup.

> [!WARNING]
> This is a beta that modifies kernel drivers and the Wi-Fi calibration file. It has been tested on one physical MacBookPro13,2, not every machine. Don't install it on a different Mac, a different Linux distribution or a production system you cannot afford to troubleshoot. Avoid suspend with an external boot disk for now.

## Before you begin

1. Open **Settings → About** in Ubuntu to confirm you installed Ubuntu 26.04.
2. Confirm the Mac is the **13-inch Late 2016 Touch Bar** model. If uncertain, open Terminal and run `cat /sys/class/dmi/id/product_name`. The supported answer is **`MacBookPro13,2`**.
3. Make sure you can connect to the internet, perhaps using Ethernet during setup.
4. Keep eGPU hardware disconnected while establishing basic support.

## Install

1. From the repository's home page, download the [v0.5.0 .deb](../packages/mbp132-support_0.5.0_all.deb?raw=1) into **Downloads**. If GitHub displays the file rather than downloading, use **Download raw file**.
2. Open **Terminal**. You can find it via the app launcher. Copy/paste one command at a time:

   ```bash
   sudo apt install ~/Downloads/mbp132-support_0.5.0_all.deb
   ```

   Enter your Ubuntu login password. No dots or stars appear while you type.
3. Run a read-only compatibility check:

   ```bash
   sudo mbp132-support preflight
   ```

   If it says **STOPPED**, copy the error into a new [support request](../.github/ISSUE_TEMPLATE/help.yml), then stop. Don't force an unsupported setup.
4. Install the driver integration:

   ```bash
   sudo mbp132-support install
   ```

   Read the warning and type **`INSTALL`** exactly when prompted. The installer fetches pinned sources and builds drivers for the *currently running* kernel.
5. Once you see **Installation steps completed**, restart the MacBook using Ubuntu's **Power → Restart** menu. Keep the external storage attached; do not attempt suspend/resume yet.
6. Test the speakers with a music track, try the volume keys and Touch Bar, type on the keyboard, move the trackpad, and verify visible Wi-Fi networks. Try connecting to your own Wi-Fi. Microphone and webcam testing is welcome, but their operation is not guaranteed by this beta.

## Status after installation

```bash
mbp132-support status
```

Some builds of v0.5.0 show `Installed-state: not-run` or report the audio DKMS package as `broken` even when the **actual** driver is loaded and `dkms status` reports it installed. Don't repeat the install just to clear this label. Check the hardware and see [Known issues](KNOWN_ISSUES.md).

## Next time

You do **not** need to run `mbp132-support install` again after every reboot. For updates, read [Updating safely](UPDATES.md). If your audio or Touch Bar stops after a kernel update, first boot a previously working kernel if available, then ask for help. Never force the installer onto an untested kernel.
