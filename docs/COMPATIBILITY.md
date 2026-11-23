# Hardware compatibility

| Model identifier | Apple model | 0.6.0 install profile | Project hardware evidence |
| --- | --- | --- | --- |
| MacBookPro13,2 | 13-inch Late 2016, four Thunderbolt 3 ports | Full | v0.5.0 tested on Ubuntu 26.04.1, `7.0.0-43-generic`, from a Samsung T9 |
| MacBookPro13,3 | 15-inch Late 2016 | Touch Bar beta | Unverified |
| MacBookPro14,2 | 13-inch Mid 2017, four Thunderbolt 3 ports | Touch Bar beta | Unverified |
| MacBookPro14,3 | 15-inch Mid 2017 | Touch Bar beta | Unverified with this package. The pinned upstream driver reports its own test on Ubuntu 26.04 with `7.0.0-27-generic`. |
| MacBookPro13,1 and MacBookPro14,1 | 13-inch, two Thunderbolt 3 ports | Ineligible | No T1 Touch Bar |
| All other model IDs | Includes T2 Macs and Apple silicon | Ineligible | Outside the allowlist |

The MacBookPro13,2 baseline recorded working Touch Bar, internal speakers, microphone, FaceTime HD camera, keyboard, trackpad and Wi-Fi. The same full integration remains model-restricted in 0.6.0. It uses the exact matching Ubuntu kernel source for audio and requires the original Broadcom hardware checks.

All profiles require Ubuntu 26.04 amd64, a `7.0.0-*-generic` kernel, a normally enumerated T1 iBridge (`05ac:8600`), and a compatible Secure Boot state. The Touch Bar preview also requires EFI boot and matching headers. It installs the shared iBridge/Touch Bar driver and its configuration. Because the camera uses the same bridge, test it after reboot. Audio patches and Wi-Fi calibration are excluded from the preview.

Sources: [Apple model identifiers](https://support.apple.com/en-us/108052), [T1 USB identity and models](https://cgit.libimobiledevice.org/libirecovery.git/commit/README.md?id=42f2c26463da466f42d207b9c0094df0d351d47a), [pinned Touch Bar upstream](https://github.com/AJ-dev-i60/t1-touchbar/tree/20d65c7b0fe6d05ea9734f869b27384a62de5109).

See the [installation and recovery guide](INSTALL.md).
