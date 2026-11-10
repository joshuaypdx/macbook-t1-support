# Optional eGPU support (future separate beta)

**Not part of the MacBook T1 Support 0.5.0 download.**

A separate experimental project, **eGPU Lab / MacBook T1 eGPU Support**, has demonstrated dual display operation on one **MacBookPro13,2**, running Ubuntu 26.04.1 kernel `7.0.0-43-generic` with a **Razer Core X Chroma** Thunderbolt 3 enclosure and an **ASUS Radeon RX 6800 XT**.

The experiment uses an Apple EFI helper to expose the Intel GPU and a targeted PCIe memory-resource repair before AMDGPU initializes. A fresh-install release candidate successfully passed one-time and persistent cold boots on a Samsung T9 installation.

That code is **not bundled here** because it performs kernel-level PCIe resource manipulation and is not yet safe to recommend generally. It has not been validated across T1 models, GPUs, kernels, ports, suspend or controlled GPU removal.

**Planned independent repository:** `macbook-t1-egpu` (working name). This folder is a placeholder only. No eGPU features or modifications are installed by `mbp132-support`.
