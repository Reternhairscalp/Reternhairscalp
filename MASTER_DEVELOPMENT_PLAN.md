# Retern Intelligence Platform — Master Development Plan

Version: 1.0  
Status: Active  
Owner: CEO, Retern Hair Growth  
Last Updated: 14 July 2026

---

## Purpose

This document is the single source of truth for the development of the Retern Intelligence Platform (RIP). It defines what RIP is, why it is being built, how it must be engineered, and the order in which its capabilities will be delivered.

When another roadmap, blueprint, or technical note conflicts with this document, this document takes precedence. Business policies, prices, treatments, customer guidance, and operating procedures remain owned by their relevant approved business documents.

Changes to this plan require explicit approval from the project owner.

---

## 1. Project Vision

RIP is the AI-powered business operating system for Retern Hair Growth.

Its purpose is to help the company understand customers, manage the complete customer lifecycle, automate repetitive work, improve decisions, and grow revenue while protecting customer trust.

RIP will connect four essential capabilities:

1. A governed business knowledge base.
2. A reliable customer and operational data platform.
3. Measurable business workflows and automations.
4. AI assistants that support staff and customers under human oversight.

The long-term outcome is a secure, auditable platform that can:

- Remember every authorized customer interaction.
- Guide leads from enquiry to appointment and long-term care.
- Help staff provide consistent, personalized service.
- Automate approved marketing and operational tasks.
- Give management accurate, timely business intelligence.
- Coordinate specialized AI capabilities through shared services.

AI is an enabler. Customer value and measurable business outcomes are the objective.

---

## 2. Business Goals

### Primary targets

- Generate 500 qualified leads per month.
- Achieve 200 confirmed appointments per month.
- Improve lead-to-appointment conversion.
- Improve consultation and package conversion.
- Increase customer retention and lifetime value.
- Reduce repetitive manual work without reducing service quality.

### Customer outcomes

- Faster and more consistent responses.
- Personalized communication based on consented customer data.
- Clear, responsible consultation and treatment guidance.
- Reliable appointment reminders and follow-up.
- A measurable long-term treatment journey.

### Operating outcomes

- One authoritative record for every customer and workflow.
- Standardized processes across marketing, sales, reception, consultation, treatment, and follow-up.
- Accurate dashboards based on operational data rather than static values.
- Human approval for sensitive, high-impact, or uncertain AI actions.

### Core metrics

- Qualified leads per month
- Lead response time
- Lead qualification rate
- Appointment booking rate
- Appointment attendance and no-show rates
- Consultation conversion rate
- Package conversion rate
- Revenue and average revenue per customer
- Customer retention and repeat-visit rates
- Referral and review rates
- Customer satisfaction
- Automation success and exception rates
- AI recommendation accuracy and escalation rate

Every metric must have an owner, definition, source, time window, and refresh schedule before it appears on a dashboard.

---

## 3. Architecture Principles

### Business first

Every feature must improve customer experience, revenue, decision quality, operational efficiency, or risk control. Features without a defined outcome and acceptance criteria must not enter development.

### Modular monolith first

RIP will begin as one deployable backend divided into clear domain modules. Microservices may be introduced only when demonstrated scale, security, ownership, or deployment requirements justify them.

### Separate knowledge from operational data

- Markdown stores approved business knowledge such as policies, SOPs, FAQs, treatments, and communication guidance.
- A relational database stores customers, consent, leads, appointments, consultations, payments, and workflow state.
- Object storage stores authorized images and documents.
- A search index may store derived knowledge chunks for retrieval.

### One source of truth

Each fact or business rule must have one authoritative owner. Python code must not duplicate prices, treatment rules, schedules, or targets when these can be loaded from validated configuration or approved knowledge.

### Stable domain boundaries

Core domains are:

- Identity and access
- Customers and consent
- Leads and conversations
- Appointments
- Consultations and assessments
- Treatments, packages, and sessions
- Communications and follow-up
- Billing and payments
- Marketing and attribution
- Analytics and reporting
- Knowledge management
- AI assistance and approvals
- Audit and compliance

