# Compatibility

## Verified (limited physical testing)

| Mac | Ubuntu | Kernel | Test results |
| --- | --- | --- | --- |
| **MacBookPro13,2 (13-inch, Late 2016, T1 Touch Bar)** | 26.04.1 LTS | **7.0.0-43-generic** | Fresh-install v0.5.0 tested. Touch Bar, built-in speakers, keyboard and trackpad worked. Broadcom adapter enumerated and scanned 5 GHz networks; a Wi-Fi connection was not tested in that session. |
| Same model | 26.04.1 LTS | **7.0.0-30-generic** | Earlier v0.4 integration test completed; speakers, microphone, Touch Bar/function keys and Wi-Fi were reported working. |

This is **one physical MacBook**, not a statistical compatibility study. The 7.0.0-43 test did not validate suspend/resume, new-kernel rebuilds or the removal path.

## Not yet supported

- **MacBookPro13,3:** 15-inch 2016 Touch Bar, T1 but different hardware profile.
- **MacBookPro14,2 / 14,3:** 2017 T1 MacBook Pro models.
- Any other Mac, including 2018-and-newer **T2** Macs.
- Other Ubuntu releases, Linux distributions or kernel families outside `7.0.0-*-generic`.

The current installer's preflight intentionally **rejects other models**. We welcome [model-support requests](../.github/ISSUE_TEMPLATE/model-request.yml) to establish a separately verified compatibility path.

## Details

The current T1 integration assumes Apple T1 iBridge USB ID `05ac:8600`, Broadcom BCM43602 PCI ID `14e4:43ba`, and a Wi-Fi interface named `wlp2s0`. Hardware differences may cause the preflight to stop even on superficially similar Macs. That is deliberate, not an invitation to remove the checks.

The Cirrus CS8409 kernel patch is an unmerged compatibility change for Ubuntu's Linux 7 source. Builds are not guaranteed to work on future kernel revisions. [More about updates](UPDATES.md).
