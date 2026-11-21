# AIONARC_CHANNEL — WebSub Distribution Observation

**Artifact ID:** `AIONARC_CHANNEL_WEBSUB_DISTRIBUTION_OBSERVATION_1795250522_2026-11-21`  
**Schema:** `AIONARC_CHANNEL_WEBSUB_DISTRIBUTION_OBSERVATION/0.1.0`  
**Status:** `PUBLISHER_ACKNOWLEDGEMENT_OBSERVED / DUAL_HUB_CONFIGURED / SUBSCRIBER_DELIVERY_OPEN`  
**Repository:** `k501-Information-Space/AIONARC_CHANNEL`  
**Operator authorization anchor:** `1795249183` — 2026-11-21 08:19:43 UTC  
**Observation anchor:** `1795250522` — 2026-11-21 08:42:02 UTC / 09:42:02 Europe/Berlin

## 1. Scope

This record captures a bounded publisher-endpoint investigation following repeated HTTP 401 responses from the previously selected Switchboard hub. It records publisher responses only for the AIONARC_CHANNEL-owned RSS, Atom and JSON Feed topics.

It does not assert search-engine indexing, subscriber subscription, subscriber delivery, notification processing or content consumption.

## 2. Observed endpoint responses

| Publisher endpoint | RSS | Atom | JSON Feed | Interpretation |
|---|---:|---:|---:|---|
| Google PubSubHubbub — `https://pubsubhubbub.appspot.com/` | 204 | 204 | 204 | Publisher announcement acknowledged |
| Switchboard — `https://switchboard.p3k.io/` | 401 | 401 | 401 | Publisher announcement rejected |
| WebSubHub — `https://websubhub.com/hub` | 500 | 500 | 500 | `Topic not found for topic URL`; no topic record exists |
| Superfeedr — `https://websub.superfeedr.com/` | 204 | 204 | 204 | Generic acknowledgement; not treated as acceptance proof |

All three feed topics returned HTTP 200 to HEAD requests. Switchboard responses included `server: nginx/1.14.0`, `content-type: text/html;charset=UTF-8`, an empty body and no `WWW-Authenticate` header. Its legacy parameter alias (`hub_mode`, `hub_url`) also returned HTTP 401 for RSS.

The publicly available Switchboard publisher controller accepts dotted or underscored parameter names and documents a successful 202 response for valid publish requests. Its documented route does not explain the observed 401. The remaining cause is external to this repository and requires production-host evidence from Switchboard.

WebSubHub returned `Topic not found` for all three feeds. Its public implementation creates a topic record through a successful subscription flow; no test subscription was created here.

Superfeedr returned 204, but its documentation describes a generic anti-spam acknowledgement. No account-side topic analytics were available to corroborate feed registration.

## 3. Configured hub order

1. **Primary:** `https://pubsubhubbub.appspot.com/` — all three publisher requests returned HTTP 204.
2. **Retained secondary:** `https://switchboard.p3k.io/` — preserved in feed declarations and continues to be notified, but currently returns HTTP 401.

The feed projections advertise both hubs. The publisher workflow attempts each hub independently. A feed topic is operationally acknowledged when at least one declared hub returns HTTP 2xx. Failure from one hub is recorded without suppressing the accepted route through the other.

WebSubHub and Superfeedr remain tested candidates only; they are not included in active feed declarations.

## 4. Evidence boundaries

**PASS — publisher acknowledgement:** Google PubSubHubbub returned HTTP 204 for RSS, Atom and JSON Feed.

**BLOCKED — Switchboard publisher acknowledgement:** HTTP 401 persists for all three feeds, including its legacy parameter alias.

**OPEN — subscriber delivery:** A 2xx publisher response does not prove that any subscriber is active, fetched the hub notification, retrieved the topic or processed the content.

**OPEN — search discovery:** IndexNow submission acceptance is not proof of crawling or indexing.

## 5. Identity and history

No signal ID, target URL, source title, source description, channel permalink or legacy identifier was changed by this update. The previous Switchboard selection remains recorded as `previously_selected_hub_url`. The old `SIGNAL_NNNN` namespace remains historical and untouched. Gateway and Index remain navigation surfaces.

## 6. Reproduction references

- [Switchboard diagnostic run](https://github.com/k501-Information-Space/AIONARC_CHANNEL/actions/runs/44885599990)
- [Public hub compatibility probe](https://github.com/k501-Information-Space/AIONARC_CHANNEL/actions/runs/44886018255)
- [Switchboard publisher controller](https://github.com/aaronpk/Switchboard/blob/master/controllers/push.php)
- [WebSubHub source](https://github.com/clone1018/WebSubHub)

**Operational state:** Google PubSubHubbub is the current primary publisher endpoint. Switchboard is retained as a secondary declaration pending external resolution. Subscriber delivery remains OPEN.