Domain modules own their data and expose explicit application use cases. AI agents and external integrations must use these interfaces rather than modifying domain state directly.

### Dependency direction

Business rules must not depend directly on frameworks or external providers. Infrastructure implements interfaces owned by application or domain layers.

```text
Channels and API
      ↓
Application use cases
      ↓
Domain rules
      ↓
Infrastructure interfaces
      ↓
Database, queues, AI models, and external providers
```

### Reliability by design

All external operations require validation, timeouts, retry rules, idempotency where relevant, error reporting, and audit records. A printed success message is not proof that a module is operational.

### Security and privacy by design

RIP must enforce least-privilege access, explicit consent, data minimization, secure secret handling, retention rules, and auditable access to customer information. Sensitive customer and health-related information must receive stronger controls than general business data.

### Observable and testable

Every production workflow must produce structured logs, measurable outcomes, and actionable failure information. Business logic must be testable without live external services.

---

## 4. Coding Standards

### Python standards

- Use supported Python 3 syntax and declare the supported version in project configuration.
- Follow PEP 8 naming and formatting conventions.
- Use type hints on public functions, methods, and domain interfaces.
- Write short functions with one clear responsibility.
- Prefer explicit data models over unstructured dictionaries at module boundaries.
- Use dependency injection for databases, AI providers, clocks, and external integrations.
- Keep business rules out of API routes and provider adapters.
- Avoid global mutable state.
- Never store credentials or customer data in source code.

### SOLID application

- **Single Responsibility:** each class or module has one reason to change.
- **Open/Closed:** extend behavior through interfaces and strategies rather than repeated conditionals where practical.
- **Liskov Substitution:** implementations must honor the behavior promised by their interfaces.
- **Interface Segregation:** consumers depend only on operations they need.
- **Dependency Inversion:** domain and application code depend on abstractions, not concrete infrastructure.

SOLID is a design guide, not a reason to create unnecessary abstractions.

### Public contracts

- Define and document input, output, validation, error, and side-effect behavior.
- Preserve existing contracts unless an approved migration plan exists.
- Use versioned API contracts when breaking changes are unavoidable.
- Return structured errors; do not rely on console output for failure handling.

### Testing

- Unit-test domain rules and extraction logic.
- Integration-test database repositories and provider adapters.
- Contract-test external integrations and webhooks.
- Add end-to-end tests for critical customer workflows.
- Every defect fix must include a regression test.
- Tests must be deterministic and must not require production credentials.

### Documentation and comments

- Document intent, constraints, and non-obvious decisions.
- Do not comment code that is already self-explanatory.
- Update this plan when an approved architectural or roadmap decision changes.
- Use decision records for significant choices that require historical context.

### Definition of done

A feature is complete only when:

- Acceptance criteria are satisfied.
- Tests pass.
- Errors and edge cases are handled.
- Security and privacy impacts are reviewed.
- Operational logging and metrics are present where needed.
- User-facing and developer documentation is current.
- No unrelated files are included in the change.
- Human approval requirements are enforced.

---

## 5. Folder Structure

### Current structure

```text
Retern intelligence platform/
├── AI Workforce/
├── Architecture/
├── Business/
├── Consitution/
├── Customer DNA/
├── Develpment/
├── Operations/
├── Vision/
├── backend/
│   ├── agents/
│   ├── consultation/
│   ├── core/
│   ├── dashboard/
│   ├── database/
│   ├── knowledge/
│   └── services/
├── MASTER_DEVELOPMENT_PLAN.md
└── README.md
```

Existing paths must not be renamed casually. Renames require an approved migration because documentation, imports, and deployment tooling may depend on them.

### Target backend structure

The project will evolve incrementally toward the following structure while preserving working contracts:

