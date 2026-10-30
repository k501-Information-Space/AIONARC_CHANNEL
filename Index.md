# Index — AIONARC_CHANNEL Root Navigation Directory

**Repository role:** `PUBLIC_SIGNAL_LAYER`  
**Classification:** `DERIVED_ROOT_NAVIGATION_DIRECTORY`  
**Completeness:** `NON_EXHAUSTIVE_ROOT_ENTRYPOINTS_ONLY`  
**Basis:** `0344feeb98c7af4a21271c69a39076e9edac3f65`  
**Operator time anchor:** `1793389236` (2026-10-30T19:40:36Z)

This Index maps the common root entrypoints and selected channel-specific root records. It is not a recursive repository inventory, a content hash manifest, a validation result or an authority declaration. The current and previous signal records are listed by their exact registered paths and remain unchanged.

| Path | Declared class | Relation |
|---|---|---|
| `README.md` | `HUMAN_ENTRY` | `CURRENT_ROOT` |
| `Gateway.md` | `HUMAN_GATEWAY` | `COMMON_ROOT_ENTRYPOINT` |
| `Gateway.json` | `MACHINE_GATEWAY` | `COMMON_ROOT_ENTRYPOINT` |
| `Index.md` | `HUMAN_INDEX` | `COMMON_ROOT_ENTRYPOINT` |
| `Index.json` | `MACHINE_INDEX` | `COMMON_ROOT_ENTRYPOINT` |
| `GATEWAY.md` | `CHANNEL_SPECIFIC_GATEWAY` | `PRESERVED_LEGACY_ENTRYPOINT` |
| `GATEWAY.json` | `CHANNEL_SPECIFIC_GATEWAY` | `PRESERVED_LEGACY_ENTRYPOINT` |
| `SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.md` | `PUBLIC_SIGNAL` | `CURRENT_SIGNAL_HUMAN` |
| `SIGNAL_0013_K501_AIONARC_V3_5_0_PUBLIC_RELEASE.json` | `PUBLIC_SIGNAL` | `CURRENT_SIGNAL_MACHINE` |
| `SIGNAL_0012_QH256_STATE_ANCHOR.md` | `PUBLIC_SIGNAL` | `PREVIOUS_SIGNAL_HUMAN` |
| `SIGNAL_0012_QH256_STATE_ANCHOR.json` | `PUBLIC_SIGNAL` | `PREVIOUS_SIGNAL_MACHINE` |
| `manifest.json` | `CHANNEL_MANIFEST` | `CURRENT_CHANNEL_METADATA` |
| `feed.json` | `JSON_FEED` | `PUBLIC_FEED` |
| `atom.xml` | `ATOM_FEED` | `PUBLIC_FEED` |
| `rss.xml` | `RSS_FEED` | `PUBLIC_FEED` |
| `index.html` | `PUBLIC_SITE` | `SITE_ENTRY` |
| `icon.png` | `SITE_ASSET` | `SITE_RESOURCE` |
| `LICENSE` | `LICENSE_DOCUMENT` | `REPOSITORY_METADATA` |

## Preserved boundary

- `GATEWAY.md` and `GATEWAY.json` remain the channel-specific Gateway records; they are not deleted or renamed.
- `SIGNAL_0012` and `SIGNAL_0013` remain append-only source records.
- `manifest.json` remains the channel publication/feed manifest; it is not an aggregate content checksum manifest.
- Feed and site files remain in their existing locations.
- This Index does not assert canonical authority, validation or completeness.
