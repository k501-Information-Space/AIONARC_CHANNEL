# K501 Library Gateway Register Architecture Review — 0.1.0-draft

**Artifact ID:** `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_REVIEW_0_1_0_DRAFT_1794951315_2026-11-17`  
**Schema ID:** `K501_LIBRARY_GATEWAY_REGISTER_ARCHITECTURE_REVIEW/0.1.0-draft`  
**Status:** `REVIEW_COMPLETED_WITH_REQUIRED_CORRECTIONS_FREEZE_CANDIDATE_CREATED`  
**Operator time anchor:** `1794951315` — 2026-11-17 21:35:15 UTC / 22:35:15 CET  
**Parent architecture freeze:** `1794935960` — 2026-11-17 17:19:20 UTC / 18:19:20 CET  
**Canonical:** `false`

## 1. Executive disposition

**Review result:** `PASS_WITH_REQUIRED_CORRECTIONS_AND_SCHEMA_PREREQUISITES`  
**Architecture contract:** `FREEZE_CANDIDATE_NOT_FROZEN`

The seven register names, count, and order are accepted unchanged under the parent freeze. All seven role assignments are accepted with the clarifications recorded below. The previous relationship list contains three direction errors: its descriptions say that DeepRead and Integrity records point to artifacts, while the table points the other way. The complete matrix in this review uses one explicit convention: **the row is the record-owning register; the column is the register whose record may be referenced**.

The five frozen standard targets are retained unchanged. Four mapping clarifications are required: Object Identity must be explicit in PROV-O and PREMIS mappings; Directory must be a source for BagIt and RO-Crate package structure; and RO-Crate URLs must not be treated as K501 Route Registry semantics. No schema, validator, crosswalk, or adapter is implemented by this review.

## 2. Source reconstruction and review scope

Reviewed inputs include the original `/K501_GATEWAY/GATEWAY.md`, `GATEWAY.json`, and `Index.json`; Gateway `v0.2.0-draft`; the register architecture draft and standard-support profile created at anchor `1794950678`; and the prior Gateway validation/readback report at anchor `1794932044`.

The original Gateway establishes navigation and authority boundaries, not source truth or completeness. The v0.2.0 draft preserves the distinctions between path, `file_id`, `library_file_id`, artifact ID, revision, time, and source scope. Its metadata observations and historical indexes are not full content coverage. This review does not reinterpret those records as a completed Library DeepRead.

The reviewed drafts and original Gateway files remain unchanged. This review is a new derived decision artifact.

## 3. Seven-register responsibility review

| Register | Decision | Review and clarification |
| --- | --- | --- |
| Directory | ACCEPT_WITH_CLARIFICATION | Responsibility is distinct from identity. Retain source, time window, listing scope, warnings, and non-atomicity as first-class observation context. |
| Object Identity | ACCEPT_WITH_CLARIFICATION | Use exact source-object instance as the candidate subject. Keep native source IDs and K501 IDs distinct. No hash/path/name-based identity collapse. Detailed issuance and equivalence rules must be pinned before this register schema is designed. |
| Artifact | ACCEPT_WITH_CLARIFICATION | Artifact and artifact-version description is distinct from source-object identity. Explicitly reference exact object identities; never infer cardinality. |
| DeepRead | ACCEPT_WITH_CLARIFICATION | Separate requested and completed extent, read method, content/page/range coverage, warnings, and unread/deferral state. Never infer complete content coverage from metadata or snippets. |
| Integrity | ACCEPT_WITH_CLARIFICATION | Every digest must be bound to exact bytes, algorithm, input identity, and scope. Integrity remains independent of DeepRead and semantics. |
| Provenance & Rights | ACCEPT_WITH_INTERNAL_DOMAIN_SEPARATION | Retain one frozen register name but separate provenance records from rights records. Rights assertions require evidence and scope; technical access and provenance are not rights clearance. |
| Route | ACCEPT_WITH_CLARIFICATION | Routes are versioned navigation declarations with time-scoped resolution observations. A route never creates identity, validates content, or authorizes access. |