```text
backend/
├── app/
│   ├── main.py
│   ├── settings.py
│   └── dependencies.py
├── api/
│   ├── routes/
│   ├── schemas/
│   └── middleware/
├── domains/
│   ├── customers/
│   ├── leads/
│   ├── appointments/
│   ├── consultations/
│   ├── treatments/
│   ├── communications/
│   ├── billing/
│   └── analytics/
├── knowledge/
│   ├── catalog.py
│   ├── ingestion.py
│   ├── retrieval.py
│   └── citations.py
├── ai/
│   ├── providers/
│   ├── policies.py
│   ├── prompts/
│   └── evaluations/
├── integrations/
│   ├── whatsapp/
│   ├── calendar/
│   ├── crm/
│   └── payments/
├── infrastructure/
│   ├── database/
│   ├── jobs/
│   ├── logging/
│   └── audit/
└── tests/
    ├── unit/
    ├── integration/
    └── end_to_end/
```

Migration to this target is incremental. A feature must not move unrelated modules merely to make the repository resemble the target structure.

---

## 6. AI Development Rules

### Role of AI

AI assists with classification, retrieval, drafting, summarization, recommendations, and decision support. AI does not become the authoritative store of customer or business state.

### Knowledge grounding

- Use approved, versioned business knowledge before answering business questions.
- Retain source references for retrieved guidance.
- Do not invent missing customer facts, prices, policies, treatment claims, or results.
- Conflicting or missing knowledge must be escalated for human resolution.

### Structured output

AI outputs used by software must conform to validated schemas. Free-form text must not directly trigger payments, bookings, customer record changes, or outbound campaigns.

### Human oversight

Human approval is mandatory for:

- Treatment or health-related recommendations beyond approved low-risk guidance
- High-value commercial offers or exceptions
- Payments, refunds, and financial adjustments
- Publishing campaigns or public claims without an approved policy
- Deleting or exporting customer data
- Actions with low confidence or conflicting evidence

### Safety

- Never promise guaranteed hair growth or treatment results.
- Distinguish scalp-wellness guidance from medical diagnosis.
- Identify approved red flags and refer them to qualified human professionals.
- Respect opt-out requests and communication preferences.
- Prevent private business knowledge or one customer's data from appearing in another customer's response.

### Confidence and escalation

Confidence scores must have documented meaning. They must be based on observable evidence or evaluated model behavior, not arbitrary values. Low-confidence results must request missing information or enter a review queue.

### Agent permissions

Each agent must have:

- A single defined mission
- An accountable human owner
- Explicit inputs and outputs
- An allowlist of tools and data
- Defined approval boundaries
- KPIs and quality thresholds
- Failure and escalation behavior
- An audit trail

Agents must call shared domain services. They must not implement duplicate customer, pricing, appointment, or treatment logic.

### Evaluation

No AI capability is production-ready until it has:

- A representative evaluation dataset
- Accuracy and safety acceptance thresholds
- Known failure cases
- Regression tests for prompts or policies
- Cost and latency measurements
- Human review of customer-facing behavior

---

## 7. Git Workflow

### Branches

- Keep the default branch releasable.
- Create one short-lived branch per feature or fix.
- Suggested names: `feature/001-consultation-analyzer`, `fix/consultation-negation`, or `docs/master-development-plan`.
- Do not combine unrelated work in one branch or pull request.

### Before changing files

1. Read this master plan and relevant business documentation.
2. Inspect repository status and preserve existing user changes.
3. State the intended files, contracts, and acceptance criteria.
4. Obtain approval when the requested workflow requires it.

### Commits

- Commit only after explicit authorization when an agent is performing the work.
- Make commits small, coherent, and reviewable.
- Use imperative messages, such as `Add consultation detail extraction`.
- Never commit credentials, customer information, generated caches, or local environment files.
- Do not rewrite shared history without explicit approval.

### Pull requests

Each pull request must include:

- Business purpose
- Scope and files changed
- Contract or data-model changes
- Test evidence
- Security and privacy impact
- Deployment or migration steps
- Known limitations and follow-up work

### Releases

- Use semantic versioning after the first defined release baseline.
- Release from a reviewed and tested revision.
- Database changes require forward and rollback procedures.
- Production deployments require monitoring and a named owner.

---

## 8. Sprint Roadmap

Sprint boundaries are outcome-based. Dates are assigned only when owner capacity and dependencies are confirmed.

### Sprint 0 — Engineering baseline

