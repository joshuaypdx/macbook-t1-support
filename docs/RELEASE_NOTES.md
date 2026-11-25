# MacBook T1 Support 0.6.1 Beta

Test Touch Bar, Wi-Fi and audio on the four 2016–2017 T1 MacBook Pro models running Ubuntu 26.04. Run `mbp132-support testing` to see the checks and eligible commands for your Mac.

- **MacBookPro13,2** retains the full installation previously tested with 0.5.0.
- **MacBookPro14,2** can try the Touch Bar, opt into subsystem-matched audio and, if stock Wi-Fi fails, try calibration after the installer confirms the Apple 0157 board.
- **MacBookPro13,3 and MacBookPro14,3** can try the Touch Bar, stock Wi-Fi and subsystem-matched audio. Calibration writes are disabled on these 15-inch boards.

The three preview models are hardware-unverified with this package. Compare camera preview before and after Touch Bar setup. For audio, use low desktop volume and report speakers, headphones and mic separately. For Wi-Fi, report joining, transferring data and reconnecting after reboot on each available band.

Download the Debian package below. Existing installations can upgrade the utility directly. [Installation and rollback](https://github.com/joshuaypdx/macbook-t1-support/blob/v0.6.1-beta.1/docs/INSTALL.md) · [Send a test report](https://github.com/joshuaypdx/macbook-t1-support/issues/new/choose) · [Earlier releases](https://github.com/joshuaypdx/macbook-t1-support/releases)
