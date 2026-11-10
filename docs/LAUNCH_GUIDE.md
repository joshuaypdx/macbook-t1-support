# Publish MacBook T1 Support on GitHub (using your Mac)

**No terminal and no coding required.** You're publishing a repository that already contains its files, source, installer and user support forms.

## 1. Create a GitHub account

Visit [github.com/signup](https://github.com/signup), choose a username and verify your email. If you already have an account, sign in instead. Turn on two-factor authentication in account settings.

## 2. Install GitHub Desktop on macOS

Visit [desktop.github.com](https://desktop.github.com/). Choose the **Intel Mac** download if you're using your 2016 MacBook. Install GitHub Desktop and sign in to your GitHub account.

> **Why Desktop?** GitHub's website does not unpack a ZIP archive into a repository. GitHub Desktop can publish a prepared project *as-is*, preserving its folders and automated feedback forms.

## 3. Unzip the prepared project

Open the supplied `macbook-t1-support-github-starter.zip` in macOS Finder. You'll get a folder named `macbook-t1-support`. Leave its contents alone, including invisible Git metadata. **Do not upload the ZIP itself to the GitHub website** and do not create an empty repository first.

## 4. Publish with GitHub Desktop

1. In GitHub Desktop, choose **File → Add Local Repository…**.
2. Select the unzipped **`macbook-t1-support`** folder and click **Add Repository**.
3. Click **Publish repository** near the top.
4. Keep the repository name `macbook-t1-support` or choose another public-facing name.
5. **Uncheck “Keep this code private”** when you're ready for others to see it. Leave owner set to your GitHub account.
6. Click **Publish Repository**. Then use **Repository → View on GitHub**.

Your README is now your project's home page. The installer and source are there. The issue forms are available in **Issues → New issue**. The starter archive was already committed locally; you don't need to write any code or commit it yourself to publish the first version.

## 5. One-time repository settings (web interface)

1. Select **Settings**. Ensure **Issues** are enabled under repository features.
2. Optionally enable **Discussions** so newcomers can ask questions separately from bug reports.
3. In the repository's right-hand **About** area, click the gear icon, and add topics: `macbook`, `ubuntu`, `linux`, `touchbar`, `apple-t1`, `macbookpro13-2`.
4. In **Settings → Security**, enable **Private vulnerability reporting** if offered. Until then, ask people not to post security details publicly.
5. Confirm the **Actions → Check installer package** workflow passes. If not, stop and review its output before advertising a release.

## 6. Publish the first downloadable beta release (optional, recommended)

The README already offers a direct package download immediately after Step 4. For a conventional GitHub **Releases** page, use one of these easy methods:

**Method A: Fully through the website.** Open **Releases → Draft a new release**, create tag `v0.5.0-beta.1`, title it `MacBook T1 Support 0.5.0 Beta`, mark **This is a pre-release**, attach `mbp132-support_0.5.0_all.deb` from the starter's `packages/` folder, then publish. Paste the text in `docs/RELEASE_NOTES.md` as its description.

**Method B: One-click automated release.** Open **Actions → Publish beta release → Run workflow**, enter `v0.5.0-beta.1` and click **Run workflow**. The workflow validates source/package consistency, then makes the pre-release and attaches the `.deb`. If Actions requests workflow permission, grant it for this trusted repository. Do not publish if validation fails. Use **A OR B**, not both with the same tag.

## 7. Receive feedback and updates

- Every GitHub account can open **Issues → New issue** and complete the pre-made forms.
- When someone reports a problem, you'll receive GitHub notifications according to your notification settings.
- To revise documentation: edit via the GitHub web pencil icon, or replace files in the local repo and click **Commit** and **Push origin** in GitHub Desktop.
- To publish a new package, use the process in [MAINTAINERS.md](MAINTAINERS.md), and create a **new release tag**.
- Github repository **Watch** options let testers opt into release updates. Installing a new `.deb` remains a manual step for them; there is no auto-update channel yet.

## Before a wider announcement

Check the actual download link; ensure the `.deb` matches the source and the real tested kernel. Prominently state that this is a beta for `MacBookPro13,2` only, and that `mbp132-support status` and fallback-kernel tracking need improvement. Do not promise Touch ID, all T1 Macs or flawless future kernel updates. The Wi-Fi NVRAM's provenance and RF/regulatory implications deserve additional review.

**Ready for a community beta is not the same thing as ready to recommend to every Mac owner.** Consider a limited, clearly labeled beta invitation first.