**Objective:** Make development reproducible and the application reliably executable.

- Repair startup and package integrity.
- Declare Python version and dependencies.
- Establish settings and environment handling.
- Add structured logging and error conventions.
- Create a real test structure and continuous integration checks.
- Define development, staging, and production environments.

**Exit:** A clean checkout can be installed, tested, and started using documented commands.

### Sprint 1 — Consultation foundation

**Objective:** Produce reliable structured consultation information.

- Feature 001: Customer Consultation Analyzer.
- Define a validated consultation result schema.
- Add representative unit and regression tests.
- Add clarification and escalation rules for incomplete inputs.
- Align treatment terminology with approved business knowledge.

**Exit:** Consultation messages produce tested, explainable structured facts without breaking current consumers.

### Sprint 2 — Customer, consent, and lead records

**Objective:** Establish persistent customer lifecycle data.

- Define customer, consent, lead, and conversation models.
- Add relational persistence and migrations.
- Implement create, update, search, and audit use cases.
- Define retention, access, correction, and deletion rules.

**Exit:** Authorized customer and lead information persists securely with an audit history.

### Sprint 3 — Lead-to-appointment workflow

**Objective:** Deliver the first complete business workflow.

- Lead qualification.
- Appointment availability and booking.
- Confirmation, reminder, rescheduling, and cancellation states.
- Follow-up tasks and no-show recovery.
- Idempotent APIs and integration boundaries.

**Exit:** A lead can progress reliably from enquiry to completed or missed appointment.

### Sprint 4 — Governed knowledge engine

**Objective:** Make approved business knowledge searchable and traceable.

- Catalog all business documents.
- Add ownership, version, status, sensitivity, and review metadata.
- Detect incomplete or conflicting rules.
- Implement ingestion, retrieval, access control, and citations.
- Add knowledge quality evaluations.

**Exit:** Staff and approved AI features can retrieve current guidance with provenance.

### Sprint 5 — WhatsApp integration

**Objective:** Connect the validated workflow to the primary communication channel.

- Receive and verify webhooks.
- Match conversations to leads and customers.
- Draft approved responses.
- Enforce consent, opt-out, retries, idempotency, and human handoff.
- Monitor delivery and failures.

**Exit:** WhatsApp messages can safely enter and progress through the lead workflow.

### Sprint 6 — Consultation and treatment journey

**Objective:** Support human-reviewed assessments and longitudinal care.

- Consultation and scalp-assessment records.
- Treatment recommendation approval.
- Treatment plans, packages, sessions, and progress notes.
- Authorized media storage.
- Follow-up and review milestones.

**Exit:** Staff can manage a customer's approved consultation-to-treatment journey.

### Sprint 7 — Business intelligence dashboard

**Objective:** Provide factual operational visibility.

- Define metric contracts and owners.
- Implement lead, appointment, conversion, revenue, and retention measures.
- Add source timestamps and drill-downs.
- Add daily management briefing and exception reporting.

**Exit:** Management can verify targets against current operational data.

### Sprint 8 — Controlled AI assistance

**Objective:** Introduce evaluated AI support to proven workflows.

- Retrieval-backed FAQ drafting.
- Consultation-note summarization.
- Follow-up drafting.
- Next-best-action suggestions.
- Approval queues, quality evaluation, cost tracking, and audit logs.

**Exit:** Approved AI capabilities save staff time while meeting measured quality and safety thresholds.

---

## 9. Module Roadmap

