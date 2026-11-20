# K501 Library Gateway Register Architecture Contract — Freeze Candidate 0.1.0-draft

**Artifact ID:** `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_CONTRACT_FREEZE_CANDIDATE_0_1_0_DRAFT_1794951315_2026-11-17`  
**Schema ID:** `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_CONTRACT/0.1.0-draft`  
**Status:** `FREEZE_CANDIDATE_NOT_FROZEN`  
**Operator time anchor:** `1794951315` — 2026-11-17 21:35:15 UTC / 22:35:15 CET  
**Parent architecture freeze:** `1794935960` — 2026-11-17 17:19:20 UTC / 18:19:20 CET  
**Review:** `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_REVIEW_0_1_0_DRAFT_1794951315_2026-11-17`  
**Canonical:** `false`  
**Implementation:** `OPEN / NOT IMPLEMENTED`

## 1. Purpose and authority

This contract candidate defines the responsibilities, ownership boundaries, reference directions, and external-standard support mapping for the seven registers already frozen by the parent architecture decision. It is intended to provide a stable architecture contract before individual register schemas are designed.

This is a **Freeze Candidate**, not a completed Freeze. It is non-canonical and is not implemented. It does not change the parent decision, Gateway v0.1.0, Gateway v0.2.0-draft, or the earlier architecture/support-profile drafts.

## 2. Frozen architecture scope

The following register set remains unchanged and in its frozen order:

| Order | Register |
| --- | --- |
| 1 | Directory |
| 2 | Object Identity |
| 3 | Artifact |
| 4 | DeepRead |
| 5 | Integrity |
| 6 | Provenance & Rights |
| 7 | Route |

The five external-standard target versions also remain unchanged: JSON Schema 2020-12; W3C PROV-O; PREMIS 3.0; RFC 8493 BagIt; RO-Crate 1.2. RO-Crate 1.3 remains outside the target set and requires a separate compatibility review.

## 3. Register responsibility contract

### Directory Register

**Responsibility:** Keep source-scoped, time-bounded observations of directory and namespace structure, including observed locators, parent/child entries, entry kind, observation scope, observation window, warnings and non-atomicity.

**Owns:** Directory observation records and their source/time context.; Observed path/locator and parent-child entry relationships.; Listing scope, counts, warnings, and atomicity limitations.

**Does not own:** Stable K501 object identity.; Artifact identity, version semantics, or canonical status.; Proof that a target was read, semantically validated, or is currently resolvable.

**Boundary:** A locator records where an entry was observed at a stated time and source scope. It is not an identity. An observation may reference an independently established Object Identity record, but cannot create that identity from a path.

### Object Identity Register

**Responsibility:** Maintain K501 identity records for exact source-object instances and evidence-backed identity assertions while retaining each issuing source system’s native identifiers and distinctions.

**Owns:** K501 object-identity records only under an explicitly approved identity rule.; Native source identifiers such as file_id and library_file_id together with their issuing source scope.; Evidence and status for supported identity, distinction, and unresolved-equivalence assertions.

**Does not own:** Directory membership as its source of record.; Artifact descriptions or artifact-version declarations.; Read-completion, digest verification, rights decisions, or inferred equivalence based only on name/path/size/hash.

**Boundary:** The candidate identity subject is a source-object instance/occurrence, not a path, filename, semantic work, or digest. Equivalence across copies or revisions requires its own explicit evidence and approved rule. Native IDs remain source-scoped; a K501 ID does not replace them.

### Artifact Register

**Responsibility:** Describe identifiable digital artifacts and declared versions, formats, schemas, status claims, companion relationships, and references to the K501 object instances represented or contained.

**Owns:** Artifact descriptors and artifact-version relationships.; Declared formats, media types, schema/version references, and source-scoped status claims.; Explicit links from artifact/version records to one or more object identities when evidenced.

**Does not own:** The underlying source-object identity record.; Read-completion or byte-integrity evidence.; Canonical admission inferred from title, package presence, schema validity, or a mapped external representation.

