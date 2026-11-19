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

- [GATEWAY.md](GATEWAY.md) / [GATEWAY.json](GATEWAY.json) — preserved channel-specific Gateway records and original signal-layer contract.
- [SIGNAL_0013 — v3.5.0 public release](SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.md) / [machine record](SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.json) — current published signal at the last signal transition.
- [SIGNAL_0012 — QH256 state anchor](SIGNAL_0012_QH256_STATE_ANCHOR.md) / [machine record](SIGNAL_0012_QH256_STATE_ANCHOR.json) — previous published state anchor.
- [JSON Feed](feed.json), [Atom](atom.xml), [RSS](rss.xml) and [public site](index.html).

## Current signal observation

The root README and the existing channel Gateway identify `SIGNAL_0013` as current, with 13 signals and `SIGNAL_0014` as the next sequence position. Its publication anchor is `1793095162` (2026-10-27T09:59:22Z). This repository alignment does not create SIGNAL_0014 or alter the signal sequence.

## Role and authority boundary

AIONARC_CHANNEL is a public publication and signal layer. It does not replace the canonical K501-AIONARC information space, and its signal records are not proof of the underlying claims. This Gateway is navigation only; it does not confer canonicality, validate a signal or promote an unpublished state.

## Temporal preservation

The statement in the original SIGNAL_0013 context that Zenodo publication and a DOI remained open is preserved as a source-time statement. It must not be read as a live currentness claim. Neither SIGNAL_0012 nor SIGNAL_0013 is rewritten by this navigation update.

## Gateway Standards reference package

- [Gateway Standards package](GATEWAY_STANDARDS/README.md) — six source-bound Library documents and paired Markdown/JSON records.
- [Machine index](GATEWAY_STANDARDS/README.json) / [source identity manifest](GATEWAY_STANDARDS/MANIFEST.json).

**Status:** non-canonical reference/navigation only. The register contract remains `FREEZE_CANDIDATE_NOT_FROZEN`; the separate support profile retains its own draft status. No schema, validator, crosswalk, adapter or achieved conformance level is asserted.

**Additive update:** operator anchor `1795068285` — 2026-11-19T06:04:45Z / 2026-11-19T07:04:45+01:00; based on parent commit `a0532df929467b30231be299fa392a6557efc87c`.

## Append-only boundary

Existing signal files, feed chronology, legacy uppercase Gateway paths and site assets remain at their established paths. No new signal is created by this change.