| Module | Responsibility | Current state | Target milestone |
|---|---|---|---|
| Core application | Startup, settings, dependency composition | Prototype | Sprint 0 |
| Logging and audit | Structured operational and access history | Placeholder | Sprints 0–2 |
| Consultation analyzer | Extract customer consultation facts | Feature 001 production baseline implemented and verified | Sprint 1 |
| Consultation recommender | Produce approved treatment suggestions | Rule-based prototype | Sprint 6 |
| Customer DNA | Canonical customer profile and preferences | Documentation only | Sprint 2 |
| Consent and privacy | Purpose, permission, retention, deletion | Not implemented | Sprint 2 |
| Lead management | Qualification and lifecycle state | Not implemented | Sprints 2–3 |
| Appointment service | Booking, reminders, rescheduling, no-shows | Not implemented | Sprint 3 |
| Knowledge engine | Catalog, validation, retrieval, citations | Customer-document loader prototype | Sprint 4 |
| WhatsApp channel | Inbound/outbound messaging and handoff | Text generator prototype | Sprint 5 |
| Treatment journey | Plans, sessions, progress, follow-up | Not implemented | Sprint 6 |
| Billing and payments | Packages, invoices, payments, refunds | Not implemented | After Sprint 6 |
| Analytics | Metric calculation and reporting | Static console dashboard | Sprint 7 |
| AI platform | Providers, policies, prompts, evaluation | In-memory prototype | Sprint 8 |
| Marketing automation | Content and campaign workflows | Readiness-print prototype | After Sprint 8 |
| External integrations | CRM, calendar, reviews, social, website | Not implemented | As required by validated workflows |

Module status must be updated when acceptance criteria are met, not when a placeholder or class name is added.

---

## 10. Future AI Agents

Agents will be introduced only after their required data, domain services, permissions, and evaluations exist.

### Customer-facing and revenue agents

- **Lead Qualification AI:** extracts lead needs, asks approved clarifying questions, and recommends routing.
- **Sales Assistant AI:** gives staff grounded answers, drafts follow-ups, and suggests approved next actions.
- **Reception AI:** handles appointment questions, availability, reminders, and human handoff.
- **Consultation Assistant AI:** summarizes consultation information and drafts recommendations for professional approval.
- **Customer Success AI:** monitors follow-ups, treatment milestones, satisfaction, retention risk, and reactivation opportunities.
- **WhatsApp AI:** coordinates approved conversational workflows through the WhatsApp integration.

### Growth agents

- **Marketing AI:** plans and drafts approved campaigns aligned with business goals.
- **Content AI:** produces channel-specific drafts from approved knowledge and brand guidance.
- **SEO AI:** researches, briefs, and monitors search content with human publication approval.
- **Social Media AI:** prepares publishing calendars, drafts, and performance summaries.
- **Advertising AI:** analyzes campaign performance and proposes budget or creative changes for approval.
- **Review and Referral AI:** coordinates compliant review requests and referral follow-up.

### Operating agents

- **Operations AI:** identifies workflow exceptions, capacity constraints, and process improvements.
- **Finance AI:** prepares revenue, payment, and variance analysis without autonomous financial authority.
- **Inventory AI:** monitors product and treatment-supply usage and recommends replenishment.
- **Analytics AI:** explains validated metrics and highlights anomalies with supporting evidence.
- **Knowledge AI:** identifies stale, conflicting, or missing documentation and routes it to owners.
- **Compliance and Audit AI:** flags policy violations, access anomalies, and missing approvals for human review.

### Management agents

- **Management AI:** combines verified departmental information into an operating briefing.
- **Chief AI Officer:** monitors agent quality, cost, safety, permissions, and improvement priorities.
- **CEO Assistant:** presents verified business status, decisions requiring attention, and traceable recommendations.

No agent may be considered autonomous merely because it can generate text. Operational status requires connected tools, enforced permissions, monitored execution, measurable outcomes, and tested failure handling.

---

## Change Control

The project owner approves changes to vision, business goals, architecture principles, sprint priorities, and agent authority.

Every approved update to this document must record:

- What changed
- Why it changed
- Who approved it
- Which modules or sprints are affected
- The effective date

Until approval is given, proposed changes remain proposals and must not be implemented.

### Approved change record

#### 14 July 2026 — Sprint 1, Feature 001

- **Change:** Implemented the production baseline for the Customer Consultation Analyzer.
- **Reason:** Establish a typed, tested, safety-aware consultation contract for current and future RIP consumers.
- **Approval:** Project owner approved implementation of the engineering plan.
- **Affected modules:** Consultation analysis, recommendation safety, WhatsApp response generation, and consultation tests.
- **Effective date:** 14 July 2026.