### Consolidated responsibility contract

### Directory Register

**Responsibility:** Keep source-scoped, time-bounded observations of directory and namespace structure, including observed locators, parent/child entries, entry kind, observation scope, observation window, warnings and non-atomicity.

**Owns:** Directory observation records and their source/time context.; Observed path/locator and parent-child entry relationships.; Listing scope, counts, warnings, and atomicity limitations.

**Does not own:** Stable K501 object identity.; Artifact identity, version semantics, or canonical status.; Proof that a target was read, semantically validated, or is currently resolvable.

**Clarification:** A locator records where an entry was observed at a stated time and source scope. It is not an identity. An observation may reference an independently established Object Identity record, but cannot create that identity from a path.

### Object Identity Register

**Responsibility:** Maintain K501 identity records for exact source-object instances and evidence-backed identity assertions while retaining each issuing source system’s native identifiers and distinctions.

**Owns:** K501 object-identity records only under an explicitly approved identity rule.; Native source identifiers such as file_id and library_file_id together with their issuing source scope.; Evidence and status for supported identity, distinction, and unresolved-equivalence assertions.

**Does not own:** Directory membership as its source of record.; Artifact descriptions or artifact-version declarations.; Read-completion, digest verification, rights decisions, or inferred equivalence based only on name/path/size/hash.

**Clarification:** The candidate identity subject is a source-object instance/occurrence, not a path, filename, semantic work, or digest. Equivalence across copies or revisions requires its own explicit evidence and approved rule. Native IDs remain source-scoped; a K501 ID does not replace them.

### Artifact Register

**Responsibility:** Describe identifiable digital artifacts and declared versions, formats, schemas, status claims, companion relationships, and references to the K501 object instances represented or contained.

**Owns:** Artifact descriptors and artifact-version relationships.; Declared formats, media types, schema/version references, and source-scoped status claims.; Explicit links from artifact/version records to one or more object identities when evidenced.

**Does not own:** The underlying source-object identity record.; Read-completion or byte-integrity evidence.; Canonical admission inferred from title, package presence, schema validity, or a mapped external representation.

**Clarification:** Artifact identity/version and source-object identity are separate domains. One artifact version may refer to one or more object instances; a source object may participate in more than one artifact description. Cardinality is recorded, never guessed.

### DeepRead Register

**Responsibility:** Record source-bound read events and coverage evidence, separating requested scope from the exact extent actually read, parsed, or visually inspected.

**Owns:** Read-event records, method, time, and exact source scope.; Requested extent compared with completed extent.; Warnings, extraction limitations, unread ranges, deferrals, and coverage status.

**Does not own:** Original source content as a replacement copy.; Semantic truth or completeness beyond the recorded method and extent.; Byte-integrity verification or rights clearance.

**Clarification:** A DeepRead record references the exact source-object identity and/or artifact version when available. Metadata listing, search snippets, and partial reads remain distinct from full content reads. DeepRead PASS is limited to the declared extent.

### Integrity Register

**Responsibility:** Record byte-integrity observations and verification events for an explicitly identified byte sequence, object instance, artifact version, payload, or package scope.

**Owns:** Digest observations with algorithm and byte/scope definition.; Byte counts and verification results tied to the exact source object, artifact version, or package payload checked.; Integrity-event and verifier context.

**Does not own:** Semantic truth, source authority, or identity equivalence.; Claims about bytes outside the declared digest scope.; Package-wide or Library-wide completeness without complete enumeration and verification.

**Clarification:** An Integrity record references the exact source identity and/or artifact version plus the byte scope. A matching digest proves byte equality only within that scope; it does not prove identity, meaning, completeness, permission, or canonicality.

### Provenance and Rights Register

**Responsibility:** Record source-to-derived relationships, activities, responsible agents, attribution, declared rights/licensing information, restrictions, and separately evidenced rights-review outcomes.

