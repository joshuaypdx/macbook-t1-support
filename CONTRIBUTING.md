# Help make MacBook T1 Support better

You don't need to be a programmer.

**If you installed it successfully:** open a [feedback report](.github/ISSUE_TEMPLATE/success-report.yml). Tell us the Mac model, Ubuntu version, running kernel and which functions work. New hardware results are particularly valuable.

**If something doesn't work:** open a [bug report](.github/ISSUE_TEMPLATE/bug-report.yml). Describe the problem in your own words and avoid sending private device identifiers.

**If you're a developer:** open an issue describing the proposed change before implementing kernel-level patches. Keep changes limited in scope, include tests, and avoid bundling proprietary firmware or third-party code without checking its license. The integration source is in [`src/`](src/); run `python3 src/tests/test_package.py` and `python3 tests/verify-release.py`.

**If you're testing a different T1 Mac:** please open a model-support issue first. Do **not** bypass the model gate or transplant the Wi-Fi NVRAM to another model without validating hardware and RF compatibility.

Maintainers welcome: triage bug reports, ask for reproduction steps, maintain readable documentation and test safe releases. Personal machine logs should not be posted without redaction.
