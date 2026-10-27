# SIGNAL_0013 — K501 AIONARC Integrated Pipeline & Proof Runtime v3.5.0: Public Release and Download

- **Signal type:** `PUBLIC_RELEASE_ANNOUNCEMENT`
- **Time anchor:** `1793095162`
- **UTC:** `2026-10-27T09:59:22Z`
- **Europe/Berlin:** `2026-10-27T10:59:22+01:00`
- **Release published:** `2026-10-27T09:26:45Z`
- **Package version:** `3.5.0` — Stable integrated package
- **Source commit:** [`946836c3d160ce25d38d5456baa8ed586a1ecd05`](https://github.com/k501-Information-Space/K501-AIONARC/commit/946836c3d160ce25d38d5456baa8ed586a1ecd05)

## The release is public and downloadable

**K501 AIONARC Integrated Pipeline & Proof Runtime v3.5.0 is published.** This is a versioned, downloadable source package with prebuilt Linux x86-64 executables—not merely a roadmap, proposal, or Zenodo draft.

**[Download the v3.5.0 ZIP archive](https://github.com/k501-Information-Space/K501-AIONARC/releases/download/v3.5.0/K501-AIONARC-Integrated-Pipeline-and-Proof-Runtime_v3.5.0_Stable.zip)**

[Open the GitHub release page](https://github.com/k501-Information-Space/K501-AIONARC/releases/tag/v3.5.0) · [Inspect the source repository](https://github.com/k501-Information-Space/K501-AIONARC)

- **Archive:** `K501-AIONARC-Integrated-Pipeline-and-Proof-Runtime_v3.5.0_Stable.zip`
- **Size:** 618,739 bytes
- **SHA-256:** `774cbf18d4674b657bafc859cda4b8b2a2dddcb2a283f70925510d4ae2d85223`
- **Tag:** [`v3.5.0`](https://github.com/k501-Information-Space/K501-AIONARC/releases/tag/v3.5.0)
- **Source commit:** [`946836c3d160ce25d38d5456baa8ed586a1ecd05`](https://github.com/k501-Information-Space/K501-AIONARC/commit/946836c3d160ce25d38d5456baa8ed586a1ecd05)

GitHub's published-release API reports the uploaded asset's size and SHA-256 as matching the locally verified archive. A separate remote download-and-rehash was not performed while preparing this signal.

## What v3.5.0 contains

The integrated package combines two retained components:

- **AIONARC Pipeline `3.0.0-alpha.1`:** read-only structural source observation, append-only frames, source-bound text extraction, verification, exact lexical queries, trace/history/diff operations, and its versioned QH256 V3A1 application mapping.
- **Proof/Evidence Runtime `0.1.0-alpha.1`:** controlled process invocation, transcript and host/run metadata capture, result recording, and evidence-file digests.

The integration test invokes the pipeline as a separate process. Evidence records remain evidence; a process exit code does not automatically promote a project gate.

**Version boundary:** `3.5.0` is the version of the integrated package. The embedded component identities are preserved and have not been individually re-versioned as stable releases.

## Verification and scope

Pre-publication evidence records PASS for source/archive parity, aggregate build and component tests, cross-component process integration, schema/specification/index/manifest/checksum verification, declared-host smoke checks, and same-host reproducibility in the recorded Linux x86-64 environment. See the [validation report](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/validation/VALIDATION_REPORT.md).

These results are bounded to the recorded artifacts, host, and toolchain. They do not guarantee that every build or deployment on every platform will succeed. The shipped AIONARC executable is qualified for Linux x86-64 and GLIBC symbols through 2.34. PDF extraction is optional and requires `pdftotext`.

## Try it

The package documents these commands:

```sh
make clean
make all
make test
make verify
```

Requirements: POSIX/Linux, GNU Make, a C11 compiler, Python 3, and `sha256sum`. See the [README and build guide](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/README.md) and [operator manual](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/docs/OPERATOR_MANUAL.md).

After downloading, verify the file locally:

```sh
sha256sum K501-AIONARC-Integrated-Pipeline-and-Proof-Runtime_v3.5.0_Stable.zip
```

Expected SHA-256: `774cbf18d4674b657bafc859cda4b8b2a2dddcb2a283f70925510d4ae2d85223`.

## Licensing and reuse

The package contains a file-level license map and rights/notice records. K501-authored code/software is mapped to MIT and K501-authored documentation/descriptive material to CC BY 4.0. Embedded upstream and third-party notices and per-file mappings remain applicable. Review [LICENSE_SCOPE.md](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/LICENSE_SCOPE.md) and the [aggregate file-license map](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/LICENSES/AGGREGATE_FILE_LICENSE_MAP.csv) before reusing individual files.

## Call for independent use

Researchers and developers: **download v3.5.0, inspect it, run the checks, and test it against your own clearly bounded cases.** Independent evaluations, reproducible issue reports, integrations, and forks are the intended next step. The aim is to provide a traceable baseline others can use and extend.

Zenodo publication and a DOI remain open and are not claimed here.

## Canonical references

- [Release and download](https://github.com/k501-Information-Space/K501-AIONARC/releases/tag/v3.5.0)
- [Direct ZIP download](https://github.com/k501-Information-Space/K501-AIONARC/releases/download/v3.5.0/K501-AIONARC-Integrated-Pipeline-and-Proof-Runtime_v3.5.0_Stable.zip)
- [Source repository](https://github.com/k501-Information-Space/K501-AIONARC)
- [Published source commit](https://github.com/k501-Information-Space/K501-AIONARC/commit/946836c3d160ce25d38d5456baa8ed586a1ecd05)
- [Validation report](https://github.com/k501-Information-Space/K501-AIONARC/blob/v3.5.0/validation/VALIDATION_REPORT.md)
- [AIONARC_CHANNEL homepage](https://k501-information-space.github.io/AIONARC_CHANNEL/)
- [Machine-readable signal](https://github.com/k501-Information-Space/AIONARC_CHANNEL/blob/main/SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.json)

---

`PROOF BEFORE STATE` · `RECONSTRUCT BEFORE EXTEND` · `OPEN UNTIL PASS`