**Owns:** Provenance relations and evidence linking source and derived object identities/artifacts.; Activity and responsible-agent references where supplied or evidenced.; Rights statements, license evidence, restrictions, rights-review state, and separately authorized redistribution decisions.

**Does not own:** K501 object-identity assignment.; Legal conclusions inferred from technical accessibility, package validity, metadata, or a license label alone.; DeepRead coverage, integrity verification, or adapter validation as their source of record.

**Clarification:** The frozen combined register contains two logically distinct record families: PROVENANCE records and RIGHTS records. They share a register boundary but must not collapse into one assertion. Rights scope, evidence, restrictions, jurisdiction/authority where known, and review outcome remain explicit; UNKNOWN/OPEN is preserved.

### Route Registry

**Responsibility:** Maintain explicit, versionable navigation and resolution routes to registered directories, objects, artifact versions, or declared operations, including unresolved, stale, and expired routes.

**Owns:** Route identifiers, route purpose, scope, and source/target declarations.; Target locators and target identity/artifact references when available.; Time-scoped route-resolution observations and unresolved/expired conditions.

**Does not own:** Target object identity or artifact content.; Content validation, authorization, access rights, or semantic correctness.; The assertion that every declared target currently exists or is accessible.

**Clarification:** A route is a navigation contract. Resolution is time- and source-scoped. A successful route resolution does not validate content or grant access/redistribution permission.

## 4. Complete register relationship matrix

**Matrix rule:** `REF` means records owned by the row register may contain an explicit reference to a record in the column register. `SELF` means a register owns its own records. `—` means no mandatory direct architectural reference is defined. It does not prohibit a future evidence-backed relation; such a relation would require explicit, versioned design.

| Record owner ↓ / referenced target → | Directory | Object Identity | Artifact | DeepRead | Integrity | Provenance & Rights | Route |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Directory | SELF | REF | — | — | — | — | — |
| Object Identity | — | SELF | — | — | — | — | — |
| Artifact | — | REF | SELF | — | — | — | — |
| DeepRead | — | REF | REF | SELF | — | — | — |
| Integrity | — | REF | REF | — | SELF | — | — |
| Provenance & Rights | — | REF | REF | REF | REF | SELF | — |
| Route | REF | REF | REF | — | — | — | SELF |

There are 49 directed cells: 7 self-scope cells, 13 direct-reference cells, and 29 no-direct-reference cells.

### 4.1 Direct reference definitions

| Record owner | Referenced register | Requirement |
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

### 4.2 Corrected direction errors in the prior architecture draft

| Prior direction | Finding | Corrected direction |
| --- | --- | --- |
| OBJECT_IDENTITY_REGISTER -> ARTIFACT_REGISTER | Direction conflicts with the accompanying statement that Artifact records reference Object Identity. | ARTIFACT_REGISTER -> OBJECT_IDENTITY_REGISTER |
| ARTIFACT_REGISTER -> DEEPREAD_REGISTER | DeepRead event is the record that references the artifact/source revision it reads. | DEEPREAD_REGISTER -> ARTIFACT_REGISTER |
| ARTIFACT_REGISTER -> INTEGRITY_REGISTER | Integrity event is the record that references the exact artifact bytes/package payload it checks. | INTEGRITY_REGISTER -> ARTIFACT_REGISTER |

The prior draft remains preserved as historical input. The corrected directions apply to this review and the Freeze Candidate only; the old artifact is not overwritten.

### 4.3 Additional explicit references

| Relationship | Decision | Reason |
| --- | --- | --- |
| DEEPREAD_REGISTER -> OBJECT_IDENTITY_REGISTER | ADDED | A read event must bind its coverage claim to the exact source-object instance when the native identity is available. |
| INTEGRITY_REGISTER -> OBJECT_IDENTITY_REGISTER | ADDED | A digest/verification event must bind its byte-scope claim to the exact source-object instance when the native identity is available. |
| PROVENANCE_AND_RIGHTS_REGISTER -> INTEGRITY_REGISTER | ADDED_OPTIONAL | A provenance/preservation statement may cite an integrity event as supporting evidence; the Integrity Register remains the source of record for that event. |