**Boundary:** Artifact identity/version and source-object identity are separate domains. One artifact version may refer to one or more object instances; a source object may participate in more than one artifact description. Cardinality is recorded, never guessed.

### DeepRead Register

**Responsibility:** Record source-bound read events and coverage evidence, separating requested scope from the exact extent actually read, parsed, or visually inspected.

**Owns:** Read-event records, method, time, and exact source scope.; Requested extent compared with completed extent.; Warnings, extraction limitations, unread ranges, deferrals, and coverage status.

**Does not own:** Original source content as a replacement copy.; Semantic truth or completeness beyond the recorded method and extent.; Byte-integrity verification or rights clearance.

**Boundary:** A DeepRead record references the exact source-object identity and/or artifact version when available. Metadata listing, search snippets, and partial reads remain distinct from full content reads. DeepRead PASS is limited to the declared extent.

### Integrity Register

**Responsibility:** Record byte-integrity observations and verification events for an explicitly identified byte sequence, object instance, artifact version, payload, or package scope.

**Owns:** Digest observations with algorithm and byte/scope definition.; Byte counts and verification results tied to the exact source object, artifact version, or package payload checked.; Integrity-event and verifier context.

**Does not own:** Semantic truth, source authority, or identity equivalence.; Claims about bytes outside the declared digest scope.; Package-wide or Library-wide completeness without complete enumeration and verification.

**Boundary:** An Integrity record references the exact source identity and/or artifact version plus the byte scope. A matching digest proves byte equality only within that scope; it does not prove identity, meaning, completeness, permission, or canonicality.

### Provenance and Rights Register

**Responsibility:** Record source-to-derived relationships, activities, responsible agents, attribution, declared rights/licensing information, restrictions, and separately evidenced rights-review outcomes.

**Owns:** Provenance relations and evidence linking source and derived object identities/artifacts.; Activity and responsible-agent references where supplied or evidenced.; Rights statements, license evidence, restrictions, rights-review state, and separately authorized redistribution decisions.

**Does not own:** K501 object-identity assignment.; Legal conclusions inferred from technical accessibility, package validity, metadata, or a license label alone.; DeepRead coverage, integrity verification, or adapter validation as their source of record.

**Boundary:** The frozen combined register contains two logically distinct record families: PROVENANCE records and RIGHTS records. They share a register boundary but must not collapse into one assertion. Rights scope, evidence, restrictions, jurisdiction/authority where known, and review outcome remain explicit; UNKNOWN/OPEN is preserved.

### Route Registry

**Responsibility:** Maintain explicit, versionable navigation and resolution routes to registered directories, objects, artifact versions, or declared operations, including unresolved, stale, and expired routes.

**Owns:** Route identifiers, route purpose, scope, and source/target declarations.; Target locators and target identity/artifact references when available.; Time-scoped route-resolution observations and unresolved/expired conditions.

**Does not own:** Target object identity or artifact content.; Content validation, authorization, access rights, or semantic correctness.; The assertion that every declared target currently exists or is accessible.

**Boundary:** A route is a navigation contract. Resolution is time- and source-scoped. A successful route resolution does not validate content or grant access/redistribution permission.

## 4. Complete register relationship matrix

**Normative direction:** a row register owns the record that may reference a record in the column register. `REF` is an explicit register-to-register reference; `SELF` is record ownership; `—` means no mandatory direct relation is defined.

| Record owner ↓ / referenced target → | Directory | Object Identity | Artifact | DeepRead | Integrity | Provenance & Rights | Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Directory | SELF | REF | — | — | — | — | — |
| Object Identity | — | SELF | — | — | — | — | — |
| Artifact | — | REF | SELF | — | — | — | — |
| DeepRead | — | REF | REF | SELF | — | — | — |
| Integrity | — | REF | REF | — | SELF | — | — |
| Provenance & Rights | — | REF | REF | REF | REF | SELF | — |
| Route | REF | REF | REF | — | — | — | SELF |

The 7×7 matrix contains 13 direct-reference relationships, 7 self-scope cells, and 29 cells with no direct architectural reference. The JSON companion preserves every cell and its exact reference condition.

