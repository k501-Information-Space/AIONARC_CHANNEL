# Gateway Standards — AIONARC_CHANNEL

**Package ID:** `K501_GATEWAY_STANDARDS_REFERENCE_PACKAGE_0_1_0_DRAFT_1795068285_2026-11-19`  
**Schema ID:** `K501_GATEWAY_STANDARDS_REFERENCE_PACKAGE/0.1.0-draft`  
**Status:** `NON_CANONICAL_REFERENCE_PACKAGE; SOURCE_STATUSES_PRESERVED`  
**Operator anchor:** `1795068285` — 2026-11-19T06:04:45Z / 2026-11-19T07:04:45+01:00  
**Parent repository commit:** `a0532df929467b30231be299fa392a6557efc87c`

## Purpose and authority

This directory publishes a bounded set of K501 Library Gateway register-architecture and external-standard support documents through AIONARC_CHANNEL. It is a navigation and reference package only. It does not replace the Library sources, establish canonicality, freeze the register contract, validate the architecture, or assert implementation or conformance.

The six documents were transferred as separate GitHub blobs. Their exact Library paths, `file_id`, `library_file_id`, source sizes, artifact IDs, schema IDs and source statuses are recorded in [MANIFEST.json](MANIFEST.json). Original Library objects were not modified. GitHub blob IDs identify repository copies and do not replace Library identity. Byte identity across the transfer is not asserted.

## Read order

1. [Architecture Review](K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_REVIEW_v0.1.0-draft_1794951315_2026-11-17.md) — review disposition, corrections and schema prerequisites.
2. [Register Architecture Contract — Freeze Candidate](K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_CONTRACT_FREEZE_CANDIDATE_v0.1.0-draft_1794951315_2026-11-17.md) — reviewed candidate for the seven-register contract.
3. [Standard Support Profile](K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_v0.1.0-draft_1794950678_2026-11-17.md) — earlier support-profile draft, retained with original status and wording.
4. [Machine package index](README.json) and [source identity manifest](MANIFEST.json).

Each source artifact is published as a Markdown/JSON pair under its original filename.

## Seven-register architecture

1. `DIRECTORY_REGISTER`
2. `OBJECT_IDENTITY_REGISTER`
3. `ARTIFACT_REGISTER`
4. `DEEPREAD_REGISTER`
5. `INTEGRITY_REGISTER`
6. `PROVENANCE_AND_RIGHTS_REGISTER`
7. `ROUTE_REGISTRY`

The reviewed candidate defines a directional 7×7 relationship matrix. Rows are referencing/source registers; columns are referenced/target registers. Declared counts: 7 self-scope cells, 13 direct-reference relations, 29 cells with no mandatory direct architectural reference. A path is a locator, not identity. Directory observation does not create object identity. Artifact version and source-object identity are distinct. DeepRead and Integrity are separate evidence domains. Provenance and Rights remain separate record families within one register. A route is navigation, not validation or authorization.

## External standards targets

| Standard | Version / identity | Bounded purpose |
|---|---|---|
| JSON Schema | 2020-12 | Structural shape and permitted-value validation |
| W3C PROV-O | W3C Recommendation | Provenance representation |
| PREMIS | 3.0 | Preservation metadata mapping |
| BagIt | RFC 8493 | Package structure, manifests and scoped fixity |
| RO-Crate | 1.2 | Research-object description and contextual metadata |

RO-Crate 1.3 is not included by inference; it remains a separate compatibility review. Selecting a target version is not an implementation or conformance claim.

## Support and implementation state

The support progression is evidence-gated: `REGISTERED`, `PARSED`, `VALIDATED`, `MAPPED`, `EXPORTED` or `IMPORTED`, then `ROUNDTRIP_VERIFIED`. Export and import are separate directions. Round-trip verification requires a tested bidirectional cycle for the exact fixture and declared scope.

The source support profile states implementation is open/not implemented and achieved support levels are not assessed. No target is promoted to an achieved support level by this publication. No schemas, graph validator, crosswalks or adapters are created by this repository update.

## Status distinctions and open work

- Parent architecture freeze anchor `1794935960`: seven register names/order, five external-standard target versions and support-level direction.
- Architecture Review anchor `1794951315`: `PASS_WITH_REQUIRED_CORRECTIONS_AND_SCHEMA_PREREQUISITES`.
- Register Contract: `FREEZE_CANDIDATE_NOT_FROZEN`; publication does not freeze it.
- Separate support-profile documents retain `DRAFT_NON_CANONICAL_SUPPORT_PROFILE_PENDING_REVIEW`. Their earlier mappings remain source-time content; consult the later Review and Contract Candidate for subsequent corrections.
- Schema prerequisites `OPEN-01` through `OPEN-09` remain open.

## AIONARC_CHANNEL boundary

AIONARC_CHANNEL is a public signal/publication layer, not the canonical K501 Information Space. This package does not create `SIGNAL_0014`, change the 13-signal count, rewrite historical signals, or modify the legacy uppercase `GATEWAY.md` and `GATEWAY.json` channel-specific records.
