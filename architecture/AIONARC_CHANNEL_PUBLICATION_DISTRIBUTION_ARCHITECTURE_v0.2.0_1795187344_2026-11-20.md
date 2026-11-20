# AIONARC_CHANNEL — Publication and Distribution Architecture

**Version:** 0.2.0 successor alignment  
**Status:** operator-GO implementation baseline; non-canonical  
**GO anchor:** 1795187344 — 2026-11-20T15:09:04Z / 2026-11-20T16:09:04+01:00  
**Parent Pages commit:** e043179c6f07216a0cc5ca702516de3833a0009c

## 1. Relationship to frozen v0.1

The operator-confirmed ARCHITECTURE DRAFT v0.1 remains a frozen historical planning snapshot. This successor does not rewrite it. The active namespace is AIONARC_SIGNAL_NNNN, assigned 0001–0017. AIONARC_SIGNAL_0018 remains OPEN and unassigned. The prior SIGNAL_NNNN sequence is historical only, with no automatic identity mapping.

## 2. Verified Pages source mode

The parent main commit had a successful GitHub dynamic Pages deployment (run 44472216721, run 55, path dynamic/pages/pages-build-deployment, completed/success). No checked-in Pages workflow or site/ folder existed. The successor therefore keeps generated public files in the repository root to preserve the existing Pages publisher. It does not switch Pages settings to GitHub Actions.

The new workflows validate root output and issue external notifications after deployed URLs expose the new registry marker. The notification workflow is not the Pages deployment workflow.

## 3. Single source and projections

signals/registry.json is the single source for all 17 references. The builder creates root index.html, 17 detail pages, RSS 2.0, Atom 1.0, JSON Feed 1.1, robots.txt and sitemap.xml. Channel permalinks and external target URLs are separate identities. JSON Feed uses url for the channel page and external_url for the external target.

Channel registration time is not external source publication time. Dates appear only where observed on source records. Missing titles, descriptions and dates remain OPEN or UNKNOWN. Operator-supplied titles remain separate from independently observed source titles.

## 4. Legacy preservation

The former current-main root projection and paired records move to history/legacy-channel-state/ using existing Git blob objects. Source bytes are not rewritten. Git history remains intact. GATEWAY_STANDARDS/, LICENSE and icon.png remain at their existing paths.

## 5. IndexNow

IndexNow is the search-engine URL notification mechanism; WebSub is feed distribution. API endpoint: https://api.indexnow.org/indexnow. The verification file is https://k501-information-space.github.io/AIONARC_CHANNEL/7bd06f0b51434af617d988f6fb785a171f45d28f5a8930ebf66e9958472a0a51.txt. Because this is a GitHub Pages project path, each request includes keyLocation; the key location scopes submissions to https://k501-information-space.github.io/AIONARC_CHANNEL/.

Only AIONARC_CHANNEL-owned public HTML pages are submitted. The 17 external target URLs are never submitted as if they belonged to this Pages host. HTTP 200 indicates submission receipt; HTTP 202 indicates acceptance with key validation pending. Neither proves crawling or indexing.

## 6. WebSub through Switchboard

The operator selected https://switchboard.p3k.io/. RSS and Atom include self and hub links. JSON Feed 1.1 contains a hubs declaration of type WebSub. After deployment and public HTTP verification, the workflow sends hub.mode=publish for each changed topic feed.

Switchboard fetches the topic and notifies active subscribers. Publisher-side response does not prove a subscriber has subscribed, received or processed the notification. GitHub Pages remains a static publisher, not a hub or subscriber callback endpoint.

## 7. Workflow order

BUILD → VALIDATE → DEPLOY (GitHub Pages dynamic branch publisher) → HTTP VERIFY → INDEXNOW NOTIFY → WEBSUB PUBLISH

Pull requests run validation. After a change reaches main, the notification workflow verifies public pages, feeds and the key URL before sending notifications. Protocol receipt, subscriber delivery and search indexing remain separate.

## 8. Validation boundary

The validator checks the exact 17-entry registry sequence; no assigned AIONARC_SIGNAL_0018; unique targets; channel-page mapping; JSON Feed 1.1 structure; RSS/Atom well-formedness; feed consistency; Sitemap ownership scope; IndexNow key filename/content; and retired SIGNAL_NNNN absence from active outputs.

## 9. Authority and invariants

This architecture and its outputs remain publication-layer artifacts, not canonical K501 state. The registry controls this repository's projections only; it does not replace the operator binding or underlying external sources.

PROOF_BEFORE_STATE · RECONSTRUCT_BEFORE_EXTEND · OBSERVE_BEFORE_MUTATE · PURE_LOGIC · APPEND_ONLY · NO_DRIFT · NO_INTERPRETATION · NO_PHANTOM · UNKNOWN_BY_DEFAULT · TRACEABILITY_REQUIRED · TEMPORAL_CONSISTENCY · DENSIFICATION_WITHOUT_ERASURE