### 4.1 Direct-reference conditions

| Record owner | Referenced register | Condition |
| --- | --- | --- |
| Directory | Object Identity | OPTIONAL_WHEN_IDENTITY_INDEPENDENTLY_ESTABLISHED |
| Artifact | Object Identity | REQUIRED_WHEN_ARTIFACT_VERSION_REPRESENTS_OR_CONTAINS_IDENTIFIED_OBJECT |
| DeepRead | Object Identity | REQUIRED_WHEN_SOURCE_OBJECT_IDENTITY_IS_AVAILABLE |
| DeepRead | Artifact | REQUIRED_WHEN_EXACT_ARTIFACT_VERSION_IS_IDENTIFIED |
| Integrity | Object Identity | REQUIRED_WHEN_SOURCE_OBJECT_IDENTITY_IS_AVAILABLE |
| Integrity | Artifact | REQUIRED_WHEN_EXACT_ARTIFACT_VERSION_OR_PACKAGE_IS_IDENTIFIED |
| Provenance & Rights | Object Identity | REQUIRED_FOR_SOURCE_OR_DERIVED_OBJECT_ASSERTIONS |
| Provenance & Rights | Artifact | REQUIRED_FOR_ARTIFACT_DERIVATION_OR_RIGHTS_SCOPE_ASSERTIONS |
| Provenance & Rights | DeepRead | OPTIONAL_WHEN_READ_OR_TRANSFORMATION_EVENT_IS_RELEVANT |
| Provenance & Rights | Integrity | OPTIONAL_WHEN_INTEGRITY_EVENT_SUPPORTS_PRESERVATION_OR_PROVENANCE_CLAIM |
| Route | Directory | OPTIONAL_WHEN_ROUTE_USES_OBSERVED_DIRECTORY_LOCATOR |
| Route | Object Identity | OPTIONAL_WHEN_TARGET_OBJECT_IDENTITY_IS_KNOWN |
| Route | Artifact | OPTIONAL_WHEN_TARGET_ARTIFACT_VERSION_IS_KNOWN |

No reference transfers authority. No direct relation is a deliberate boundary, not a prohibition against future evidenced relationships. Any new relationship requires a versioned architecture change and must not be inferred during schema implementation.

The corrected matrix adds three explicit relationships beyond reversing the three misdirected references in the prior draft: `DEEPREAD_REGISTER → OBJECT_IDENTITY_REGISTER`, `INTEGRITY_REGISTER → OBJECT_IDENTITY_REGISTER`, and optional `PROVENANCE_AND_RIGHTS_REGISTER → INTEGRITY_REGISTER`. Their conditions are encoded in the JSON matrix and the review artifact.

## 5. Cross-register invariants

1. K501 remains the native information model and retains its own object identities, source scopes, temporal references, and status definitions.
2. Every register is authoritative only for its own record/evidence domain; cross-register links are references, not silent transfers of authority.
3. Source object identity, artifact identity/version, path/locator, byte sequence, and route are distinct concepts and must not be substituted for one another.
4. Original source data and derived external representations remain separate.
5. All records preserve source identity, source scope, time reference, and provenance where available.
6. Unknown values remain UNKNOWN/OPEN; absence is not FALSE; missing or unresolved references are not silently repaired.
7. New observations and corrections are append-only; historical records and claims are never silently overwritten.
8. Validation is not proof of truth, semantic correctness, source completeness, rights, permission, or canonicality.
9. Integrity evidence is limited to exact bytes and the declared verification scope.
10. DeepRead evidence is limited to the exact method and extent recorded.
11. Information loss, unmapped fields, unsupported constructs, transformations, and omissions in external representations must be explicit and traceable.
12. Routes are navigation declarations only and do not imply target validity, identity, authorization, rights clearance, or semantic correctness.


## 6. Overlap and separation decisions

### 6.1 Object Identity versus Artifact

Object Identity identifies a source-object instance using native source identifiers and scoped evidence. Artifact describes a digital representation/version and explicitly references the object instance(s) it represents or contains. Paths and hashes do not establish identity or equivalence.

