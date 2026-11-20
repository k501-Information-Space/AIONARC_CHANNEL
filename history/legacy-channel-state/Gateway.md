# Gateway — AIONARC_CHANNEL

**Repository role:** `PUBLIC_SIGNAL_LAYER`  
**Namespace:** `K501-AIONARC`  
**Branch:** `main`  
**Gateway classification:** `NAVIGATION_ONLY`  
**Operator time anchor:** `1793389236` — 2026-10-30T19:40:36Z / 2026-10-30T20:40:36+01:00

## Common root entrypoints

- [README.md](README.md) — repository introduction and current public-signal state.
- [Gateway.json](Gateway.json) — machine-readable routes and role boundaries.
- [Index.md](Index.md) / [Index.json](Index.json) — non-exhaustive root entrypoint directory.
- [manifest.json](manifest.json) — channel publication/feed manifest.

## Channel-specific records

- [SIGNAL_0014 — QH_STATE_KERNEL V1 publication reference index](SIGNAL_0014_K501_QH_STATE_KERNEL_V1_PUBLICATION_REFERENCES.md) / [machine record](SIGNAL_0014_K501_QH_STATE_KERNEL_V1_PUBLICATION_REFERENCES.json) — current published signal.
- [SIGNAL_0013 — v3.5.0 public release](SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.md) / [machine record](SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.json) — previous published signal.
- [SIGNAL_0012 — QH256 state anchor](SIGNAL_0012_QH256_STATE_ANCHOR.md) / [machine record](SIGNAL_0012_QH256_STATE_ANCHOR.json) — earlier published state anchor.
- [JSON Feed](feed.json), [Atom](atom.xml), [RSS](rss.xml) and [public site](index.html).

## Current signal observation

`SIGNAL_0014` is the current published signal. The sequence contains 14 signals; `SIGNAL_0015` is next. Its operator-supplied registration anchor is `1795068779` (2026-11-19T06:12:59Z; 2026-11-19T07:12:59+01:00). It registers three separate external references: Zenodo records 24051677 and 24218851, plus the DEV.to article. Metadata and content boundaries are recorded in the paired signal documents.

## Role and authority boundary

AIONARC_CHANNEL is a public publication and signal layer. It does not replace the canonical K501-AIONARC information space, and its signal records are not proof of the underlying claims. This Gateway is navigation only; it does not confer canonicality, validate a signal or promote an unpublished state.

## Temporal preservation

The statement in the original SIGNAL_0013 context that Zenodo publication and a DOI remained open is preserved as a source-time statement. It must not be read as a live currentness claim. SIGNAL_0012 and SIGNAL_0013 remain unchanged; SIGNAL_0014 is appended as a new paired record.

## Gateway Standards reference package

- [Gateway Standards package](GATEWAY_STANDARDS/README.md) — six source-bound Library documents and paired Markdown/JSON records.
- [Machine index](GATEWAY_STANDARDS/README.json) / [source identity manifest](GATEWAY_STANDARDS/MANIFEST.json).

**Status:** non-canonical reference/navigation only. The register contract remains `FREEZE_CANDIDATE_NOT_FROZEN`; the separate support profile retains its own draft status. No schema, validator, crosswalk, adapter or achieved conformance level is asserted.

**Additive update 1:** operator anchor `1795068285` — 2026-11-19T06:04:45Z / 2026-11-19T07:04:45+01:00; based on parent commit `a0532df929467b30231be299fa392a6557efc87c`.

**Additive update 2:** signal registration anchor `${epoch}` — ${utc} / ${local}; based on parent commit `${head}`. New paired signal appended; prior signal records remain unchanged.

## Append-only boundary

Existing signal files are preserved. SIGNAL_0014 is appended to the feeds. Legacy uppercase Gateway paths and site assets remain at their established paths.
