# MacBook T1 Support

**Making Ubuntu feel at home on a 2016 MacBook Pro.** 🍎🐧

![Beta](https://img.shields.io/badge/status-public%20beta-orange) ![Ubuntu](https://img.shields.io/badge/Ubuntu-26.04%20LTS-E95420) ![Tested Mac](https://img.shields.io/badge/tested-MacBookPro13%2C2-2472A3)

**MacBook T1 Support** is a community-made installer for hardware that doesn't work fully with an ordinary Ubuntu installation on certain older MacBooks. It brings together established community work for the **Touch Bar, internal sound, and Broadcom Wi-Fi** in one guided setup.

> [!IMPORTANT]
> **Beta, and currently only for one Mac model.** The installer checks for **MacBookPro13,2**, the **13-inch Late 2016 MacBook Pro with Touch Bar (T1)**. It refuses other models. The name describes our long-term goal, **not** broad T1 compatibility today. This is not an Apple or Ubuntu product.

## 👋 Start here (no Linux expertise required)

**What you need:** Ubuntu **26.04 LTS**, a **MacBookPro13,2**, an internet connection, and a backup of important files. We tested the installer on a fresh, updated Ubuntu 26.04.1 installation running kernel `7.0.0-43-generic` on one real MacBookPro13,2.

### 1. Download the installer

**[⬇️ Download MacBook T1 Support 0.5.0 Beta (.deb)](packages/mbp132-support_0.5.0_all.deb?raw=1)**

If GitHub shows a file page instead of downloading, click **Download raw file**. Save the file in **Downloads**. You don't need the source-code ZIPs that GitHub displays automatically.

### 2. Open Terminal and install the app

Copy this line, paste it into Ubuntu's **Terminal**, and press Return:

```bash
sudo apt install ~/Downloads/mbp132-support_0.5.0_all.deb
```

Ubuntu will ask for your computer password. **The password will not appear as you type.** That's normal. This first step installs the support utility; it **does not install the hardware drivers yet**.

### 3. Check that your Mac is supported

```bash
sudo mbp132-support preflight
```

If it says **PASS**, continue. If it says **STOPPED**, don't force it. [Ask for help](../../issues/new/choose) and include the exact error message. This preflight doesn't make changes.

### 4. Install your Mac's hardware support

```bash
sudo mbp132-support install
```

Read the warning, then type **`INSTALL`** when asked. The installer downloads specific, pinned revisions of three community projects, obtains matching Ubuntu kernel source, and builds the required drivers. **An internet connection is needed.** It may take a while. Do not power down during installation.

When the installer says the steps have completed, **reboot**. Keep external GPUs disconnected during this initial test.

### 5. Test the hardware

Try your MacBook's **built-in speakers**, **microphone**, **Touch Bar/function keys**, **trackpad**, and **Wi-Fi**. Some functions, including the webcam, are not yet comprehensively verified on fresh installations. Then run:

```bash
mbp132-support status
```

A known beta issue can make this status display look alarming even while the hardware works. See [Known issues](docs/KNOWN_ISSUES.md) before attempting a repair. **Do not reinstall repeatedly to clear a warning.**

**That's it.** You should now have a more capable Ubuntu MacBook, without configuring EFI or GRUB yourself.

[Detailed installation help](docs/INSTALL.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Supported computers](docs/COMPATIBILITY.md)

---

## What works, and what doesn't (yet)

| Feature | Beta status |
| --- | --- |
| Touch Bar and function keys | ✅ Working on the test Mac |
| Internal speakers (Cirrus CS8409) | ✅ Working on the test Mac |
| Built-in keyboard / trackpad | ✅ Working on the test Mac |
| Broadcom Wi-Fi | 🟡 Driver detected and scans networks; connection and regulatory behavior should be checked per device |
| T1 iBridge | ✅ Detected |
| Camera / microphone | 🟡 Requires broader testing |
| Touch ID | ❌ Not supported |
| Apple-style customizable Touch Bar graphics | ❌ Not supported |
| Suspend/resume with external boot drive | ⚠️ Untested; avoid for now |
| External graphics (eGPU) | 🧪 [Separate experimental project](docs/EGPU.md) |

**One machine is not a compatibility guarantee.** We have positive real-hardware testing on `7.0.0-30-generic` (earlier package) and `7.0.0-43-generic` (v0.5.0 on the fresh Samsung SSD). The public beta needs more testers and proper regression testing on future kernel updates.

## 🛟 Need help or want to contribute?

**You do not need to understand Linux commands to give useful feedback.**

- **[Something isn't working](../../issues/new/choose)**: Guided bug-report form. Include what you expected and what happened.
- **[Request support for another Mac](../../issues/new/choose)**: Tell us the model and Ubuntu version.
- **[Ask a question](../../issues/new/choose)**: Beginners welcome.
- **Follow new releases:** Use GitHub's **Watch** option to receive release notifications. Updates are **not yet installed automatically**.

**Please don't publish your Mac's serial number, password, Wi-Fi MAC address, personal files, or unredacted full logs.** See [safe reporting tips](docs/TROUBLESHOOTING.md#reporting-a-problem-safely).

## Before you update your kernel

This beta uses kernel modules that may need rebuilding when Ubuntu installs a new kernel. **A successful build doesn't guarantee that audio or the Touch Bar will work on a newer kernel.** Version 0.5.0 still refers to `7.0.0-30-generic` as its automatic fallback kernel. The newer `7.0.0-43-generic` hardware test is not automatically reflected in that fallback logic. Read [updates and kernel precautions](docs/UPDATES.md) before running kernel cleanup or relying on a new kernel. Do not run `apt autoremove` until you have a working fallback.

## For developers and advanced users

The [original integration source](src/) and [offline package tests](src/tests/test_package.py) are included. The `.deb` in [packages/](packages/) is byte-for-byte the v0.5.0 beta package that was tested on hardware. The integration does **not** bundle the third-party kernel driver source or NVRAM; those are fetched at pinned Git revisions after explicit approval.

[Attributions and licenses](NOTICE.md) · [Contribute](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md) · [Maintainer release guide](docs/MAINTAINERS.md)

---

*Created by Mac enthusiasts, for Mac enthusiasts. Built to be understandable, not intimidating.*
