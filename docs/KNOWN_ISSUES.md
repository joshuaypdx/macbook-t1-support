# Known beta issues (read before reporting a problem)

## 1. The status message can be wrong

On the fresh, updated Ubuntu 26.04.1 Samsung SSD test, `mbp132-support status` printed **`Installed-state: not-run`** and **`snd_hda_macbookpro/0.1: broken`**, despite working speakers and a loaded codec driver. A separate `sudo dkms status` reported:

```text
snd_hda_macbookpro/0.1, 7.0.0-43-generic, x86_64: installed (Original modules exist)
```

The reported `broken` label may be a reporting/parsing error; it is **not proof of a broken audio driver**. The contradictory installed-state record also needs investigation. Don't rerun the full installer just to make the label disappear. Please provide the outputs of `uname -r`, `dkms status`, and `modinfo -n snd_hda_codec_cs8409`, along with whether speakers actually work.

## 2. Kernel fallback version is outdated

Version 0.5.0's safeguard looks specifically for `7.0.0-30-generic`, the earlier proven version. If that kernel is absent, the installer warns that it cannot protect a known-good kernel. The newly verified `7.0.0-43-generic` is **not automatically protected by v0.5.0**. A later version should ask the user to confirm a working kernel and protect that installed version.

**For now:** do not run `apt autoremove` until you have verified and preserved a fallback. Avoid forcing an update to an untested kernel. See [updates](UPDATES.md).

## 3. Wi-Fi board calibration may differ

The installer uses one pinned, community-sourced Broadcom NVRAM file. It does not extract an original per-machine calibration file. Its licensing and regulatory provenance need review before recommending it broadly, and a connected Wi-Fi test was not completed on the fresh SSD installation.

## 4. Suspend and power management

Suspend/resume from externally attached storage has not been qualified. Unexpected storage disconnects can cause data loss. Avoid suspend with an external boot drive until tested.

## 5. Removal is best effort

`sudo mbp132-support remove` may not fully undo every upstream audio installer or system configuration change. Avoid treating it as a guaranteed rollback. Back up important data before setup and seek support if removal fails.

## 6. Installation is currently Terminal-assisted

The `.deb` installs a command-line helper. It does **not** automatically execute the privileged hardware-driver setup. We want a guided GUI/double-click workflow later, after broader safety testing.
