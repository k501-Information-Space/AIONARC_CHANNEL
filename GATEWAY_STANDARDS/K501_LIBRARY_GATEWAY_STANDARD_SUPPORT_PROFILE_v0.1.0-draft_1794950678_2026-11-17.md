# K501 Library Gateway Standard Support Profile — 0.1.0-draft

**Artifact ID:** `K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_0_1_0_DRAFT_1794950678_2026-11-17`  
**Schema ID:** `K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE/0.1.0-draft`  
**Status:** `DRAFT / NON-CANONICAL / SUPPORT_PROFILE_PENDING_REVIEW`  
**Operator GO anchor:** `1794950678` — 17 November 2026, 21:24:38 UTC / 22:24:38 CET  
**Parent architecture freeze:** `1794935960` — 17 November 2026, 17:19:20 UTC / 18:19:20 CET  
**Implementation:** `OPEN / NOT IMPLEMENTED`  
**Canonical:** `false`

## 1. Purpose and separation

This profile records the five external standards whose support direction was confirmed in the Gateway architecture freeze. It is a separate artifact from `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE/0.1.0-draft` and does not merge external standard models into the K501 native information model.

The set and version direction are frozen at the parent decision. This profile's detailed purpose boundaries and support descriptions remain draft pending review. The inclusion of a standard is a declared integration target, not an implementation, validation, interoperability, or conformance claim.

## 2. Frozen standard-support targets

| Standard | Frozen target version | Intended bounded use | Current implementation state |
|---|---|---|---|
| JSON Schema | 2020-12 | Structural shape and value constraints for future machine-readable K501 and adapter documents | OPEN / NOT IMPLEMENTED |
| W3C PROV-O | W3C Recommendation | Bounded provenance representation for source/derived entities, activities, and agents | OPEN / CROSSWALK NOT BUILT |
| PREMIS | 3.0 | Preservation metadata patterns for objects, events, agents, and rights evidence | OPEN / CROSSWALK NOT BUILT |
| BagIt | RFC 8493 | Package-level organization, payload manifests, tag files, and scoped fixity checks | OPEN / ADAPTER NOT BUILT |
| RO-Crate | 1.2 | Package-level research object description and contextual metadata | OPEN / ADAPTER NOT BUILT |

RO-Crate 1.3 is not part of the frozen target set. It remains subject to a separate compatibility review. No compatibility is inferred from RO-Crate 1.2.

## 3. Standard-specific boundaries

### 3.1 JSON Schema 2020-12

**Intended use:** Define and validate the structural shape and permitted value constraints of future machine-readable Gateway, register, and adapter documents.

**Boundary:** Schema validation checks conformance to a declared schema only. It does not prove that source values are true, paths exist, identifiers are authoritative, a source has been fully read, or the Library is complete.

Reference: https://json-schema.org/specification

### 3.2 W3C PROV-O

**Intended use:** Evaluate a bounded provenance representation for source and derived entities, read/transformation activities, and responsible agents.

**Boundary:** PROV-O is an external representation. It does not replace K501 object identities, source-scope rules, or status definitions. A K501–PROV-O crosswalk remains OPEN.

Reference: https://www.w3.org/TR/prov-o/

### 3.3 PREMIS 3.0

**Intended use:** Evaluate preservation metadata mappings for objects, preservation events, agents, and rights evidence.

**Boundary:** PREMIS preservation concepts do not replace K501 identity or canonical-state rules. A K501–PREMIS crosswalk remains OPEN.

Reference: https://www.loc.gov/standards/premis/v3/

### 3.4 RFC 8493 — BagIt

**Intended use:** Evaluate package-level organization, payload manifests, tag files, and scoped fixity verification for exchange or preservation packages.

**Boundary:** A valid BagIt package supports claims only about that bag and the payload scope actually checked. It does not imply Library-wide coverage, K501 semantic validity, or canonicality. Existing K501 checksum sidecars must not be described as BagIt packages unless they satisfy the actual BagIt requirements.

Reference: https://www.rfc-editor.org/rfc/rfc8493.html

### 3.5 RO-Crate 1.2