These additions make the source-object identity of read and integrity evidence explicit and permit provenance to cite an integrity event where that event supports a preservation/derivation claim.

## 5. Overlap, boundary, and open-question review

| ID | Topic | State | Decision / open requirement |
| --- | --- | --- | --- |
| OVL-01 | Directory locator vs object identity | RESOLVED_BY_CONTRACT_BOUNDARY | Directory stores observed location/time; Object Identity stores source-object identity. Directory may reference identity only when independently established. |
| OVL-02 | Object identity vs artifact/artifact version | RESOLVED_AT_ARCHITECTURE_LEVEL; SCHEMA_DETAIL_OPEN | Object Identity identifies a source-object instance. Artifact Register describes a representation/version and references source-object identities. One-to-many is allowed only when evidenced. |
| OVL-03 | Artifact vs DeepRead coverage | RESOLVED_BY_OWNERSHIP | Artifact owns description/version; DeepRead owns read event and exact coverage. DeepRead references Artifact and Object Identity; Artifact does not own read status. |
| OVL-04 | Artifact vs Integrity | RESOLVED_BY_OWNERSHIP | Artifact owns description/version; Integrity owns byte/digest evidence. Integrity references Artifact and Object Identity; no reciprocal ownership. |
| OVL-05 | DeepRead vs Integrity | RESOLVED_AS_INDEPENDENT_EVIDENCE_DOMAINS | Reading content and verifying bytes are independent operations. Neither implies the other; both may reference the same source/artifact version. |
| OVL-06 | Provenance vs DeepRead/Integrity events | RESOLVED_BY_REFERENCE_ONLY | Provenance may reference DeepRead/Integrity events when they support a derivation or preservation claim; those event records remain owned by their respective registers. |
| OVL-07 | Provenance vs Rights within one frozen register | RESOLVED_BY_LOGICAL_RECORD_FAMILIES | Keep one register, but distinguish PROVENANCE records from RIGHTS records. No legal permission is inferred from origin, technical access, or a license string alone. |
| OVL-08 | Route locator vs target identity/artifact | RESOLVED_BY_REFERENCE_ONLY | Route stores locator and route resolution; target identity and artifact version are references only. Route resolution does not imply validity or permission. |
| OPEN-01 | Object Identity issuance/equivalence procedure | OPEN_SCHEMA_PREREQUISITE | Define deterministic assignment, source scope, duplicate/copy claims, revision relationship, and evidence required for equivalence before Object Identity schema design. |
| OPEN-02 | Artifact version and source-object relationship cardinality | OPEN_SCHEMA_PREREQUISITE | Define version identity, immutable revision references, and relationship multiplicity in Artifact Register design; do not infer cardinality. |
| OPEN-03 | Append-only correction and supersession representation | OPEN_SCHEMA_PREREQUISITE | Define how correction, withdrawal, supersession, and status changes are appended without rewriting prior evidence. |
| OPEN-04 | Directory freshness and route temporal resolution | OPEN_SCHEMA_PREREQUISITE | Define observation validity window, stale route handling, unresolved/expired states, and source-interface time semantics. |
| OPEN-05 | Rights evidence and decision authority | OPEN_SCHEMA_PREREQUISITE | Define evidence scope, applicable rights/permission statement, reviewer authority, decision time, restrictions, and UNKNOWN/OPEN states. No default legal conclusion. |
| OPEN-06 | DeepRead coverage vocabulary | OPEN_SCHEMA_PREREQUISITE | Define requested vs completed extents, extraction methods, coverage states, and how partial/failed reads are represented without false completion. |
| OPEN-07 | Integrity algorithm and verification event semantics | OPEN_SCHEMA_PREREQUISITE | Define supported algorithms, byte scope, canonical byte acquisition, verifier provenance, and result state per exact verification event. |
| OPEN-08 | External mapping loss taxonomy | OPEN_SUPPORT_PROFILE_PREREQUISITE | Define explicit values for unmapped, unsupported, omitted, normalized, defaulted, and lossy fields before any crosswalk or adapter is accepted. |
| OPEN-09 | RO-Crate 1.3 compatibility | OPEN_SEPARATE_REVIEW | No support or compatibility is inferred from the frozen RO-Crate 1.2 target. |

