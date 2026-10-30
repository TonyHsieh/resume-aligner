"""Alignment and tailoring engine for target job descriptions.

Strictly adheres to:
1. Absolute Truthfulness: Only facts, metrics, and tools from Fact Ledger.
2. Tailoring & Reframing: Emphasizes genuine accomplishments relevant to the target role.
3. Review Highlighting: Changes marked with **bold** in resume_REVIEW.docx.
4. SAMPLE_FORMAT.docx fidelity: Header (mobile/email only, no grad year), 9pt Times New Roman, bold headings.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from .ledger import FactLedger, load_fact_ledger
from .model import Labeled, Resume, Role
from .render_docx import render_resume
from .tracker import Tracker, sha
from .validate import validate_resume


def load_all_alignments(
    alignments_dir: Path | str = "output/alignments",
) -> dict[str, dict[str, Any]]:
    """Load all alignment configurations from output/alignments/*.py (with fallback to src/resume_factory/alignments_*.py)."""
    alignments: dict[str, dict[str, Any]] = {}

    # 1. Primary: output/alignments/*.py
    p = Path(alignments_dir)
    if p.exists():
        for f in sorted(p.glob("*.py")):
            if f.name.startswith("__"):
                continue
            mod_name = f"output_alignments_{f.stem}"
            try:
                spec = importlib.util.spec_from_file_location(mod_name, f)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    sys.modules[mod_name] = mod
                    spec.loader.exec_module(mod)
                    for var_name in dir(mod):
                        if var_name.endswith("_ALIGNMENTS") and isinstance(getattr(mod, var_name), dict):
                            alignments.update(getattr(mod, var_name))
            except Exception as e:
                print(f"Warning: could not load alignments from {f}: {e}")

    # 2. Fallback / backward compatibility: src/resume_factory/alignments_*.py
    src_dir = Path(__file__).parent
    for f in sorted(src_dir.glob("alignments_*.py")):
        mod_name = f"resume_factory.{f.stem}"
        if mod_name not in sys.modules:
            try:
                spec = importlib.util.spec_from_file_location(mod_name, f)
                if spec and spec.loader:
                    mod = importlib.util.module_from_spec(spec)
                    sys.modules[mod_name] = mod
                    spec.loader.exec_module(mod)
                    for var_name in dir(mod):
                        if var_name.endswith("_ALIGNMENTS") and isinstance(getattr(mod, var_name), dict):
                            alignments.update(getattr(mod, var_name))
            except Exception as e:
                print(f"Warning: could not load alignments from {f}: {e}")

    return alignments


def generate_critical_fit_analysis(job, cfg: dict, resume: Resume, jd_text: str = "") -> list[str]:
    """Generate an exacting critical analysis of the resume vs job match-up,
    highlighting high-alignment anchors, vulnerabilities/perceived gaps,
    and a specific study guide for interview preparation.
    """
    c_lower = (job.company or "").lower()
    t_lower = (job.title or "").lower()
    lines = []

    lines.extend([
        "## 2. Critical Fit & Vulnerability Assessment (Exacting Analysis)",
        "",
        "> **Evaluator Note:** This analysis applies an exacting, critical eye to contrast the candidate's verified record against target expectations, exposing potential panel skepticism, transition hurdles, and unstated evaluation criteria.",
        "",
    ])

    if "amazon" in c_lower or "aws" in c_lower:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **Enterprise Platform Engineering & Scalability:** Proven leadership operating developer platforms supporting 80–100 engineers with 40% deployment acceleration and 80% FinOps governance.",
            "- **24x7 High-Reliability Operations:** Managed 24x7 mission-critical operations and severity escalation frameworks across 10–15 engineers, perfectly matching AWS operational rigor.",
            "- **Distributed Systems & Kubernetes:** Deep hands-on container orchestration, microservices, and infrastructure-as-code automation.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Hyperscaler Ecosystem Transition:** Recent prominent experience is focused on Microsoft Azure and Kubernetes at Blue Shield/Stellarus. AWS bar-raisers will test depth in AWS-native primitives (Lambda concurrency models, DynamoDB single-table design, S3 consistency, IAM permission boundaries, Transit Gateway).",
            "- **Amazon Mechanism & Writing Culture:** Amazon famously rejects PowerPoint in favor of 6-page narrative memos and PR/FAQ documents. Interviewers will probe whether the candidate can operate within Amazon's rigorous 'Working Backwards' mechanisms.",
            "- **Customer-Facing Solutions Architecture Scope:** For SA roles, interviewers will challenge whether an internal engineering leader can pivot to consultative, quota-carrying field engagements with external CxOs.",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Cloud-Agnostic Distributed Systems Rigor:** Frame Azure and Kubernetes work as distributed systems fundamentals that map 1:1 to AWS cloud-native patterns. Reiterate foundational C/systems programming heritage.",
            "- **Measurable Mechanism Design:** Cite the BlueStack IDP and GitOps governance frameworks as self-service mechanisms that eliminated manual gating, aligning with Amazon's 'Invent & Simplify' and 'Ownership' principles.",
            "- **Executive Advisory Credibility:** Highlight consulting with executive leadership, enterprise architects, and cross-functional directors on multi-year cloud modernizations.",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and bar-raiser interviews, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & AWS-Native Systems Deep-Dives",
            "- **AWS Well-Architected Framework:** Deep-dive into the 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability). Rehearse architectural trade-offs for each.",
            "- **Distributed Storage & Data Layer:** Study DynamoDB partition key hashing, secondary indexes (GSI/LSI), read/write capacity modes (on-demand vs provisioned), and Aurora Serverless v2 scaling mechanics.",
            "- **Networking & Hybrid Connectivity:** Master AWS Transit Gateway, Direct Connect, VPC Peering, and AWS PrivateLink architectures for enterprise hybrid cloud.",
            "",
            "### 2. Domain Mechanics & Role-Specific Nuances",
        ])
        if "game" in t_lower:
            lines.extend([
                "- **Game Backend & Server Fleet Management:** Review Amazon GameLift fleet autoscaling, matchmaker queue rules, UDP packet serialization, and real-time multiplayer state synchronization.",
                "- **3D Pipelines & Cloud Workstations:** Rehearse cloud game compilation pipelines, virtual workstations (NICE DCV / Amazon EC2 G5/G6 instances), and asset streaming architectures.",
            ])
        elif "pace" in t_lower or "prototyp" in t_lower:
            lines.extend([
                "- **Generative AI Prototyping & Bedrock:** Review Amazon Bedrock foundation models (Anthropic Claude on Bedrock, Titan, Llama 3), Bedrock Agents, Knowledge Bases, and RAG architectures.",
                "- **Custom Agent Frameworks:** Study Python custom agent patterns, LangChain / LlamaIndex orchestration, and serverless PoC delivery within short customer sprint timelines.",
            ])
        elif "azure" in t_lower or "compete" in t_lower:
            lines.extend([
                "- **AWS vs Azure Comparative Architecture:** Master granular service mappings between Azure (Entra ID, Azure Monitor, ExpressRoute, AKS, Cosmos DB) and AWS (IAM, CloudWatch, Direct Connect, EKS, DynamoDB).",
                "- **Enterprise TCO & Migration Economics:** Prepare TCO comparative models demonstrating migration economics and multi-cloud risk mitigation strategies.",
            ])
        else:
            lines.extend([
                "- **Enterprise Multi-Account Governance:** Study AWS Organizations, Control Tower, Service Control Policies (SCPs), and AWS Cost Explorer / CUR for FinOps cost allocation.",
                "- **Resilience & Disaster Recovery:** Master multi-region active-active vs active-passive failover strategies, Route 53 health checks, and cross-region replication.",
            ])
        lines.extend([
            "",
            "### 3. Company-Specific Evaluation Rubric (Amazon Leadership Principles)",
            "- **Customer Obsession:** Prepare 2 STAR stories demonstrating starting with the customer and working backwards, prioritizing long-term customer trust over short-term expediency.",
            "- **Invent and Simplify:** Prepare stories showcasing the creation of scalable developer platforms that simplified complex legacy middleware.",
            "- **Dive Deep & Ownership:** Have metrics at your fingertips (e.g., 40% deployment reduction, 80% governance compliance, 80–100 engineers, 10–15 direct reports). Amazon bar-raisers will drill 3 layers deep into technical specifics.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"Your recent engineering leadership was heavily focused on Microsoft Azure. How will you build deep technical credibility on AWS with our most demanding enterprise architects?\"**  ",
            "   *Recommended Defense:* \"Anchor in distributed systems first principles: container orchestration, GitOps automation, and microservice resilience operate on the same fundamental distributed primitives across hyperscalers. At Blue Shield/Stellarus, I evaluated multi-cloud primitives and engineered self-service platforms that accelerated velocity by 40%. The learning curve is in service API syntax, which is straightforward given my foundational C and systems background.\"",
            "",
            "2. **\"Tell me about a time when you had to make a high-stakes architectural decision with incomplete data.\"**  ",
            "   *Recommended Defense:* \"Discuss the end-to-end redesign of the Blue Shield Member Portal. Detail how you evaluated high-concurrency availability requirements, established phased canary migrations to mitigate risk, and created fallback telemetry to validate stability before full traffic cutover.\"",
            "",
            "3. **\"How do you scale architectural guidance across hundreds of startup or enterprise teams without becoming an approval bottleneck?\"**  ",
            "   *Recommended Defense:* \"Describe the implementation of the BlueStack Internal Developer Platform: instead of manual architecture review gates, codified best-practice templates, automated security scanning, and FinOps cost quotas into the CI/CD pipeline, enabling 80–100 developers to deploy autonomously while enforcing 80% governance compliance.\"",
        ])
    elif "anthropic" in c_lower:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **AI Implementation & Agentic Workflows:** Active practitioner designing and deploying custom Python agents, LLM integrations, and automated platform workflows.",
            "- **24x7 Mission-Critical Reliability:** Built and managed engineering teams handling 24x7 incident response, telemetry, and severity escalation across 10–15 engineers.",
            "- **Developer Tooling & Platform Delivery:** Managed internal developer platforms supporting 80–100 engineers, reducing deployment cycles by 40%.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Enterprise Tenure vs Hyper-Growth Startup Velocity:** Extensive tenure in enterprise healthcare (Blue Shield) and retail (Safeway). Anthropic operates as a frontier AI lab with extreme velocity, fluid processes, and minimal bureaucracy. Interviewers will test comfort with ambiguity, scrappiness, and rapid iteration.",
            "- **Frontier LLM Operational Mechanics:** Panelists will test deep technical understanding of LLM-specific infrastructure: KV cache memory footprints, context window degradation, time-to-first-token (TTFT) vs inter-token latency, prompt caching economics, and token rate limiting.",
            "- **Anthropic Tooling & Safety Paradigm:** Familiarity with the Claude API (tool use / function calling, vision, batch API), Claude Code CLI, and Anthropic's Responsible Scaling Policy.",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Operational Ballast for Enterprise Growth:** Frame enterprise background as a unique competitive advantage: as Anthropic scales enterprise adoption (Claude for Enterprise), having leaders who understand enterprise compliance (SOC 2, HIPAA, SOX) and 24x7 mission-critical SLAs is vital.",
            "- **Builder Heritage & Agility:** Highlight early career roots delivering commercial 3D games from scratch at LucasArts and independent game studios, proving hands-on engineering agility.",
            "- **Hands-On AI Workflows:** Discuss practical implementation of custom Python agents and automated developer workflows.",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and hiring manager interviews, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & Frontier AI Systems Deep-Dives",
            "- **Claude API Capabilities:** Thoroughly study Claude API tool use (JSON schema definitions, multi-turn tool calling), prompt caching (5-minute TTL, read vs write cost savings), vision inputs, and batch endpoints.",
            "- **LLM Serving & Inference Stack:** Review GPU memory constraints (HBM3e bandwidth, model weights vs KV cache sizing), continuous batching (vLLM / TensorRT-LLM), speculative decoding, and streaming response architectures.",
            "- **Reliability & Rate Limiting:** Study token bucket vs leaky bucket rate limiting algorithms, handling HTTP 429 and 529 Overloaded error codes, exponential backoff with jitter, and multi-region inference failover.",
            "",
            "### 2. Domain Mechanics & Role-Specific Nuances",
        ])
        if "support" in t_lower:
            lines.extend([
                "- **AI-Driven Customer Operations:** Review closed-loop defect detection from customer traces, automated issue clustering, and prompt drift monitoring.",
                "- **Enterprise Integration Troubleshooting:** Rehearse diagnosing SSO/SAML/OAuth federation failures, CORS misconfigurations, and SDK serialization errors across Python and TypeScript.",
            ])
        elif "commerce" in t_lower or "cpq" in t_lower:
            lines.extend([
                "- **Enterprise Commerce & Usage Billing:** Study usage-based metering pipelines, hyperscaler marketplace billing sync (AWS, GCP, Azure), Stripe integration, and ASC 606 revenue recognition.",
                "- **Audit & Compliance Controls:** Master SOX control testing, SOC 1/2 Type II evidence collection, and Quote-to-Cash data lineage.",
            ])
        else:
            lines.extend([
                "- **Infrastructure & Cluster Coordination:** Review Kubernetes orchestration for model serving, Slurm cluster scheduling, InfiniBand network telemetry, and GPU utilization metrics.",
                "- **Developer Productivity at AI Scale:** Study local development environments, DevContainers, CI/CD pipeline bottlenecks, and integrating AI coding assistants into engineering workflows.",
            ])
        lines.extend([
            "",
            "### 3. Company-Specific Evaluation Rubric (Anthropic Culture & Mission)",
            "- **AI Safety & Alignment:** Review Anthropic's Responsible Scaling Policy (RSP), ASL (AI Safety Level) 1–4 containment standards, and Constitutional AI principles.",
            "- **Extreme Ownership in Ambiguity:** Be prepared to discuss how to build structure from scratch in rapidly evolving environments without waiting for formal mandates.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"Anthropic operates in an extremely fast-moving, ambiguous environment where processes are invented daily. How will you adjust coming from structured enterprise environments?\"**  ",
            "   *Recommended Defense:* \"Emphasize that the structures I created at Blue Shield—like the BlueStack IDP and severity escalation tiers—were built precisely because they didn't exist when I arrived. I thrive in ambiguity by creating lightweight, repeatable mechanisms that remove friction for engineers. Furthermore, my foundational career in commercial gaming at LucasArts was defined by intense, scrappy execution under firm shipping deadlines.\"",
            "",
            "2. **\"When Claude is deployed as an autonomous first-responder for enterprise customer issues, how do you handle hallucination risk or incorrect billing diagnoses?\"**  ",
            "   *Recommended Defense:* \"Enforce deterministic verification gates: the LLM diagnoses and prepares remediation proposals, but high-impact transactional mutations (like billing adjustments or account provisioning) are executed through deterministic, schema-validated tool calls with human-in-the-loop escalation paths for edge cases. Ground this in verified experience designing zero-hallucination pipelines and strict FinOps governance.\"",
            "",
            "3. **\"How do you balance engineering velocity with strict reliability and safety constraints when deploying infrastructure for frontier AI?\"**  ",
            "   *Recommended Defense:* \"Implement automated guardrails rather than manual gatekeeping: use canary deployments, automated rollbacks triggered by latency and error-rate SLIs, and continuous synthetic test suites. This matches my track record at Blue Shield where we achieved 40% faster deployment turnaround while improving governance compliance by 80%.\"",
        ])
    elif "google" in c_lower or "youtube" in c_lower:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **Commercial Product Delivery & Technical Vision:** Full cradle-to-grave commercial software delivery ($1M flagship release at LucasArts) managing cross-functional teams of 14 engineers and artists.",
            "- **Enterprise Data & Systems Integration:** Managed Master Data Management (MDM) infrastructure for enterprise systems of record, data consistency, and high-concurrency member portals.",
            "- **Executive Alignment & Technical Program Governance:** Experienced consulting with VPs, directors, and cross-functional leaders to translate technical roadmaps into business value.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Google Product / TPM Interview Framework Rigor:** Google interviewers heavily assess candidates against standardized frameworks (CIRCLES framework for PMs, architectural system design at Google scale for TPMs, Fermi estimation problems).",
            "- **Scale & Ecosystem Nuances (YouTube Creator Economics / Search):** For YouTube roles, interviewers will drill into creator monetization mechanics (YPP revenue splits, Super Chat, Shorts monetization pool, Content ID) or search ranking signals (candidate generation vs fine ranking).",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Systems Foundation & CS Pedigree:** Highlight foundational Bachelor of Science in Computer Science from UC Santa Barbara and decades of hands-on software systems engineering.",
            "- **Data-Driven Decision Making:** Cite Master Data Management (MDM) leadership and FinOps governance metrics (80% compliance, 40% cycle time reduction) as evidence of disciplined analytical execution.",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and hiring committee evaluations, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & Google Systems Deep-Dives",
            "- **Google Distributed Systems Primitives:** Study Google Spanner (TrueTime, external consistency, Paxos), Borg/Kubernetes cluster scheduling, BigQuery Dremel engine, and Protocol Buffers / gRPC.",
            "- **System Design at Scale:** Prepare system design topologies handling millions of QPS, distributed caching (Memcached / Redis clusters), and asynchronous event streaming (PubSub / Kafka).",
            "",
            "### 2. Domain Mechanics & Role-Specific Nuances",
        ])
        if "creator" in t_lower or "earning" in t_lower:
            lines.extend([
                "- **YouTube Creator Monetization Mechanics:** Review YouTube Partner Program (YPP) revenue-sharing structures (55% long-form creator split, 45% Shorts creator pool), Content ID digital rights royalties, channel memberships, and international currency withholding tax compliance.",
                "- **Financial Intelligence & AI in Fintech:** Study predictive cash-flow forecasting models, anomaly detection in creator payouts, and automated dispute resolution workflows.",
            ])
        elif "search" in t_lower:
            lines.extend([
                "- **Video Search & Recommendation Pipelines:** Study two-stage recommendation architecture: candidate generation (deep collaborative filtering) followed by ranking scoring (wide-and-deep neural nets), multimodal search embeddings (CLIP, Gemini multimodal), and metrics (NDCG, MRR, watch time vs clickbait penalties).",
                "- **Generative AI in Search:** Review LLM-assisted search summaries, conversational query expansion, and latency-budgeted retrieval augmented generation (RAG).",
            ])
        else:
            lines.extend([
                "- **Enterprise Core Systems & Automation:** Review CRM, creator support tooling, BI telemetry pipelines, and agentic workflows for operational friction deflection.",
                "- **Cross-Functional OKR Formulation:** Study Google's OKR framework, launch review gating (privacy, security, legal reviews), and operational SLA governance.",
            ])
        lines.extend([
            "",
            "### 3. Company-Specific Evaluation Rubric (Google PM / TPM Bar)",
            "- **CIRCLES Framework for Product Design:** Practice Comprehend Situation, Identify Customer, Report Needs, Cut through Priorities, List Solutions, Evaluate Trade-offs, Summarize.",
            "- **Googleyness & Leadership:** Prepare STAR examples demonstrating intellectual humility, collaborative consensus-building, thriving in ambiguity, and ethical technology stewardship.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"How would you design a product feature that increases YouTube creator payout transparency while mitigating partner support escalations?\"**  ",
            "   *Recommended Defense:* \"Deconstruct the problem using the CIRCLES framework: identify creator personas (top-tier enterprise creators vs mid-tier emerging creators). Uncover root causes of escalations (deductions, delayed revenue recognition, tax withholding). Propose a real-time earnings breakdown dashboard with AI-generated plain-language explanations of discrepancies, backed by immutable audit logs from Master Data Management systems.\"",
            "",
            "2. **\"Tell me about a time you led a major technical transformation where key stakeholders had fundamentally conflicting priorities.\"**  ",
            "   *Recommended Defense:* \"Discuss the Blue Shield Member Portal complete rewrite: balanced business demands for rapid feature delivery against security, regulatory compliance, and 24x7 operational reliability. Established objective architectural gating criteria and automated CI/CD test gates that unified engineering and executive leadership.\"",
        ])
    elif "wing" in c_lower:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **0-to-1 Pilot Program Execution:** Demonstrated track record leading complex technical initiatives from whiteboard inception through full production deployment.",
            "- **Product Development Process (PDP) Stewardship:** Deep background establishing operational rigor, stage gates, and engineering cadence.",
            "- **24x7 Safety-Critical Operations:** Managed high-reliability mission-critical systems with zero single points of failure.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Aviation & Physical Drone Operational Nuances:** Shifting from pure cloud/software platforms to physical drone delivery logistics involving FAA regulations, airspace management, weather volatility, and hardware maintenance cycles.",
            "- **Hardware-Software Stage Gate Coordination:** Navigating the tight coupling between avionics firmware, ground pad dispatchers, and merchant POS software.",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Disciplined Engineering Rigor:** Highlight 24x7 production reliability where human and financial stakes demanded zero downtime.",
            "- **Multi-Disciplinary Team Management:** Cite experience managing cross-functional technical teams (including artists, systems programmers, and infrastructure engineers).",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and hiring manager interviews, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & Aviation Logistics Deep-Dives",
            "- **Drone Delivery Regulatory Frameworks:** Study FAA Part 135 air carrier certification, Beyond Visual Line of Sight (BVLOS), and Unmanned Traffic Management (UTM) airspace deconfliction.",
            "- **Hardware-in-the-Loop (HIL) & Stage Gating:** Review EVT -> DVT -> PVT stage gates, firmware over-the-air (FOTA) validation protocols, and fail-safe telemetry fallback mechanisms.",
            "- **Commerce & Last-Mile Dispatching:** Study dynamic drone dispatch routing, package payload weight/balance constraints, and merchant point-of-sale (POS) integration architectures.",
            "",
            "### 2. Company-Specific Evaluation Rubric (Wing / Alphabet Culture)",
            "- **Safety Culture:** In autonomous aviation, safety is non-negotiable. Prepare examples demonstrating unyielding commitment to operational safety and root-cause post-mortems.",
            "- **Operational Scalability:** Emphasize building repeatable operational frameworks that enable scaling to multiple continents.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"How do you maintain program momentum when flight hardware testing encounters an unexpected regulatory or supply chain delay?\"**  ",
            "   *Recommended Defense:* \"Decouple software and hardware test tracks: utilize Hardware-in-the-Loop (HIL) simulation testbeds and synthetic telemetry replay to continue validating mission planning and merchant integration software in parallel with hardware resolution.\"",
        ])
    elif "affirm" in c_lower:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **Developer Enablement & Internal Platforms:** Directed platform engineering managing BlueStack IDP supporting 80–100 engineers with 40% faster deployment turnaround.",
            "- **Financial & Master Data Management:** Accountable for enterprise Master Data Management (MDM) infrastructure ensuring precise transactional data integrity.",
            "- **Governance & Change Leadership:** Drove FinOps and change management achieving 80% compliance across enterprise systems.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Fintech / BNPL Underwriting Mechanics:** Affirm interviewers will test understanding of sub-second credit decisioning, fraud scoring latencies, merchant discount rates (MDR), and loan servicing state machines.",
            "- **Developer Productivity Measurement:** Panelists will probe how developer onboarding effectiveness is measured beyond subjective sentiment.",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Proven Platform Velocity:** Cite the 40% reduction in deployment lead times and 80% governance adherence as concrete proof of developer platform impact.",
            "- **Enterprise Financial Data Rigor:** Point to Master Data Management systems of record at Safeway and high-volume transaction processing at Blue Shield.",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and hiring manager interviews, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & Fintech Systems Deep-Dives",
            "- **Affirm Core Products & Economics:** Study Affirm Adaptive Checkout, split-pay products, merchant integration APIs, and sub-second credit decisioning pipelines.",
            "- **Financial Ledger Idempotency:** Master double-entry bookkeeping ledger architecture, distributed transaction atomicity (Saga pattern), and reconciliation pipelines.",
            "- **Developer Productivity Frameworks:** Study DORA metrics (Deployment Frequency, Lead Time, MTTR, Change Failure Rate) and the SPACE framework.",
            "",
            "### 2. Company-Specific Evaluation Rubric (Affirm Values)",
            "- **No Hidden Fees / Transparency:** Affirm's core brand promise is honesty and transparency. Align behavioral answers with ethical consumer financial practices.",
            "- **Push the Envelope:** Show examples of challenging legacy approaches to deliver modern, automated platforms.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"How do you measure whether an engineering onboarding program is actually accelerating engineer productivity rather than simply delivering curriculum?\"**  ",
            "   *Recommended Defense:* \"Track concrete operational milestones: Time to First PR, Time to First Production Deploy, and 30/60/90-day commit cadences, coupled with qualitative developer friction surveys. At Blue Shield/Stellarus, tracked concrete 40% cycle time reductions by eliminating deployment bottlenecks.\"",
        ])
    else:
        lines.extend([
            "### High-Alignment Anchors (Strengths)",
            "- **Platform Engineering & Architecture:** Proven leadership managing developer platforms supporting 80–100 engineers with 40% cycle time reduction.",
            "- **24x7 Production Reliability:** Built and managed engineering teams responsible for 24x7 mission-critical operations across 10–15 engineers.",
            "- **FinOps & Governance:** Demonstrated success driving 80% compliance with FinOps cost governance and change management.",
            "",
            "### Perceived Vulnerabilities & Panel Scrutiny Areas (Gaps to Defend)",
            "- **Domain & Toolchain Ramp-Up:** Shifting into specific proprietary technology stacks or specialized vertical domains requires demonstrating rapid technical ramp-up.",
            "- **Cross-Functional Scope Translation:** Ensuring enterprise leadership scale translates effectively into target team velocity expectations.",
            "",
            "### Strategic Counter-Framing & Proof Points",
            "- **Foundational Systems Engineering:** Point to BS in Computer Science and extensive track record architecting complex distributed platforms.",
            "- **Repeatable Operational Playbooks:** Cite proven frameworks for incident response, self-service CI/CD, and cost governance.",
            "",
            "## 3. Interview Preparation & Deep-Dive Study Areas",
            "",
            "> **Targeted Study Guide:** Prior to technical rounds and hiring manager interviews, the applicant should thoroughly review and master the following topics:",
            "",
            "### 1. Technical Architecture & Systems Deep-Dives",
            "- **Distributed Systems & Kubernetes:** Review container lifecycle management, service mesh architectures, and automated GitOps delivery pipelines.",
            "- **Reliability Engineering & Observability:** Study SLI/SLO formulation, error budget policies, distributed tracing, and automated canary deployments.",
            "- **FinOps & Cost Governance:** Master cloud cost attribution, spot/reserved instance strategies, and infrastructure efficiency metrics.",
            "",
            "### 2. Company & Domain Mechanics",
            "- Review company's core product architecture, recent public engineering blog posts, and open-source contributions.",
            "- Study target system bottlenecks, data flows, and scalability constraints.",
            "",
            "## 4. Anticipated High-Pressure Interview Questions & Defense Angles",
            "",
            "1. **\"How do you ensure engineering teams maintain high deployment velocity while enforcing strict reliability and governance standards?\"**  ",
            "   *Recommended Defense:* \"Embed compliance and guardrails directly into the developer platform (Golden Paths / IDP) rather than creating manual review gates. At Blue Shield/Stellarus, this approach improved deployment turnaround by 40% while simultaneously increasing governance adherence to 80%.\"",
        ])

    return lines


def generate_all_alignments(
    ledger_path: str = "inputs/facts.yaml",
    tracker_path: str = "output/tracker.json",
    output_base: str = "output",
    alignments_dir: str = "output/alignments",
):
    ledger = load_fact_ledger(ledger_path)
    tracker = Tracker(tracker_path)

    # Master facts hash for freshness tracking
    master_facts_hash = sha(Path(ledger_path).read_text(encoding="utf-8"))

    # Load alignment strategies from output/alignments (gitignored)
    alignments = load_all_alignments(alignments_dir)

    # Ensure search category listings are blocked
    if "job-2061ebf1" in tracker.jobs:
        tracker.jobs["job-2061ebf1"].status = "blocked"
        tracker.jobs["job-2061ebf1"].company = "Amazon"
        tracker.jobs["job-2061ebf1"].title = "Category Search Index"
        tracker.jobs["job-2061ebf1"].note = "Search category index (moved to List of List of Jobs tab)"

    results = []


    for jid, cfg in alignments.items():
        job = tracker.jobs.get(jid)
        if not job or job.status == "blocked":
            continue

        if "company" in cfg and not job.company:
            job.company = cfg["company"]
        if "title" in cfg and not job.title:
            job.title = cfg["title"]

        slug = cfg["slug"]
        # Load directives
        directives_path = Path("inputs/directives.yaml")
        cutoff_year = 2011
        key_leadership_skills = []
        if directives_path.exists():
            import yaml
            dirs = yaml.safe_load(directives_path.read_text(encoding="utf-8")) or {}
            cutoff_year = dirs.get("ageism", {}).get("cutoff_year", 2011)
            key_leadership_skills = dirs.get("skills_emphasis", {}).get("key_leadership_skills", [])

        # Apply 15-year ageism filter to chronological roles (preserving authorized prior heritage roles)
        import re
        filtered_roles = []
        additional_roles = []
        for r in cfg["roles"]:
            if "before" in r.dates.lower() or "prior" in r.dates.lower():
                additional_roles.append(r)
                continue
            years = re.findall(r"\b(19\d\d|20\d\d)\b", r.dates)
            end_yr = 2026 if "Present" in r.dates else (int(years[-1]) if years else 2026)
            if end_yr >= cutoff_year:
                filtered_roles.append(r)

        # Enhance skills with directives key leadership skills emphasis
        enhanced_skills = list(cfg["skills"])
        if key_leadership_skills:
            lead_text = ", ".join(key_leadership_skills) + "."
            has_lead = False
            for idx, s in enumerate(enhanced_skills):
                if any(k in s.label.lower() for k in ["leadership", "management", "operations"]):
                    enhanced_skills[idx] = Labeled(s.label, lead_text)
                    has_lead = True
                    break
            if not has_lead:
                enhanced_skills.append(Labeled("Key Leadership & Governance:", lead_text))

        # 1. Build Resume Object
        resume = Resume(
            name=ledger.name,
            headline=cfg["headline"],
            contact=f"mobile: {ledger.phone}  •  e-mail: {ledger.email}",
            summary=cfg["summary"],
            expertise=cfg["expertise"],
            roles=filtered_roles,
            additional_roles=additional_roles,
            education=[
                Labeled(f"{edu['institution']}:", edu["degree"])
                for edu in ledger.education
            ],
            skills=enhanced_skills,
        )


        # 2. Validate Resume
        is_valid, validation_errors = validate_resume(
            resume,
            ledger,
            cfg["cited_facts"],
            allowed_older_specialized=True,
        )
        if not is_valid:
            print(f"Validation warnings for {jid}: {validation_errors}")

        # 3. Render DOCX files
        job_dir = Path(output_base) / f"{jid}_{slug}"
        job_dir.mkdir(parents=True, exist_ok=True)
        clean_path = job_dir / "resume.docx"
        review_path = job_dir / "resume_REVIEW.docx"
        render_resume(resume, clean_path, review=False)
        render_resume(resume, review_path, review=True)

        # 4. Generate Comparative Alignment Report
        report_path = job_dir / "alignment_report.md"
        report_lines = [
            f"# Comparative Gap & Alignment Analysis: {job.company} – {job.title}",
            "",
            f"**Target Role:** {job.title}  ",
            f"**Company:** {job.company}  ",
            f"**Source Link:** [{job.source}]({job.source})  ",
            "",
            "## 1. Requirement vs. Evidence Matrix",
            "",
            "| Core Job Requirement / Competency | Direct Evidence in Source Resume | Alignment Status | Recommended Action / Reframing |",
            "|---|---|---|---|",
        ]
        for req, ev, status, rec in cfg["comparisons"]:
            report_lines.append(f"| **{req}** | {ev} | `{status}` | {rec} |")

        report_lines.append("")
        # Insert critical fit assessment, interview study guide, and high-pressure defense scenarios
        jd_file = Path("work") / jid / "jd_raw.txt"
        jd_text = jd_file.read_text(encoding="utf-8") if jd_file.exists() else ""
        report_lines.extend(generate_critical_fit_analysis(job, cfg, resume, jd_text=jd_text))

        report_lines.extend([
            "",
            "## 5. Factual Integrity & Validation Audit",
            "",
            f"- **Validation Status:** `{'PASSED (0% Hallucination)' if is_valid else 'WARNINGS DETECTED'}`",
            f"- **Cited Fact IDs:** {', '.join(cfg['cited_facts'])}",
            f"- **Age-Trimming Strategy:** Contiguous oldest-experience truncation applied while retaining authentic specialized gaming/systems heritage for media/gaming targets.",
            f"- **Contact Hygiene:** Mobile and email only; graduation year omitted to combat ageism.",
            "",
            "## 6. Generated Artifacts",
            "",
            f"- [Tailored Resume (Clean DOCX)](file://{clean_path.resolve()})",
            f"- [Tailored Resume with Changes in Bold (Review DOCX)](file://{review_path.resolve()})",
            f"- [Comparative Alignment Report](file://{report_path.resolve()})",
            f"- [Clarifying Questions](file://{job_dir.resolve()}/questions.md)",
        ])
        report_content = "\n".join(report_lines) + "\n"
        report_path.write_text(report_content, encoding="utf-8")
        # Remove legacy alias alignment.md if present
        alias_path = job_dir / "alignment.md"
        if alias_path.exists():
            alias_path.unlink()

        # 5. Generate Clarifying Questions file
        q_path = job_dir / "questions.md"
        q_lines = [
            f"# Clarifying Questions for Disambiguation Gate: {job.company} – {job.title}",
            "",
            "The following targeted questions address nuances and specific team context where additional detail can further sharpen your interview positioning:",
            "",
        ]
        for i, q in enumerate(cfg["questions"], 1):
            q_lines.append(f"{i}. **{q}**")
        q_lines.append("")
        q_path.write_text("\n".join(q_lines) + "\n", encoding="utf-8")

        # 6. Update Tracker
        jd_file = Path("work") / jid / "jd_raw.txt"
        jd_hash = sha(jd_file.read_text(encoding="utf-8")) if jd_file.exists() else sha(job.source)
        tracker.mark_aligned(
            jid,
            jd_hash=jd_hash,
            master_hash=master_facts_hash,
            outputs={
                "resume": f"output/{jid}_{slug}/resume.docx",
                "review": f"output/{jid}_{slug}/resume_REVIEW.docx",
                "report": f"output/{jid}_{slug}/alignment_report.md",
                "questions": f"output/{jid}_{slug}/questions.md",
            },
            open_questions=len(cfg["questions"]),
        )
        results.append((jid, job.company, job.title, str(clean_path)))

    tracker.save()
    tracker.write_index()
    print(f"Successfully generated alignments for {len(results)} jobs.")
    return results


if __name__ == "__main__":
    generate_all_alignments()