**Intended use:** Evaluate package-level research object description and contextual metadata for selected K501 artifacts and distributable collections.

**Boundary:** RO-Crate is not a replacement for the K501 file-level Object Identity Register, Directory Register, or DeepRead Register. RO-Crate 1.3 remains outside this target profile until a separate compatibility review is completed.

Reference: https://www.researchobject.org/ro-crate/specification/1.2/

## 4. Internal support-level model

The frozen progression is:

`REGISTERED → PARSED → VALIDATED → MAPPED → EXPORTED / IMPORTED → ROUNDTRIP_VERIFIED`

| Level | Meaning | Minimum evidence |
|---|---|---|
| `REGISTERED` | Exact external standard/version and intended K501 integration scope are recorded in a versioned profile. | Standard identifier/version, bounded purpose, authoritative reference. |
| `PARSED` | A concrete input document or payload representation has been parsed by an identified parser in the declared version scope. | Input identity and scope, parser/version, parse result and warnings. |
| `VALIDATED` | The parsed representation has passed declared syntax/schema/profile checks for the pinned standard version. | Validation profile/version, validator/version, report and result. |
| `MAPPED` | An explicit, versioned mapping to or from the K501 native model is defined and applied for a declared scope. | Mapping/crosswalk ID and version, field coverage, explicit unmapped/unsupported/loss records. |
| `EXPORTED` or `IMPORTED` | A concrete export or import operation has been performed and recorded through the declared adapter boundary. | Direction, source/output identities, adapter/version, time, transformation evidence. |
| `ROUNDTRIP_VERIFIED` | A bidirectional exchange cycle has passed a defined round-trip test for the exact fixture, fields, and invariants. | Input/export/import identities, adapter versions, fixture, expected invariants, observed result, losses, and report. |

A level is reached only when its evidence is recorded. No level is inferred from a filename, target selection, successful parsing alone, or an unsupported later-stage claim. `ROUNDTRIP_VERIFIED` applies only to the tested scope; it is not a universal semantic-equivalence or full-system conformance claim. A one-way adapter may be recorded as `EXPORTED` or `IMPORTED`, but it is not round-trip verified.

## 5. Current support state

The five standards are frozen integration targets. Their detailed adapter execution state and achieved support levels have not been assessed by this profile. The profile does not claim that any parser, validator, mapper, exporter, importer, or round-trip test exists.

| Item | State |
|---|---|
| Standard-support direction | FROZEN |
| Detailed support profile | DRAFT / REVIEW OPEN |
| Implementation | OPEN / NOT IMPLEMENTED |
| PROV-O / PREMIS crosswalks | OPEN |
| BagIt / RO-Crate adapters | OPEN |
| Achieved support levels | NOT ASSESSED |
| RO-Crate 1.3 compatibility | OPEN / SEPARATE REVIEW |
| Canonicalization | NOT AUTHORIZED |

## 6. Cross-standard operating constraints

1. K501 remains the native information model and retains its own identifiers, sources, temporal references, and status definitions.
2. External standards are connected through versioned adapters and bounded interfaces only.
3. Original data and derived external representations remain separate.
4. A mapping never redefines K501 identity or status semantics.
5. Validation is not proof of truth, source completeness, permission, or canonicality.
6. Unmapped, unsupported, and lossy fields must remain visible and traceable.
7. Exact standard editions and versions must be pinned; version changes require separate review.
8. `OPEN` does not mean `PASS`; `UNKNOWN` does not mean `FALSE`.

## 7. Source basis

- `K501_LIBRARY_GATEWAY_REVIEW_VALIDATION_REPORT_1794932044_2026-11-17.md` — comparative research references for the five standards; no adoption or conformance was asserted by that report.
- User-confirmed Gateway architecture freeze, anchor `1794935960` — five target versions, support-level progression, and architecture boundaries.

**Disposition:** `STANDARD_SUPPORT_DIRECTION=FROZEN` · `PROFILE_DETAIL=DRAFT` · `IMPLEMENTATION=OPEN` · `ACHIEVED_SUPPORT_LEVELS=NOT_ASSESSED` · `CANONICALIZATION=NOT_AUTHORIZED`