The key overlaps are resolved as follows:

- Directory observations do not create Object Identity.
- Artifact identity/version is not a replacement for source-object identity.
- DeepRead and Integrity are independent evidence domains; neither implies the other.
- Provenance may reference read and integrity events but does not own those events.
- Provenance and Rights remain one frozen register with two logically separate record families.
- Route resolution is not content validation or authorization.

The OPEN items are schema prerequisites, not implementation results. They must be resolved within the relevant schema/support work item before that item is frozen.

## 6. Five standard targets — mapping review

The five target versions are retained unchanged. The review below checks what each standard is suitable to represent and what must remain K501-native.

| Frozen target | Primary register relation | Supporting relation | Decision |
| --- | --- | --- | --- |
| JSON Schema 2020-12 | Directory, Object Identity, Artifact, DeepRead, Integrity, Provenance & Rights, Route | None | ACCEPT_WITH_BOUNDARY |
| W3C PROV-O W3C Recommendation | Provenance & Rights | Object Identity, Artifact, DeepRead | ACCEPT_WITH_MAPPING_CORRECTION |
| PREMIS Data Dictionary 3.0 | Artifact, Integrity, Provenance & Rights | Object Identity, DeepRead | ACCEPT_WITH_MAPPING_CORRECTION |
| The BagIt File Packaging Format RFC 8493 | Directory, Artifact, Integrity | Object Identity, Provenance & Rights | ACCEPT_WITH_MAPPING_CORRECTION |
| RO-Crate 1.2 | Artifact, Directory, Provenance & Rights | Object Identity | ACCEPT_WITH_MAPPING_CORRECTION |

### 6.1 Required profile mapping clarifications

| Standard | Correction / boundary |
| --- | --- |
| JSON Schema | JSON Schema does not establish that referenced IDs exist or that cross-register graph relationships are valid. Referential/graph checking remains a separate validator work unit. |
| W3C PROV-O | Add Object Identity Register to the related-register mapping. Keep rights decisions outside PROV-O semantics; provenance vocabulary is not a rights-clearance authority. DeepRead coverage detail remains owned by DeepRead Register. |
| PREMIS Data Dictionary | Add Object Identity Register as the K501 identity reference for PREMIS Objects. The relation is not assumed to be one-to-one. DeepRead events map only when they qualify as declared preservation events; not every read is automatically a PREMIS event. |
| The BagIt File Packaging Format | Add Directory Register to the related-register mapping. Provenance/Rights may supply optional bag metadata, but BagIt is not a provenance ontology or rights-clearance mechanism. Any K501 object identifier carried as metadata remains a K501 value, not a BagIt identity. |
| RO-Crate | Add Directory Register as a source of package/file-structure observations. Remove Route Registry from direct mapped registers: RO-Crate file URLs/identifiers are not equivalent to K501 route declarations or route-resolution evidence. Preserve Object Identity only as K501 identifier references, not as a replaced RO-Crate identity. |

**External specification checks:**

