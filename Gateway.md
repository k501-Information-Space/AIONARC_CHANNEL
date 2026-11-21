# AIONARC_CHANNEL Gateway

**Repository:** `k501-Information-Space/AIONARC_CHANNEL`  
**Role:** `PUBLIC_REFERENCE_AND_DISTRIBUTION_CHANNEL`  
**Authority:** navigation only; registry and source evidence retain their own scopes.

## Start here

- [README](README.md) — overview and boundaries.
- [Active registry](signals/registry.json) — 17 operator-bound IDs and URLs.
- [Public index](index.html) — channel pages.
- [Manifest](manifest.json).
- [Navigation Index](Index.md) / [Index.json](Index.json).

## Feeds and discovery

- [RSS 2.0](rss.xml) · [Atom 1.0](atom.xml) · [JSON Feed 1.1](feed.json)
- [Sitemap](sitemap.xml) · [robots.txt](robots.txt)

WebSub hubs: https://pubsubhubbub.appspot.com/ (primary) · https://switchboard.p3k.io/ (retained secondary; current POST status 401)  
IndexNow API: `https://api.indexnow.org/indexnow`

Google PubSubHubbub acknowledged RSS, Atom and JSON Feed publisher announcements with HTTP 204. Switchboard remains as secondary declaration but currently returns HTTP 401. Publisher acknowledgement does not prove subscriber delivery. IndexNow receives only URLs hosted under `https://k501-information-space.github.io/AIONARC_CHANNEL/`; external targets are not submitted as owned URLs.

## Identity boundaries

Active namespace: `AIONARC_SIGNAL_NNNN`, assigned 0001–0017. `AIONARC_SIGNAL_0018` remains OPEN / UNASSIGNED. The former `SIGNAL_NNNN` sequence is historical only and is not remapped.

Page permalinks and external target URLs are distinct. Source dates are separate from channel registration time. This Gateway and the Index are navigation surfaces, not proof of source truth or canonicality.

## Build and validation

- `scripts/build.py` — deterministic root-site generator.
- `scripts/validate.py` — registry and projection validation.
- `.github/workflows/validate.yml` — pull-request validation.
- `.github/workflows/aionarc-notify.yml` — post-deployment IndexNow and dual-hub WebSub publishing.
- `architecture/AIONARC_CHANNEL_WEBSUB_DISTRIBUTION_OBSERVATION_1795250522_2026-11-21.md` — bounded publisher-response evidence.

GitHub Pages currently publishes from the repository root on `main`. Frozen baseline: `ARCHITECTURE DRAFT · v0.1`. Successor: [Architecture v0.2](architecture/AIONARC_CHANNEL_PUBLICATION_DISTRIBUTION_ARCHITECTURE_v0.2.0_1795187344_2026-11-20.md).
