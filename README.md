# AIONARC_CHANNEL

**Role:** public reference and distribution channel for selected K501 Information Space sources  
**Active namespace:** `AIONARC_SIGNAL_NNNN` · **Assigned:** 17  
**Latest:** `AIONARC_SIGNAL_0017` · **Next:** `AIONARC_SIGNAL_0018` — OPEN / UNASSIGNED / NOT PUBLISHED

AIONARC_CHANNEL provides stable reference pages for operator-bound external destinations. It is a publication and distribution layer, not the canonical K501 Information Space. Registration does not establish the truth or canonicality of external source claims.

## Public channel

- [Index](index.html)
- [RSS 2.0](rss.xml) · [Atom 1.0](atom.xml) · [JSON Feed 1.1](feed.json)
- [Sitemap](sitemap.xml) · [robots.txt](robots.txt)
- [Active registry](signals/registry.json)

Channel permalinks and external target URLs are separate. Channel registration time is distinct from source publication dates. Missing metadata remains OPEN or UNKNOWN. Operator-supplied titles are preserved separately from independently observed source titles.

## Build and distribution

`signals/registry.json` is the single source for the homepage, detail pages, feeds and sitemap. Generated files remain in the repository root because the verified GitHub Pages publisher uses the `main` branch root.

IndexNow is restricted to AIONARC_CHANNEL-owned Pages URLs. External targets are not submitted as if they belonged to this host. WebSub publishes independently to Google PubSubHubbub (`https://pubsubhubbub.appspot.com/`, primary) and retains Switchboard (`https://switchboard.p3k.io/`) as a secondary declaration. Google acknowledged all three feed topics with HTTP 204; Switchboard currently returns HTTP 401. Publisher acknowledgement does not prove subscriber delivery.

## Historical generation

The prior `SIGNAL_NNNN` sequence is historical only and is not mapped to `AIONARC_SIGNAL_NNNN`. Its current-main files are preserved byte-for-byte under [history/legacy-channel-state/](history/legacy-channel-state/); Git history remains intact.

Frozen baseline: `ARCHITECTURE DRAFT · v0.1`. Implementation successor: [Architecture v0.2](architecture/AIONARC_CHANNEL_PUBLICATION_DISTRIBUTION_ARCHITECTURE_v0.2.0_1795187344_2026-11-20.md).

Author: Patrick R. Miller · Alias: iinkognit0 · [ORCID 0009-0004-3275-9545](https://orcid.org/0009-0004-3275-9545)
