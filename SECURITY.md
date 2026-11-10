# Security policy

This is a community beta that installs kernel drivers and executes root-level integration code. There is no security guarantee and no signed distribution mechanism yet.

For private security reports, **do not open a public issue containing an exploit or secrets**. After the repository is published, enable **Settings → Security → Private vulnerability reporting** (where available), then use GitHub's **Report a vulnerability** feature. Until it is configured, do not send sensitive findings or logs through public Issues.

The installer checks exact Git commits for upstream downloads, but third-party dependencies, Wi-Fi calibration data and future kernel compatibility require ongoing review. No automatic update to a new installer is deployed to users.
