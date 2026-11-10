# Updates and future kernels

Ubuntu's ordinary security and application updates are important. **Don't permanently block kernel security updates** merely to keep this experimental driver working. At the same time, newly released kernels need testing before the Mac-specific driver modules can be trusted.

## Current v0.5.0 behavior

- DKMS is configured to rebuild the Apple iBridge/Touch Bar and Cirrus CS8409 modules when compatible kernels are installed and the required Ubuntu build sources are available.
- `mbp132-support status` and an update-health service attempt to identify missing modules.
- The fallback mechanism refers to `7.0.0-30-generic`. On machines installed directly with `7.0.0-43-generic`, that older version may not exist and therefore **no known-good kernel gets protected automatically**.
- A successful DKMS compile does **not** guarantee the rebuilt drivers work after reboot.
- Users must install new versions of `mbp132-support` manually. **GitHub releases are not an APT repository and do not silently update users.**

## Practical advice for this beta

Keep a backup, preserve a known-working kernel and avoid `apt autoremove` until you've confirmed an alternative boot path. If a later kernel causes sound/Touch Bar problems, select a previously working kernel from Ubuntu's advanced boot choices if available and report the regression. Do not run `sudo mbp132-support repair` on a kernel that actively crashes or fails to boot.

## For advanced users: keep a working kernel installed

If you have *physically tested* the current kernel, you can mark only its **already installed packages** as manually installed (this reduces the chance that APT automatically removes them):

```bash
for pkg in "linux-image-$(uname -r)" "linux-modules-$(uname -r)" "linux-modules-extra-$(uname -r)"; do
  dpkg-query -W -f='${Status}' "$pkg" 2>/dev/null | grep -q 'install ok installed' && sudo apt-mark manual "$pkg"
done
```

This is optional and intended for advanced testers. It does not fix kernel ABI incompatibilities or guarantee that a boot entry will remain accessible. It also does not replace regular system updates.

## Planned improvement

A later release should have the user explicitly confirm which kernel actually works, preserve that version, and offer a plain-English post-update report. Installation should remain opt-in and reversible wherever technically possible.