- JSON Schema 2020-12 separates Core and Validation; it checks a declared structure and values, not the truth or referential integrity of the information. Reference: https://json-schema.org/specification
- PROV-O models `Entity`, `Activity`, and `Agent`, with relations for use, generation, derivation, and responsibility. The K501 identity and artifact records remain the source references. Reference: https://www.w3.org/TR/prov-o/
- PREMIS 3.0 defines four entities: `Objects`, `Events`, `Rights`, and `Agents`. The K501 crosswalk must explicitly keep PREMIS Object mapping distinct from K501 object and artifact identity. Reference: https://www.loc.gov/standards/premis/v3/
- RFC 8493 requires a payload manifest to list every payload file exactly once; a valid bag requires the bag to be complete and checksums to verify. These claims concern that bag, not the full K501 Library. Reference: https://www.rfc-editor.org/rfc/rfc8493.html
- RO-Crate 1.2 uses JSON-LD with a Root Data Entity and related Data/Contextual Entities. Its metadata is not an exhaustive file manifest; not every file must be represented as a Data Entity. Therefore it cannot replace the K501 Directory, Object Identity, or DeepRead evidence domains. Reference: https://www.researchobject.org/ro-crate/specification/1.2/ and https://www.researchobject.org/ro-crate/specification/1.2/root-data-entity

RO-Crate 1.3 remains `OPEN / SEPARATE COMPATIBILITY REVIEW REQUIRED`.

## 7. Internal support-level model review

**Decision:** `ACCEPT_WITH_SCOPE_AND_DIRECTION_CLARIFICATION`.

Support is assessed per exact standard version, adapter version, operation direction, input/output identities, and tested fixture/scope. There is no global support PASS for a whole standard or for K501.

| Level | Meaning | Minimum evidence |
| --- | --- | --- |
| REGISTERED | The exact standard/version and bounded K501 integration purpose are recorded in an accepted, versioned support profile. | Exact standard identifier and version.; Bounded purpose and scope.; Authoritative specification reference. |
| PARSED | A concrete input document/package is read by an identified parser within the pinned version and scope. | Exact input identity and byte/scope reference.; Parser name and version.; Parse result, warnings, and unsupported constructs. |
| VALIDATED | The parsed input passes the declared syntax/schema/profile checks for the pinned version and profile. | Validation profile and version.; Validator identity/version.; Validation report, scope, warnings, and result. |
| MAPPED | A versioned K501-to-standard or standard-to-K501 mapping is defined and applied to a declared scope. | Mapping/crosswalk identifier and version.; Field/relationship coverage.; Explicit unmapped, unsupported, defaulted, transformed, and lossy elements. |
| EXPORTED / IMPORTED | A concrete export or import is performed through a declared adapter boundary. The direction is recorded explicitly; both outcomes may exist for a bidirectional adapter. | Direction=EXPORTED or IMPORTED.; Exact source/input and output/result identities.; Adapter/version, time, transformation evidence, and losses. |
| ROUNDTRIP_VERIFIED | A bidirectional export/import cycle passes declared tests for the exact fixture, fields, and invariants. | Input/export/import identities and adapter versions.; Fixture, expected invariant set, and comparison method.; Observed results, losses, warnings, and report. |

Operational flow: `REGISTERED → PARSED → VALIDATED → MAPPED → (EXPORTED / IMPORTED)`. `ROUNDTRIP_VERIFIED` requires both directions and a scoped comparison. `EXPORTED` and `IMPORTED` are distinct outcomes. No achieved implementation level is asserted by this review.

## 8. Explicit review decisions

