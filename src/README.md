# MBP13,2 Ubuntu support package (beta v0.5)

One installer for Ubuntu 26.04 LTS on the Apple 2016 `MacBookPro13,2` (T1). **Not an official Ubuntu or Apple package.**

## Status

A real `MacBookPro13,2` tested version 0.4 on Ubuntu **26.04.1**, kernel **7.0.0-30-generic**, and confirmed speakers, microphone, Wi-Fi, Touch Bar and function keys work. Version 0.5 **adds update safeguards** but has not itself been tested on that computer.

## What this update does

On upgrade from 0.4, it **does not reinstall your drivers**. It protects the known-good `7.0.0-30-generic` kernel from automatic removal with APT's `NeverAutoRemove`, checks DKMS install status after APT transactions and at boot, and reports mismatches. It also fixes the earlier cleanup error and pins all three upstream source revisions to immutable commits.

Ubuntu's DKMS infrastructure normally rebuilds compatible modules for new kernels. **A successful DKMS build is not proof of runtime compatibility.** Audio still uses an unmerged kernel 7 compatibility patch. No automatic boot rollback is attempted. The older kernel should remain available in GRUB if your GRUB setup shows multiple kernels.

## Install

Upgrade from 0.4:

```bash
sudo apt install ./mbp132-support_0.5.0_all.deb
```

That is it. **Do not run `mbp132-support install` a second time** on the working system. Optional diagnostics:

```bash
mbp132-support status
```

For a fresh install on the exact model with Ubuntu 26.04's standard `7.0.0-generic` family, the command is:

```bash
sudo mbp132-support install
```

The **only hardware-validated kernel** is `7.0.0-30-generic`. Other kernel revisions in this family are experimental. The installer refuses different kernel families; a future update requires patch review, not blind retries.

If a kernel update leaves modules missing (not a crash), `sudo mbp132-support repair` can rebuild the two DKMS modules after ensuring that Ubuntu's matching source is available. It **never** resets your USB or T1 hardware while running.

## Limitations

- No guaranteed future kernel ABI compatibility; no safety guarantee for untested kernel revisions.
- No automatic GRUB default switching or reboot rollback.
- No eGPU, Touch ID, custom Touch Bar graphics, suspend, or external-disk power-management changes.
- Wi-Fi NVRAM is a community calibration file, not an original per-device backup; its licensing/regulatory provenance needs scrutiny before a public binary release.
- Full end-to-end hardware test only on one machine for v0.4, not yet a broadly validated public installer.

## Attribution and sources

- `duzelli/snd_hda_macbookpro` pinned `3414707841e7a518707be4748cd8787794e19045` (upstream `davidjo`, PR #216)
- `AJ-dev-i60/t1-touchbar` pinned `20d65c7b0fe6d05ea9734f869b27384a62de5109`
- `DeyAgrO/macbook-pro-13-2-linux` pinned `c005707321186f6ac6ac81fbe577226189568f69`

The binary package contains integration logic, **not** bundled vendor firmware/compiled third-party binaries. Third-party downloads are verified by exact git commit after retrieval, then installed only after the user's explicit consent.

## Test/build

Run `python3 tests/test_package.py` from this directory. The `.deb` is packaged with `dpkg-deb --build --root-owner-group` from a staging directory. This tests structural safeguards, *not* a kernel compilation or physical hardware.
