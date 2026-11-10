# Attribution and third-party notices

The repository's **original integration scripts and documentation** are distributed under [MIT](LICENSE). This MIT license **does not relicense** upstream drivers or firmware.

The installer fetches three external projects at **specific Git commit hashes**, verifies the checked-out revisions, and builds/configures their contents locally after explicit user consent. The downloadable `.deb` includes our integration utility and package metadata. It does not ship upstream driver source, compiled driver binaries, or the Broadcom Wi-Fi NVRAM file.

| Component | Upstream project | Pinned commit |
| --- | --- | --- |
| Audio CS8409 patch | [duzelli/snd_hda_macbookpro](https://github.com/duzelli/snd_hda_macbookpro) | `3414707841e7a518707be4748cd8787794e19045` |
| T1 Touch Bar / iBridge | [AJ-dev-i60/t1-touchbar](https://github.com/AJ-dev-i60/t1-touchbar) | `20d65c7b0fe6d05ea9734f869b27384a62de5109` |
| Wi-Fi NVRAM | [DeyAgrO/macbook-pro-13-2-linux](https://github.com/DeyAgrO/macbook-pro-13-2-linux) | `c005707321186f6ac6ac81fbe577226189568f69` |

The T1 driver is described upstream as GPL-2.0; consult the original repositories for the current legal terms and their respective copyright owners. The Wi-Fi NVRAM is community-distributed and its calibration, licensing, and RF/regulatory provenance need further review. **Do not redistribute that NVRAM directly under this repository's MIT license.**

This project is not affiliated with, sponsored by, or endorsed by Apple, Canonical, Ubuntu, Broadcom, or the upstream authors. Apple and Ubuntu names and trademarks belong to their owners.

The integration runs downloaded source code and an upstream audio install script with elevated privileges. Pinning a Git commit reduces inadvertent changes but does not replace an independent security audit. If this matters to you, review the source and upstream repositories before installing.
