# Workflow diagrams

Diagrams for [PurpleBelt's One-Prompt Solution Builder](../../references/one-prompt-solution-builder.md).

**Architecture blueprints only.** These pictures are documentation rendered directly by GitHub from editable [Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) text. They do **not** provision a Copilot Studio Workflow or prove connected tenant operation.

## 1. One-prompt builder — design, build and release gates

This is the **developer experience** inside VS Code. It may generate some components directly, but a workflow canvas, connection, publication or Teams test can require supported tenant tooling and authorization. A diagram is never the deployment artifact.

```mermaid
flowchart TD
  subgraph IDE["VS Code · One-Prompt Solution Builder (design-time)"]
    A["Business outcome + one prompt"] --> B["Discover workspace, harness and permissions"]
    B --> C["Select simplest architecture + data contracts"]
    C --> D{"Verified authoring tools available?"}
    D -->|Yes| E["Generate native components + test fixtures"]
    D -->|No| F["Designer-ready build sheet + UNBOUND connections"]
    E --> G["Local validation + failure tests"]
  end
  subgraph CLOUD["Microsoft tenant · explicitly authorized steps"]
    G --> H{"Connections, DLP and approvals ready?"}
    H -->|Yes| I["Sync / provision with supported tooling"]
    I --> J["Publish where required"]
    J --> K["Run real trigger → reasoning → channel"]
    H -->|No| F
  end
  K --> L{"Observed intended effect?"}
  L -->|Yes| M["Delivery report + measured evidence"]
  L -->|No| N["Diagnose failed step, reconcile and retest"]
  N --> G
  F --> O["Pending manual/tenant steps + exact owner"]
  O --> M
  classDef input fill:#ede9fe,stroke:#7c3aed,color:#3b0764,stroke-width:2px;
  classDef decision fill:#fef3c7,stroke:#d97706,color:#78350f,stroke-width:2px;
  classDef output fill:#dcfce7,stroke:#16a34a,color:#14532d,stroke-width:2px;
  classDef gate fill:#fee2e2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
  class A input;
  class D,H,L decision;
  class F,O,N gate;
  class M output;
```

## 2. Financial News Intelligence — runtime workflow

Reference scenario: an approved feed is polled on a schedule, deterministic filters run first, then a bounded AI step explains relevant news, and only verified high-importance alerts reach Teams. Use **either a bounded AI Prompt or a compatible Agent node** when the chosen workflow/runtime supports it; do not assume Power Automate can invoke modern-harness agents.

```mermaid
flowchart TD
  subgraph INGEST["01 · Scheduled flow / approved connector"]
    T["Every 30 minutes"] --> S["Read permitted RSS / News API"]
    S --> Q{"New records fetched?"}
    Q -->|No| Z["End: no alert"]
    Q -->|Yes| N["Normalize ID, URL, source and publish time"]
    N --> D{"Already seen or stale?"}
    D -->|Yes| Z
    D -->|No| R{"Relevant to portfolio scope?"}
    R -->|No| Z
  end
  subgraph INTELLIGENCE["02 · Bounded AI step (prompt or supported Agent node)"]
    R -->|Yes| A["Grounded impact analysis + cited evidence"]
    A --> G{"Sufficient fresh evidence?"}
    G -->|No| REVIEW["Hold for review / log uncertainty"]
    G -->|Yes| P{"Material impact threshold met?"}
    P -->|No| LOW["Log / suppress routine news"]
  end
  subgraph ACTION["03 · Approved business actions"]
    P -->|Yes| CLAIM{"Alert key safely reserved?"}
    CLAIM -->|No / unknown| STOP["Reconcile or manual gate; no blind resend"]
    CLAIM -->|Yes| TEAMS["Post cited alert to Microsoft Teams"]
    TEAMS --> CHECK{"Delivery evidence confirmed?"}
    CHECK -->|Yes| SENT["Mark sent; retain message evidence"]
    CHECK -->|No / timeout| REC["Reconcile actual state before retry"]
  end
  classDef trigger fill:#ede9fe,stroke:#7c3aed,color:#3b0764,stroke-width:2px;
  classDef decision fill:#fef3c7,stroke:#d97706,color:#78350f,stroke-width:2px;
  classDef ai fill:#dbeafe,stroke:#2563eb,color:#1e3a8a,stroke-width:2px;
  classDef effect fill:#dcfce7,stroke:#16a34a,color:#14532d,stroke-width:2px;
  classDef halt fill:#fee2e2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
  class T trigger;
  class Q,D,R,G,P,CLAIM,CHECK decision;
  class A ai;
  class TEAMS,SENT effect;
  class REVIEW,STOP,REC halt;
```

**Implementation notes:** Source connectors, identities, quotas, portfolio permissions and Teams destination are **UNBOUND** until verified in the user's environment. An alert ledger can be a permitted SharePoint list or another suitable durable store; an atomic unique-claim mechanism must actually be supported to avoid concurrent duplicates. If that mechanism is unavailable, use a controlled consumer/reconciliation process and explicitly report residual duplicate risk.

The diagram's `SENT` state requires a checked, observable Teams delivery effect, not just an AI answer or local simulation. No snapshot may be labeled live news without an operational trigger. A failed Teams send should not blindly replay if a prior attempt may already have posted.

## How to maintain these diagrams

1. Edit the fenced `mermaid` code in this Markdown file. GitHub re-renders it automatically. Keep the diagram text editable and source-controlled (no PNG-only design).
2. For a new business project, generate its own `docs/diagrams/workflow.md` using [Diagram design guide](../../references/diagram-design.md). Include a **builder/architecture** view and a **runtime/decision** view for multi-component work.
3. Label proposal versus actual implementation explicitly; tie each external edge to a connector/identity, and each side effect to an observed test.
4. After changing connections or branch conditions, update the architecture diagram, build sheet and acceptance tests in the same change.
