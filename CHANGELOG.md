# Changelog

## 0.6.1 Beta

- Test Touch Bar, Wi-Fi and audio across all four T1 models with the new testing command.
- Opt into subsystem-matched audio on preview models, board-checked calibration on MacBookPro14,2 and optional keyboard backlight. Each trial has its own rollback command.
- Preserve existing full and Touch Bar installations during package upgrade.

## 0.6.0 Beta

- Add model-specific preflight and a separately confirmed Touch Bar preview for MacBookPro13,3, MacBookPro14,2 and MacBookPro14,3.
- Keep the MacBookPro13,2 full profile. Exclude board-specific audio and Wi-Fi configuration on preview models.
- Scope repair, removal and DKMS diagnostics to the recorded installation model and its components.
- Add offline safety coverage and publish a new package with a SHA-256 checksum.

## 0.5.0 Beta (2026-11-10 public repository candidate)

- Includes the tested v0.5.0 integration `.deb` and matching source tree.
- Fresh-install test completed on **MacBookPro13,2 / Ubuntu 26.04.1 / `7.0.0-43-generic`** from an external Samsung T9, with functioning internal speakers, Touch Bar and input devices. Wi-Fi driver enumerated and scanned networks.
- Adds GitHub onboarding, bug-report forms, compatibility chart, update warnings and source validation tests.
- **No new driver changes in this GitHub packaging release.**
- Known shortcomings: inconsistent `status` health report on the fresh install and fallback-kernel logic still favoring `7.0.0-30-generic` even when that kernel is absent. See [Known issues](docs/KNOWN_ISSUES.md).

## Planned 0.5.1 (not yet released)

- Improve install-state and DKMS status parsing, including valid `installed (Original modules exist)` output.
- Align fallback protection with a hardware-confirmed kernel rather than a stale hard-coded version.
- Improve plain-English diagnostics and usability tests.
- Test upgrade and removal paths before issuing a replacement `.deb`.

## Future

- Guided graphical installer and signed package distribution.
- More T1 model validation, each with explicit compatibility gates.
- Separate eGPU project after its beta testing is complete.