| Decision | Subject | Disposition | Reason |
| --- | --- | --- | --- |
| DEC-01 | Seven register names/count/order | ACCEPT_FROZEN_UNCHANGED | Parent freeze anchor 1794935960 controls the register set. |
| DEC-02 | Seven register responsibilities | ACCEPT_WITH_CLARIFICATIONS | All seven responsibilities are coherent once identity/artifact, read/integrity, provenance/rights, and route/authorization boundaries are explicit. |
| DEC-03 | Register relationship matrix | CHANGE_REQUIRED; CORRECTED_MATRIX_ACCEPTED_FOR_FREEZE_CANDIDATE | Three directions in the prior relationship list were inconsistent with the stated reference ownership. New matrix uses row=record owner, column=referenced register. |
| DEC-04 | Five standard target versions | ACCEPT_FROZEN_UNCHANGED | No version or target-set change is made. |
| DEC-05 | Standard-to-register mapping detail | ACCEPT_WITH_MAPPING_CORRECTIONS | PROV-O and PREMIS need explicit Object Identity references; BagIt and RO-Crate need Directory as a source for package structure; RO-Crate must not be treated as a native Route Registry mapping. |
| DEC-06 | Support-level progression | ACCEPT_WITH_SCOPE_AND_DIRECTION_CLARIFICATION | Stages are per exact version/adapter/scope; EXPORTED and IMPORTED are distinct branches; ROUNDTRIP requires both. |
| DEC-07 | Canonicalization and implementation | NOT_AUTHORIZED / OPEN | No implementation, Gate transition, schema build, or canonicalization is authorized by this review. |

## 9. Recommended schema work order

| Order | Register | Dependency note |
| --- | --- | --- |
| 1 | Object Identity | Define source-object identity, source scope, and explicit equivalence rules first. |
| 2 | Directory | Can be designed independently but must cross-reference Object Identity without deriving identity from paths; review alongside order 1. |
| 3 | Artifact | Depends on stable identity references and exact artifact/version distinction. |
| 4 | DeepRead | References source identity and artifact version; remains separate from Integrity. |
| 5 | Integrity | References source identity/artifact version and exact byte scope; independent of DeepRead. |
| 6 | Provenance & Rights | Depends on object, artifact, read, and integrity references; retains separate provenance and rights record families. |
| 7 | Route | Depends on registered directory/object/artifact targets and temporal resolution semantics. |

Object Identity and Directory should be reviewed as a dependency pair, despite their distinct ownership. DeepRead and Integrity should remain separate and can be developed in parallel after Artifact references are stable.

## 10. Final review state and boundaries

`REVIEW = PASS_WITH_REQUIRED_CORRECTIONS_AND_SCHEMA_PREREQUISITES`  
`SEVEN_REGISTER_SET = FROZEN_UNCHANGED`  
`REGISTER_ROLE_ASSIGNMENTS = ACCEPTED_WITH_CLARIFICATIONS`  
`RELATIONSHIP_MATRIX = CORRECTED_AND_ACCEPTED_FOR_FREEZE_CANDIDATE`  
`FIVE_STANDARD_TARGETS = ACCEPTED_UNCHANGED`  
`STANDARD_MAPPINGS = ACCEPTED_WITH_CORRECTIONS`  
`SUPPORT_LEVEL_MODEL = ACCEPTED_WITH_SCOPE_AND_DIRECTION_CLARIFICATION`  
`ARCHITECTURE_CONTRACT = FREEZE_CANDIDATE_NOT_FROZEN`  
`REGISTER_SCHEMAS = OPEN_NOT_STARTED`  
`GRAPH_VALIDATOR = OPEN_NOT_STARTED`  
`CROSSWALKS = OPEN_NOT_STARTED`  
`ADAPTERS = OPEN_NOT_STARTED`  
`FULL_LIBRARY_DEEPREAD = OPEN`  
`IMPLEMENTATION = OPEN_NOT_IMPLEMENTED`  
`CANONICALIZATION = NOT_AUTHORIZED`

The Freeze Candidate requires explicit operator acceptance before schema design begins. The open schema prerequisites remain visible and must not be converted into assumed values.

## 11. Source basis

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

**Design rules:** `RECONSTRUCT_BEFORE_EXTEND` · `PROOF_BEFORE_STATE` · `OBSERVE_BEFORE_MUTATE` · `APPEND_ONLY` · `NO_DRIFT` · `NO_INTERPRETATION` · `NO_PHANTOM` · `UNKNOWN_BY_DEFAULT` · `TRACEABILITY_REQUIRED` · `TEMPORAL_CONSISTENCY` · `DENSIFICATION_WITHOUT_ERASURE` · `OPEN_UNTIL_PASS`