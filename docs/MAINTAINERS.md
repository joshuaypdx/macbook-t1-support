# Maintainers: GUI-first release process

This guide is for the project owner. **No command-line Git knowledge is needed** to publish or update the repository on GitHub. Start with [LAUNCH_GUIDE.md](LAUNCH_GUIDE.md).

## What is currently inside

- `packages/mbp132-support_0.5.0_all.deb`: the **exact** 12,120-byte beta package tested on the MacBook.
- `src/`: the **matching v0.5.0 integration source**, including its existing offline tests. Upstream driver repositories are **not** vendored here.
- `tests/verify-release.py`: compares the package payload with the committed source tree before a release.
- `.github/ISSUE_TEMPLATE/`: plain-English feedback and bug-report forms shown automatically in **Issues → New issue**.
- `.github/workflows/ci.yml`: checks code syntax, package/source consistency and source tests on every commit and pull request.
- `.github/workflows/release.yml`: optional manual **Actions → Publish beta release → Run workflow** publishing the vetted `.deb` as a GitHub pre-release. It does not modify anyone's computer.

## Ship a corrected version later

1. Prepare and physically test the new installer on an actual MacBook. Save its source and `.deb`.
2. Replace the `packages/` `.deb` and update `src/` in your *local GitHub Desktop repository*. Ask a maintainer/developer to update `README.md` download filename, compatibility notes, changelog, release notes, and test assertions. Do not rename a package without updating references.
3. Open **GitHub Desktop**. Review changed files, type a commit message and click **Commit to main**, then **Push origin**.
4. On GitHub, open **Actions** and verify the **Check installer package** workflow is green. If it fails, don't publish a release.
5. Optional: use **Actions → Publish beta release → Run workflow**, enter a *new* tag like `v0.5.1-beta.1`. It validates package/source consistency and requires the release tag's base version to match the package version.
6. Keep release notes understandable. Avoid technical changes without hardware validation. Reply to issues with reproducible findings, and label model-specific problems.

GitHub does not have a magic switch that safely rebuilds a Linux kernel driver when Ubuntu changes its ABI. Before each driver update, test the new kernel and the actual speaker/Touch Bar/Wi-Fi behavior.

## Good public-release practices

- Make the README legible to Mac owners and keep one primary Download button.
- Use **pre-release** for anything not qualified on more models and kernel versions.
- Add a **Security** contact path and private vulnerability reporting before inviting a large audience.
- Don't upload machine logs, screenshots with device serials, proprietary Wi-Fi NVRAM, or external driver binaries without verified redistribution rights.
- Keep both sources and the exact released `.deb` so issues can be reproduced.