### 6.2 DeepRead versus Integrity

DeepRead proves only the recorded read method and extent. Integrity proves only a digest result for the exact byte scope. Neither operation implies the other. Both may independently reference the same object/artifact version.

### 6.3 Provenance versus Rights

The frozen `Provenance and Rights Register` remains one register, but it contains distinct logical record families. Provenance expresses source/derivation/activity/agent relationships. Rights expresses declared licenses, restrictions, evidence, reviewer/authority, scope, and review outcomes. Provenance is not permission, and a license string alone is not rights clearance.

### 6.4 Directory versus Route

Directory records observed structure at a time and source scope. Route Registry records a navigation declaration and its resolution state. A stale or unresolved route does not alter historical directory observations. Neither one creates target identity or permission.

### 6.5 Artifact versus external representations

External JSON-LD, PREMIS, BagIt, or PROV-O outputs are derived representations with their own artifact identities/versions. They do not replace the K501 source object or K501 artifact records. Unmapped, omitted, transformed, and lossy values remain traceable.

## 7. Standard-support profile binding

The five standard targets and their versions are frozen. This section binds their bounded intended uses to the register architecture. It does not assert implementation or conformance.

| Standard target | Primary register responsibility | Supporting references | Decision |
| --- | --- | --- | --- |
| JSON Schema 2020-12 | Directory, Object Identity, Artifact, DeepRead, Integrity, Provenance & Rights, Route | None | ACCEPT_WITH_BOUNDARY |
| W3C PROV-O W3C Recommendation | Provenance & Rights | Object Identity, Artifact, DeepRead | ACCEPT_WITH_MAPPING_CORRECTION |
| PREMIS Data Dictionary 3.0 | Artifact, Integrity, Provenance & Rights | Object Identity, DeepRead | ACCEPT_WITH_MAPPING_CORRECTION |
| The BagIt File Packaging Format RFC 8493 | Directory, Artifact, Integrity | Object Identity, Provenance & Rights | ACCEPT_WITH_MAPPING_CORRECTION |
| RO-Crate 1.2 | Artifact, Directory, Provenance & Rights | Object Identity | ACCEPT_WITH_MAPPING_CORRECTION |

### 7.1 JSON Schema 2020-12

Structural shape and permitted values for machine-readable records across all seven registers, Gateway documents, support profiles, and adapter documents. It does not prove referential integrity, existence of targets, identity authority, semantic truth, or completeness. Graph/reference validation remains a separate work unit.

### 7.2 W3C PROV-O

Use `Entity`, `Activity`, and `Agent` concepts for source/derived entities, read/transformation activities, and responsibility. Provenance and Rights is the primary owner; Object Identity, Artifact, and DeepRead supply references. PROV-O does not replace K501 identity or rights decisions.

### 7.3 PREMIS 3.0

Use its Object, Event, Rights, and Agent entities for bounded preservation metadata. Artifact, Integrity, and Provenance and Rights are primary; Object Identity provides the explicit K501 identity reference; DeepRead contributes only where a read operation is deliberately represented as a preservation event. No one-to-one mapping is assumed.

### 7.4 RFC 8493 BagIt

Use BagIt for package-level payload/tag organization and scoped fixity. Directory supplies observed path/hierarchy inputs, Artifact describes the package, and Integrity records exact payload/tag verification. Provenance/Rights may supply optional contextual metadata but does not become a BagIt rights model. BagIt completeness/validity is limited to the exact bag and manifest scope.

### 7.5 RO-Crate 1.2

Use JSON-LD Root Data Entity, Data Entities, and Contextual Entities to describe selected research-object packages. Artifact and Directory provide package/file descriptions; Provenance and Rights supplies contextual provenance/rights metadata; Object Identity references may be retained as K501 identifiers. RO-Crate URLs are not K501 Route Registry records. RO-Crate does not require every file to be described and is not a substitute for complete Library identity or DeepRead coverage.

### 7.6 Version boundary

`RO_CRATE_1_2 = FROZEN_TARGET`  
`RO_CRATE_1_3 = OPEN / SEPARATE_COMPATIBILITY_REVIEW_REQUIRED`

