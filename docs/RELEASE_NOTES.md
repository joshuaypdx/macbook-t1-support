# Help test MacBook T1 Support 0.6.0 Beta

Have a 2016 or 2017 MacBook Pro with Touch Bar running Ubuntu 26.04 LTS? We’re looking for reports from all four T1 models, especially the three new preview models.

- **MacBookPro13,2** keeps the full setup. The previous package worked on one MacBookPro13,2 running Ubuntu 26.04.1, kernel `7.0.0-43-generic`, from a Samsung T9 external SSD. A 0.6.0 regression report on this model is welcome.
- **MacBookPro13,3, MacBookPro14,2 and MacBookPro14,3** can opt into the **hardware-unverified Touch Bar preview**. The preview installs the iBridge/Touch Bar driver and excludes audio patches and Wi-Fi calibration. Check the FaceTime camera too, since it shares the iBridge.
- This is a prerelease with offline installer and package checks. 0.6.0 still needs testing on physical Macs.

Download `mbp132-support_0.6.0_all.deb` below, back up your important files and follow the [install and recovery guide](https://github.com/joshuaypdx/macbook-t1-support/blob/v0.6.0-beta.1/docs/INSTALL.md). Run the read-only preflight before installing drivers.

[Report a success or failure](https://github.com/joshuaypdx/macbook-t1-support/issues/new/choose). Include your model identifier, Ubuntu version, `uname -r`, preflight and reboot results, and what worked. Please redact serial numbers, MAC addresses and other identifiers.