## 8. Internal support-level contract

The support progression is evaluated per exact standard version, adapter version, operation direction, source/output identity, and declared test scope:

`REGISTERED → PARSED → VALIDATED → MAPPED → (EXPORTED | IMPORTED)`

`ROUNDTRIP_VERIFIED` is a separate achieved result requiring both export and import directions plus an exact fixture and invariant comparison.

| Level | Meaning | Minimum evidence |
| --- | --- | --- |
| REGISTERED | The exact standard/version and bounded K501 integration purpose are recorded in an accepted, versioned support profile. | Exact standard identifier and version.; Bounded purpose and scope.; Authoritative specification reference. |
| PARSED | A concrete input document/package is read by an identified parser within the pinned version and scope. | Exact input identity and byte/scope reference.; Parser name and version.; Parse result, warnings, and unsupported constructs. |
| VALIDATED | The parsed input passes the declared syntax/schema/profile checks for the pinned version and profile. | Validation profile and version.; Validator identity/version.; Validation report, scope, warnings, and result. |
| MAPPED | A versioned K501-to-standard or standard-to-K501 mapping is defined and applied to a declared scope. | Mapping/crosswalk identifier and version.; Field/relationship coverage.; Explicit unmapped, unsupported, defaulted, transformed, and lossy elements. |
| EXPORTED / IMPORTED | A concrete export or import is performed through a declared adapter boundary. The direction is recorded explicitly; both outcomes may exist for a bidirectional adapter. | Direction=EXPORTED or IMPORTED.; Exact source/input and output/result identities.; Adapter/version, time, transformation evidence, and losses. |
| ROUNDTRIP_VERIFIED | A bidirectional export/import cycle passes declared tests for the exact fixture, fields, and invariants. | Input/export/import identities and adapter versions.; Fixture, expected invariant set, and comparison method.; Observed results, losses, warnings, and report. |

No support level is inferred from a filename, target selection, successful parsing alone, or a general claim about a standard. A one-way exchange cannot be called `ROUNDTRIP_VERIFIED`. All level claims are scoped; no universal conformance is implied.

## 9. Schema design order

| Order | Register | Design dependency |
| --- | --- | --- |
| 1 | Object Identity | Define source-object identity, source scope, and explicit equivalence rules first. |
| 2 | Directory | Can be designed independently but must cross-reference Object Identity without deriving identity from paths; review alongside order 1. |
| 3 | Artifact | Depends on stable identity references and exact artifact/version distinction. |
| 4 | DeepRead | References source identity and artifact version; remains separate from Integrity. |
| 5 | Integrity | References source identity/artifact version and exact byte scope; independent of DeepRead. |
| 6 | Provenance & Rights | Depends on object, artifact, read, and integrity references; retains separate provenance and rights record families. |
| 7 | Route | Depends on registered directory/object/artifact targets and temporal resolution semantics. |

Object Identity and Directory should be reviewed as a pair. DeepRead and Integrity remain separate evidence domains and may be designed in parallel once identity/artifact references are stable. The graph validator, crosswalks, and adapters remain separate work units after the relevant schemas are individually defined and accepted.

## 10. Open prerequisites

- **OPEN-01 — Object Identity issuance/equivalence procedure (OPEN_SCHEMA_PREREQUISITE):** Define deterministic assignment, source scope, duplicate/copy claims, revision relationship, and evidence required for equivalence before Object Identity schema design.
- **OPEN-02 — Artifact version and source-object relationship cardinality (OPEN_SCHEMA_PREREQUISITE):** Define version identity, immutable revision references, and relationship multiplicity in Artifact Register design; do not infer cardinality.
- **OPEN-03 — Append-only correction and supersession representation (OPEN_SCHEMA_PREREQUISITE):** Define how correction, withdrawal, supersession, and status changes are appended without rewriting prior evidence.
- **OPEN-04 — Directory freshness and route temporal resolution (OPEN_SCHEMA_PREREQUISITE):** Define observation validity window, stale route handling, unresolved/expired states, and source-interface time semantics.
- **OPEN-05 — Rights evidence and decision authority (OPEN_SCHEMA_PREREQUISITE):** Define evidence scope, applicable rights/permission statement, reviewer authority, decision time, restrictions, and UNKNOWN/OPEN states. No default legal conclusion.
- **OPEN-06 — DeepRead coverage vocabulary (OPEN_SCHEMA_PREREQUISITE):** Define requested vs completed extents, extraction methods, coverage states, and how partial/failed reads are represented without false completion.
- **OPEN-07 — Integrity algorithm and verification event semantics (OPEN_SCHEMA_PREREQUISITE):** Define supported algorithms, byte scope, canonical byte acquisition, verifier provenance, and result state per exact verification event.
- **OPEN-08 — External mapping loss taxonomy (OPEN_SUPPORT_PROFILE_PREREQUISITE):** Define explicit values for unmapped, unsupported, omitted, normalized, defaulted, and lossy fields before any crosswalk or adapter is accepted.
- **OPEN-09 — RO-Crate 1.3 compatibility (OPEN_SEPARATE_REVIEW):** No support or compatibility is inferred from the frozen RO-Crate 1.2 target.

These open items are intentionally not silently completed by this contract. They are inputs to the relevant schema or support-profile design and validation work.

## 11. Acceptance criteria for a later Freeze

1. Operator explicitly accepts this exact contract revision and its 7x7 directed relationship matrix.
2. The frozen register names/order and five standard versions remain unchanged.
3. All required corrections to relationship direction and standard mapping are included in this candidate.
4. Identity, artifact, read, integrity, provenance/rights, and route boundaries are accepted as written.
5. Open schema prerequisites remain explicitly recorded and are not converted to implementation claims.
6. The Markdown and JSON companions pass structural cross-check, exact-byte readback, and SHA-256 verification.


## 12. Current disposition

`REGISTER_SET = FROZEN_UNCHANGED`  
`STANDARD_TARGET_SET = FROZEN_UNCHANGED`  
`ROLE_ASSIGNMENTS = ACCEPTED_IN_CANDIDATE_WITH_CLARIFICATIONS`  
`RELATIONSHIP_MATRIX = CORRECTED_7X7_CONTRACT`  
`STANDARD_MAPPING = CORRECTED_IN_CANDIDATE`  
`CONTRACT = FREEZE_CANDIDATE_NOT_FROZEN`  
`REGISTER_SCHEMAS = OPEN_NOT_STARTED`  
`GRAPH_VALIDATOR = OPEN_NOT_STARTED`  
`PROV_O_PREMIS_CROSSWALKS = OPEN_NOT_STARTED`  
`BAGIT_RO_CRATE_ADAPTERS = OPEN_NOT_STARTED`  
`FULL_LIBRARY_DEEPREAD = OPEN`  
`IMPLEMENTATION = OPEN_NOT_IMPLEMENTED`  
`CANONICALIZATION = NOT_AUTHORIZED`

No existing Gateway file or prior draft is modified. No implementation, gate transition, or canonicalization is claimed.

## 13. Source basis and external references

- `GATEWAY.md` — `/K501_GATEWAY/GATEWAY.md`; `file_id=file_0000000005b081f4ab0aae42da29d211`; `library_file_id=libfile_eadbf46aaf0881919b6ddb02019d38d8`. Scope: Original human gateway; authority is navigation only; identity/source/time/route constraints.
- `GATEWAY.json` — `/K501_GATEWAY/GATEWAY.json`; `file_id=file_00000000ee50824683be7efeb68d9b80`; `library_file_id=libfile_63e66320cf18819193bd9c37d778fec8`. Scope: Original machine gateway; route semantics, resolution rules, and source boundaries.
- `Index.json` — `/K501_GATEWAY/Index.json`; `file_id=file_0000000006c88243b19890d6e02b463f`; `library_file_id=libfile_c801ceaea90481918a146a095a3e48cc`. Scope: Historical top-level navigation index; incomplete file/content coverage is explicit.
- `GATEWAY_v0.2.0-draft_1794932044_2026-11-17.md` — `/K501_GATEWAY/GATEWAY_v0.2.0-draft_1794932044_2026-11-17.md`; `file_id=file_000000003bb08243895188cc5db49d55`; `library_file_id=libfile_850d69b96ca881918d6d13418bb63868`. Scope: Additive navigation draft; source identity, exact scope, current directory snapshot, and no-mutation boundaries.
- `GATEWAY_v0.2.0-draft_1794932044_2026-11-17.json` — `/K501_GATEWAY/GATEWAY_v0.2.0-draft_1794932044_2026-11-17.json`; `file_id=file_00000000ecd881f49870397837142c65`; `library_file_id=libfile_8546aa48eea0819197ddda5463f9a84c`. Scope: Machine route contract and explicit identity/resolution rules.
- `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_v0.1.0-draft_1794950678_2026-11-17.md` — `/K501_SPECIFICATION/K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_v0.1.0-draft_1794950678_2026-11-17.md`; `file_id=file_00000000b28881f4aa92c7852f83c6f0`; `library_file_id=libfile_a9fb668061c88191a1a1110ebad4a79b`. Scope: Role assignments and existing ten directional relationships reviewed; preserved unchanged.
- `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_v0.1.0-draft_1794950678_2026-11-17.json` — `/K501_SPECIFICATION/K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_v0.1.0-draft_1794950678_2026-11-17.json`; `file_id=file_00000000f7bc81f4811278fab5d61b32`; `library_file_id=libfile_a72c134f4660819190a2445a28659604`. Scope: Structured roles, relationship matrix, and source boundaries reviewed; preserved unchanged.
- `K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_v0.1.0-draft_1794950678_2026-11-17.md` — `/K501_SPECIFICATION/K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_v0.1.0-draft_1794950678_2026-11-17.md`; `file_id=file_000000009240820a8fa285e11ed90df4`; `library_file_id=libfile_b6c21d5429b881918055637122a8ea68`. Scope: Five frozen support targets and internal support-level model reviewed; preserved unchanged.
- `K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_v0.1.0-draft_1794950678_2026-11-17.json` — `/K501_SPECIFICATION/K501_LIBRARY_GATEWAY_STANDARD_SUPPORT_PROFILE_v0.1.0-draft_1794950678_2026-11-17.json`; `file_id=file_000000006c1c821097ba6241e2773e1c`; `library_file_id=libfile_f5e32e69d0fc819186d090edfb10e5a8`. Scope: Five target versions and related-register lists reviewed; preserved unchanged.
- `K501_LIBRARY_GATEWAY_REVIEW_VALIDATION_REPORT_1794932044_2026-11-17.md` — `/K501_LIBRARY/K501_LIBRARY_GATEWAY_REVIEW_VALIDATION_REPORT_1794932044_2026-11-17.md`; `file_id=file_00000000f4bc820a9f19157bd6f1f0ce`; `library_file_id=libfile_95d9f470db848191bd32cde6c260dd33`. Scope: Historical evidence for targeted DeepRead, open boundaries, comparative external-standards research, and prior layered-register proposal.

External specification references: JSON Schema 2020-12 https://json-schema.org/specification ; W3C PROV-O https://www.w3.org/TR/prov-o/ ; PREMIS 3.0 https://www.loc.gov/standards/premis/v3/ ; RFC 8493 https://www.rfc-editor.org/rfc/rfc8493.html ; RO-Crate 1.2 https://www.researchobject.org/ro-crate/specification/1.2/ .

**Design rules:** `RECONSTRUCT_BEFORE_EXTEND` · `PROOF_BEFORE_STATE` · `OBSERVE_BEFORE_MUTATE` · `APPEND_ONLY` · `NO_DRIFT` · `NO_INTERPRETATION` · `NO_PHANTOM` · `UNKNOWN_BY_DEFAULT` · `TRACEABILITY_REQUIRED` · `TEMPORAL_CONSISTENCY` · `DERIVED_IS_NOT_CANONICAL` · `DENSIFICATION_WITHOUT_ERASURE` · `OPEN_UNTIL_PASS`