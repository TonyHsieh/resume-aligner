"""Alignment configurations for Batch 5 target roles:
- Perplexity AI: Engineering Manager (Enterprise) (job-c8ae8308)
- Snout: Principal Software Engineer (job-ed329a2a)
- Together AI: Senior Software Engineer, Customer Insights (job-69f8cb02)
- Together AI: Solutions Architect (job-a0d42b13)
- Together AI: Senior Backend Engineer, Inference Platform (job-769b6b46)
- Together AI: Senior Product Engineer, Fullstack (job-d7eddd46)
- Together AI: Senior Product Engineer (job-87ee584c)
- Franklin Templeton: FTI Lead System Analyst (job-c711e11c)
- Franklin Templeton: Client Success Manager (job-c4be9bb5)
- Franklin Templeton: Head of AI Community (job-7f9d8d3e)
- Franklin Templeton: AI/ML Lead Engineer (job-5325e35d)
- Amazon / Ring: Senior Product Manager, Builder - Tech (job-f97df981)
- Amazon / AWS: Senior AI Acceleration Lead, Customer Success COE (job-ae23ccef)
- Amazon / AWS: Customer Solutions Manager, Media & Entertainment (job-3ca6b741)
- Amazon / AWS: Sr. Customer Solutions Manager, ISV & Private Equity (job-83cfc9b8)
- Amazon / AWS: Sr. PM-T, Customer Success Intelligence Team (job-153e4a94)
- Amazon: Principal PM-T, Growth, Outbound Communications (job-9153eb57)
"""

from typing import Any
from .model import Labeled, Role

BATCH_5_ALIGNMENTS: dict[str, dict[str, Any]] = {
    # 1. Perplexity AI - Engineering Manager (Enterprise)
    "job-c8ae8308": {
        "slug": "perplexity_em_enterprise",
        "company": "Perplexity AI",
        "title": "Engineering Manager (Enterprise)",
        "headline": "Engineering Manager | Enterprise Software & Cloud Platforms | High-Reliability Architecture, Governance & Applied AI",
        "summary": "**Enterprise engineering manager and platform leader** with extensive track record building and scaling secure enterprise platforms, developer toolchains, and mission-critical cloud integrations. Directed engineering teams operating the **BlueStack platform for 80–100 engineers**, led **24x7 high-reliability operations across 10–15 engineers**, achieved an **80% increase in FinOps and Change Management adherence**, and brings hands-on experience in **Python, custom AI agents, and enterprise compliance**.",
        "expertise": [
            "Enterprise Engineering Leadership & Team Mentorship",
            "Mission-Critical Cloud Platforms & Architecture (Azure / AWS)",
            "24x7 High-Reliability Production Operations & SLAs",
            "Enterprise Governance, FinOps & Security Compliance (80% gain)",
            "Developer Platforms & GitOps Automation (40% speedup)",
            "REST APIs, Middleware & Cross-System Integration",
            "Applied AI Tooling & Workflow Automation (Python, Copilot)",
            "Executive Stakeholder Consulting & Cross-Functional Alignment",
        ],
        "skills": [
            Labeled("Enterprise Platforms & Cloud:", "Internal Developer Platforms (Backstage), Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, MS Azure, AWS Serverless, Docker, SonarQube, Artifactory."),
            Labeled("Languages & Systems:", "Python, Rust, JavaScript, C, Java, Shell scripting, REST APIs, enterprise middleware, relational schemas, high-throughput systems."),
            Labeled("Databases & Data Integrity:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, data modeling, enterprise access controls."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Enterprise Engineering Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies for **80–100 internal developers and enterprise stakeholders**."),
                    Labeled("Scalable Platform Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Enterprise Transformation & Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy & Governance:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Operational Reliability & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                    Labeled("Enterprise Architecture & Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Leading engineering teams building enterprise software and customer solutions", "Managed enterprise platform teams supporting 80–100 engineers and led 24x7 operations across 10–15 engineers.", "Direct Match", "Direct match for enterprise engineering management and scale"),
            ("Enterprise governance, security compliance, and FinOps", "Drove 80% increase in FinOps and Change Management adherence; extensive regulatory compliance experience.", "Direct Match", "Verified governance and operational metrics"),
            ("Technical depth across cloud systems and applied AI workflows", "Hands-on engineering in Python, Rust, Kubernetes, GitOps, and custom Python AI agents.", "Direct Match", "Pragmatic technical depth paired with seasoned leadership"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How does the Enterprise engineering team collaborate with Enterprise Sales and InfoSec on SOC2, HIPAA, and custom tenant boundaries?",
            "What architectural patterns (e.g. single-tenant VPCs, BYOK, hybrid gateways) are prioritized for enterprise customers adopting Perplexity?",
            "What are the top performance and reliability SLAs demanded by enterprise customers today?",
        ],
    },

    # 2. Snout - Principal Software Engineer
    "job-ed329a2a": {
        "slug": "snout_principal_swe",
        "company": "Snout",
        "title": "Principal Software Engineer",
        "headline": "Principal Software Engineer | Full-Stack Web & Portals | Distributed Systems, Python/JavaScript, Payments & High Reliability",
        "summary": "**Principal full-stack software engineer and systems architect** with extensive track record setting technical direction, architecting scalable web platforms, and delivering mission-critical portal applications. Architected the **Blue Shield Member Portal rewrite**, scaled internal developer platforms for **80–100 engineers**, accelerated deployment turnaround by **40%**, and brings hands-on polyglot fluency in **Python, JavaScript, PostgreSQL, REST APIs, and automated cloud systems**.",
        "expertise": [
            "Full-Stack Web Architecture & Portal Modernization",
            "Distributed Systems, APIs & Transactional Data Flows",
            "Technical Direction, Architecture & Hands-on Coding",
            "Relational Database Modeling & PostgreSQL / MySQL",
            "High-Reliability Architecture (24x7 Mission-Critical SLAs)",
            "Cloud Platforms & DevOps Automation (Azure / AWS)",
            "Security, Data Integrity & Quality Safeguards",
            "Cross-Functional Product & Engineering Leadership",
        ],
        "skills": [
            Labeled("Programming & Web Platforms:", "Python, JavaScript, TypeScript/React fundamentals, HTML5, CSS, REST APIs, microservices, full-stack application development."),
            Labeled("Databases & Data Integrity:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, schema design, high-concurrency transactions."),
            Labeled("Cloud, Platforms & DevOps:", "MS Azure, AWS Serverless, Kubernetes, GitOps, GitHub Actions, Docker, CI/CD, SonarQube, Artifactory."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Architecture & Technical Direction:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Automated Cloud Systems:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Engineering:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Web Platform & Portal Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, modernizing web UI and transactional backend services."),
                    Labeled("24x7 Operational Rigor:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="(Concurrent) Independent Contractor",
                dates="April 1999 – November 2012",
                title="Full-Stack Engineer & Product Lead",
                bullets=[
                    Labeled("Commercial Web & Portal Development:", "**Engineered full-stack front-end (JavaScript, CSS) and backend services (PHP, MySQL, APIs)** for commercial high-concurrency interactive platforms and applications."),
                ],
            ),
        ],
        "comparisons": [
            ("Setting technical direction across web platforms, payments, and data systems", "Led technical architecture for Blue Shield Member Portal rewrite and managed platform architecture for 80–100 engineers.", "Direct Match", "Direct match for Principal Engineer scope and portal delivery"),
            ("Writing high-quality code daily in Python, JavaScript, and SQL", "Extensive hands-on engineering across Python, JavaScript, PostgreSQL, MySQL, and automated pipelines.", "Direct Match", "Verified polyglot technical depth"),
            ("Building for startup velocity while maintaining reliability and security", "Drove 40% deployment speedup and managed 24x7 high-reliability operations with zero compromise on quality.", "Direct Match", "Proven balance of high velocity and operational stability"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What payments gateway and recurring billing infrastructure (e.g. Stripe Billing) currently powers Snout's clinic wellness plans?",
            "How does Snout architect clinic-facing vs. pet-owner-facing portal surfaces to ensure seamless data synchronization?",
            "What are the top technical initiatives on the roadmap for scaling from tens of clinics to thousands?",
        ],
    },

    # 3. Together AI - Senior Software Engineer, Customer Insights
    "job-69f8cb02": {
        "slug": "together_ai_swe_customer_insights",
        "company": "Together AI",
        "title": "Senior Software Engineer, Customer Insights",
        "headline": "Senior Software Engineer | Customer Insights & Analytics Platforms | Python, Distributed Systems, Telemetry & Cloud Observability",
        "summary": "**Senior software and platform engineer** with deep experience building analytics pipelines, customer insights platforms, and automated developer tooling. Directed platform systems supporting **80–100 engineers**, accelerated deployment cycle times by **40%**, increased FinOps and governance adherence by **80%**, and brings hands-on proficiency in **Python, PostgreSQL, telemetry pipelines, and cloud systems**.",
        "expertise": [
            "Customer Insights & Usage Analytics Platforms",
            "Telemetry, Logging & Observability Architecture",
            "Distributed Systems & Data Pipelines (Python, SQL)",
            "Cloud Platforms & Serverless (AWS / Azure)",
            "High-Reliability Production Systems (24x7 SLAs)",
            "Relational Data Modeling & PostgreSQL / MySQL",
            "FinOps Governance & Cost Visibility (80% gain)",
            "Developer Velocity & CI/CD Automation (40% speedup)",
        ],
        "skills": [
            Labeled("Programming & Data:", "Python, JavaScript, Rust, C, Java, Shell scripting, REST APIs, data pipelines, schema modeling."),
            Labeled("Databases & Analytics:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, telemetry systems, usage metrics pipelines."),
            Labeled("Cloud & Platforms:", "AWS Serverless, MS Azure, Kubernetes, GitOps, GitHub Actions, Docker, SonarQube, Artifactory."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Analytics & Telemetry Operations:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Observability & Systems Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("FinOps Insights & Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Analytics & Automation:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Mission-Critical Reporting & Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Operational Telemetry:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Building customer insights, usage analytics, and telemetry pipelines", "Built usage tracking and FinOps governance platforms delivering 80% improvement in compliance and cost visibility.", "Direct Match", "Strong match for usage analytics and telemetry engineering"),
            ("Python proficiency and distributed systems data pipelines", "Extensive hands-on engineering in Python, PostgreSQL, MySQL, and automated pipelines.", "Direct Match", "Verified Python systems depth"),
            ("Operational excellence and high-scale reliability", "Managed 24x7 operations across 10–15 engineers and operated developer platforms for 80–100 engineers.", "Direct Match", "Proven high-scale reliability"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What data warehouse or streaming systems (e.g. ClickHouse, Snowflake, Kafka) power Together AI's customer insights pipeline?",
            "How does the Customer Insights team partner with Product and GTM on token usage anomaly detection?",
            "What are the target latency requirements for customer-facing usage dashboards vs. internal analytics?",
        ],
    },

    # 4. Together AI - Solutions Architect
    "job-a0d42b13": {
        "slug": "together_ai_solutions_architect",
        "company": "Together AI",
        "title": "Solutions Architect",
        "headline": "Solutions Architect | AI Infrastructure, Inference & Cloud Architecture | Enterprise Payer & Financial Systems Depth",
        "summary": "**Enterprise solutions architect and technologist** with deep experience designing scalable cloud solutions, integrating complex enterprise platforms, and consulting executive technical stakeholders. Implemented **BlueStack IDP for 80–100 engineers**, accelerated deployment turnaround by **40%**, drove an **80% increase in FinOps adherence**, and brings hands-on proficiency with **AI agent workflows, Python, cloud architectures, and enterprise security**.",
        "expertise": [
            "Enterprise Solutions Architecture & Technical Consulting",
            "AI Inference Infrastructure & Platform Integration",
            "Cloud Systems Architecture (Azure / AWS Serverless)",
            "Executive Technical Stakeholder Alignment & Roadmapping",
            "High-Reliability Architecture (24x7 Enterprise SLAs)",
            "FinOps Governance, TCO & Compute Optimization (80% gain)",
            "Security, Zero-Trust Access & Regulatory Compliance",
            "Developer Platforms & CI/CD Velocity (40% speed gain)",
        ],
        "skills": [
            Labeled("Architecture & Cloud:", "Solutions architecture, enterprise system modeling, MS Azure, AWS Serverless, Kubernetes, GitOps, Docker, microservices, REST APIs."),
            Labeled("AI, Automation & Tools:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, Gemini, n8n, Ansible, shell scripting."),
            Labeled("Databases & Middleware:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, enterprise middleware integration."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Solutions Consulting:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Architecture & Delivery:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Cloud Solutions Architecture:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Stakeholder Consultation:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Solutions Design:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Operational SLA Delivery:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Guiding enterprise customers in architecting AI and cloud infrastructure", "Decade of solutions architecture experience consulting executive stakeholders and leading cloud transformations.", "Direct Match", "Direct match for Solutions Architect consultative scope"),
            ("Deep understanding of compute optimization and FinOps", "Drove 80% increase in FinOps adherence and optimized cloud resource allocation across enterprise scale.", "Direct Match", "Verified FinOps and resource optimization impact"),
            ("Technical fluency in AI workflows and modern platform tooling", "Hands-on experience with Python, AI agents, Copilot, Codex, Ollama, and containerized deployment.", "Direct Match", "Grounded in verified technical ledger facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What are the most common architecture hurdles enterprise clients face when migrating from public cloud AI APIs to Together AI dedicated endpoints?",
            "How does the Solutions Architecture team assist customers with multi-region high availability and fallback inference routing?",
            "What reference architectures exist for integrating Together AI inference models with enterprise RAG pipelines?",
        ],
    },

    # 5. Together AI - Senior Backend Engineer, Inference Platform
    "job-769b6b46": {
        "slug": "together_ai_swe_inference_platform",
        "company": "Together AI",
        "title": "Senior Backend Engineer, Inference Platform",
        "headline": "Senior Backend Engineer | High-Throughput Inference & Cloud Platforms | Python, Rust, Kubernetes & High-Reliability Systems",
        "summary": "**High-performance backend and platform engineer** with extensive track record building distributed execution engines, high-reliability infrastructure, and automated developer tooling. Directed platform systems supporting **80–100 engineers**, accelerated deployment turnaround by **40%**, maintained 24x7 operations across **10–15 engineers**, and brings strong technical depth in **Python, Rust, C, Kubernetes, and low-latency systems**.",
        "expertise": [
            "High-Throughput Backend & Inference Platform Engineering",
            "Distributed Systems Architecture & Low-Latency Services",
            "Kubernetes & Container Orchestration (Azure / AWS)",
            "GitOps & CI/CD Automation (Kargo, ArgoCD, GitHub Actions)",
            "24x7 High-Reliability Operations & Incident Triage",
            "Polyglot Systems Engineering (Python, Rust, C, Java)",
            "Deployment Cycle Optimization (40% speed gain)",
            "Relational Data Tiers & Microservices Architecture",
        ],
        "skills": [
            Labeled("Languages & Systems:", "Python, Rust, C, Java, Shell scripting, Linux environment, REST APIs, microservices, 3D real-time systems."),
            Labeled("Platforms & Cloud Infrastructure:", "Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Backstage IDP, Docker, MS Azure, AWS Serverless, Atlantis/OpenTofu, SonarQube."),
            Labeled("Databases & Storage:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema design, high-availability data tiers."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Operations & Systems Engineering:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Kubernetes & GitOps Infrastructure:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation & Infrastructure as Code:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Mission-Critical Operational Rigor:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                    Labeled("Enterprise Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting major digital platform transition and rewrite."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Building high-throughput backend infrastructure for model inference", "Operated developer platforms for 80–100 engineers and built 24x7 high-reliability infrastructure.", "Direct Match", "Extensive track record delivering high-throughput backend platforms"),
            ("Kubernetes orchestration, container builds, and low-latency routing", "Deep hands-on architecture with Kubernetes, Docker, Azure, and automated GitOps pipelines.", "Direct Match", "Strong match for container orchestration and infrastructure"),
            ("Polyglot depth in Python, Rust, and systems languages", "Hands-on engineering in Python, Rust, C, and Java across enterprise platforms and real-time systems.", "Direct Match", "Polyglot technical depth verified in master facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How does Together AI's inference engine optimize batching and KV-cache management across heterogeneous GPU clusters?",
            "What distributed scheduling frameworks are utilized for model routing and load balancing under peak traffic?",
            "What are the target p99 latency SLAs for streaming text generation across flagship model tiers?",
        ],
    },

    # 6. Together AI - Senior Product Engineer, Fullstack
    "job-d7eddd46": {
        "slug": "together_ai_product_eng_fullstack",
        "company": "Together AI",
        "title": "Senior Product Engineer, Fullstack",
        "headline": "Senior Product Engineer | Full-Stack AI Products & Web Platforms | Python, JavaScript, Developer Experience & Cloud Infrastructure",
        "summary": "**Senior full-stack product engineer** with deep experience building user-facing web applications, developer portals, and automated backend platforms. Led digital portal modernization for the **Blue Shield Member Portal rewrite**, scaled developer portal tooling for **80–100 engineers**, accelerated deployment velocity by **40%**, and brings hands-on proficiency in **Python, JavaScript, PostgreSQL, REST APIs, and applied AI workflows**.",
        "expertise": [
            "Full-Stack Web & Product Engineering",
            "Developer Portals & User Experience (Backstage IDP)",
            "API Design & Transactional Backend Services",
            "Relational Database Architecture & PostgreSQL / MySQL",
            "Deployment Turnaround Acceleration (40% speedup)",
            "Cloud Platforms & Serverless (Azure / AWS)",
            "Applied AI Tooling & Workflow Automation (Python, Copilot)",
            "Cross-Functional Collaboration & Product Velocity",
        ],
        "skills": [
            Labeled("Full-Stack & Web:", "Python, JavaScript, TypeScript/React fundamentals, HTML5, CSS, REST APIs, full-stack application development, Backstage UI."),
            Labeled("Databases & Data Integrity:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, schema design, high-availability tiers."),
            Labeled("Cloud & DevOps:", "MS Azure, AWS Serverless, Kubernetes, GitOps, GitHub Actions, Docker, CI/CD, SonarQube."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Product & Platform Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Full-Stack Platform Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Product Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation & Infrastructure as Code:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal & Product Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, modernizing web UI self-service."),
                    Labeled("Operational Rigor & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                ],
            ),
            Role(
                company="(Concurrent) Independent Contractor",
                dates="April 1999 – November 2012",
                title="Full-Stack Engineer & Product Lead",
                bullets=[
                    Labeled("Full-Stack Product Delivery:", "**Engineered full-stack front-end (JavaScript, CSS) and backend services (PHP, MySQL, APIs)** for commercial high-concurrency interactive platforms and applications."),
                ],
            ),
        ],
        "comparisons": [
            ("Building end-to-end product features across web and backend tiers", "Led UI and backend rewrite for Blue Shield Member Portal and built full-stack developer portals for 80–100 engineers.", "Direct Match", "Extensive experience delivering scalable full-stack products"),
            ("Full-stack engineering in Python, JavaScript, and PostgreSQL", "Hands-on engineering across Python, JavaScript, PostgreSQL, MySQL, and automated cloud workflows.", "Direct Match", "Verified polyglot technical depth"),
            ("Fast iteration paired with production reliability", "Accelerated developer deployment turnaround by 40% while maintaining 24x7 enterprise operational reliability.", "Direct Match", "Demonstrated velocity and operational excellence"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How do Together AI product engineers partner with research to translate novel model capabilities into developer-facing console features?",
            "What is the frontend tech stack (e.g. Next.js, React) and state management pattern for Together AI's developer dashboard?",
            "What are the priority product experiments currently being run to improve self-serve developer activation and onboarding?",
        ],
    },

    # 7. Together AI - Senior Product Engineer
    "job-87ee584c": {
        "slug": "together_ai_senior_product_engineer",
        "company": "Together AI",
        "title": "Senior Product Engineer",
        "headline": "Senior Product Engineer | AI Developer Platforms & Web Applications | Full-Stack Systems, Python/JavaScript & High-Velocity Delivery",
        "summary": "**Senior product engineer and technologist** with extensive track record building intuitive developer tools, self-service portals, and scalable cloud systems. Implemented **BlueStack IDP for 80–100 engineers**, accelerating deployment times by **40%**, driving an **80% increase in FinOps and governance adherence**, and brings hands-on proficiency in **Python, JavaScript, PostgreSQL, REST APIs, and applied AI tooling**.",
        "expertise": [
            "Product Engineering & Developer Platform UX",
            "Full-Stack Web & Backend Systems (Python, JavaScript, SQL)",
            "Self-Service Developer Portals & Workflows (40% speed gain)",
            "Relational Database Architecture & PostgreSQL / MySQL",
            "Cloud Platforms & Container Infrastructure (Azure / AWS)",
            "Applied AI Workflows & Agentic Tooling (Python, Copilot)",
            "Production Safeguards, Governance & FinOps (80% gain)",
            "Cross-Functional Product Delivery & Technical Ownership",
        ],
        "skills": [
            Labeled("Product & Full-Stack:", "Python, JavaScript, TypeScript/React fundamentals, HTML5, CSS, REST APIs, full-stack application development, Backstage UI."),
            Labeled("Databases & Storage:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, schema design, high-availability tiers."),
            Labeled("Cloud & DevOps:", "MS Azure, AWS Serverless, Kubernetes, GitOps, GitHub Actions, Docker, CI/CD, SonarQube."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Product Engineering:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Platform Architecture & Automation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Product Velocity & Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation Solutions & Strategy:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, modernizing web UI self-service."),
                    Labeled("Operational Rigor & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Designing and shipping developer-facing product features", "Built developer platform products supporting 80–100 engineers with 40% velocity improvement.", "Direct Match", "Direct match for developer product engineering"),
            ("Technical depth in Python, JavaScript, and cloud systems", "Hands-on engineering across Python, JavaScript, PostgreSQL, MySQL, and automated pipelines.", "Direct Match", "Verified polyglot technical depth"),
            ("High product ownership and velocity", "Led cradle-to-grave delivery across enterprise digital transformations and commercial platforms.", "Direct Match", "Demonstrated full-lifecycle product ownership"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What are the key developer onboarding funnels Together AI is optimizing this quarter?",
            "How does Together AI gather and prioritize feedback from AI developers and startup founders?",
            "What are the top UI/UX challenges when visualizing model performance, latency, and token consumption?",
        ],
    },

    # 8. Franklin Templeton - FTI Lead System Analyst
    "job-c711e11c": {
        "slug": "franklin_templeton_lead_system_analyst",
        "company": "Franklin Templeton",
        "title": "FTI Lead System Analyst",
        "headline": "Lead System Analyst | Enterprise Systems & Integration Architecture | Cloud Migration, FinOps & Regulatory Governance",
        "summary": "**Lead system analyst and enterprise integration architect** with extensive background analyzing complex business workflows, designing scalable middleware patterns, and directing enterprise system modernizations. Led architecture for the **Blue Shield Member Portal rewrite**, scaled cloud developer platforms for **80–100 engineers**, achieved an **80% increase in FinOps and Change Management adherence**, and brings deep expertise in **relational databases, SQL, system modeling, and regulatory compliance**.",
        "expertise": [
            "Lead Systems Analysis & Enterprise Architecture",
            "Business Workflow Modeling & Requirements Synthesis",
            "Middleware & Enterprise Integration (APIs, WebLogic, SQL)",
            "Cloud Transformation & FinOps Governance (80% gain)",
            "Data Modeling & Relational Integrity (Oracle, PostgreSQL)",
            "Change Leadership & Regulatory Compliance",
            "Executive Stakeholder Consulting & Cross-Functional Alignment",
            "High-Reliability Production Systems (24x7 SLAs)",
        ],
        "skills": [
            Labeled("Systems Analysis & Architecture:", "Enterprise systems analysis, business workflow modeling, requirements gathering, system specification, data flow diagrams, REST APIs, enterprise middleware."),
            Labeled("Databases & Data Modeling:", "Oracle PL/SQL, SQL, Transact-SQL, PostgreSQL, MySQL, DynamoDB, Microsoft Access, data integrity, reporting requirements."),
            Labeled("Cloud Platforms & DevOps:", "MS Azure, AWS Serverless, Kubernetes, GitOps, Backstage IDP, GitHub Actions, Docker, CI/CD, SonarQube."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Systems Analysis & Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, analyzing developer workflow requirements, and supporting toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Architecture & Governance:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Enterprise Analysis & FinOps Adherence:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Systems Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Major System Analysis & Rewrite:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal, synthesizing complex business rules."),
                    Labeled("24x7 Operational Reliability:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Integration Transformation:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Leading complex systems analysis and enterprise modernization programs", "Led technical analysis and architecture for Blue Shield Member Portal rewrite and enterprise cloud migrations.", "Direct Match", "Direct match for Lead System Analyst scope and enterprise rigor"),
            ("Translating business requirements into technical integration specifications", "Partnered across matrixed business organizations driving 80% improvement in Change Management and governance.", "Direct Match", "Demonstrated requirements synthesis and cross-functional leadership"),
            ("Data modeling and SQL depth across enterprise relational systems", "Deep expertise in Oracle PL/SQL, SQL, PostgreSQL, and Transact-SQL across financial and healthcare systems.", "Direct Match", "Backed by verified database ledger facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What core investment management systems and trading platforms are within scope for this modernization initiative?",
            "How does the Systems Analysis team interface with enterprise data governance and financial audit teams?",
            "What architectural patterns are standardized for connecting legacy on-prem transactional engines with cloud analytics tiers?",
        ],
    },

    # 9. Franklin Templeton - Client Success Manager
    "job-c4be9bb5": {
        "slug": "franklin_templeton_client_success_mgr",
        "company": "Franklin Templeton",
        "title": "Client Success Manager",
        "headline": "Client Success & Relationship Leader | Enterprise Financial Technology & Cloud Platforms | Stakeholder Alignment & Operational SLAs",
        "summary": "**Client success and enterprise technology leader** with extensive track record managing enterprise stakeholder relationships, driving technology platform adoption, and ensuring mission-critical operational SLAs. Supported **80–100 internal developers and stakeholders** on the BlueStack IDP, drove an **80% increase in FinOps and governance adherence**, managed **24x7 operations across 10–15 engineers**, and brings strong consultative communication.",
        "expertise": [
            "Enterprise Client Success & Relationship Management",
            "Platform Adoption & User Onboarding (80–100 stakeholders)",
            "Executive Stakeholder Consulting & Communication",
            "24x7 Mission-Critical Operational SLAs & Incident Escalations",
            "Change Leadership & FinOps Governance (80% gain)",
            "Cross-Functional Delivery (Product, Tech, Operations)",
            "Vendor Management & Contract Negotiation",
            "Business Process Improvement & Value Realization",
        ],
        "skills": [
            Labeled("Client Success & Consulting:", "Client relationship management, executive stakeholder consulting, customer onboarding, adoption roadmaps, value realization, training documentation, SLA management."),
            Labeled("Enterprise Systems & Governance:", "FinOps governance, Change Leadership, regulatory compliance, risk mitigation, business workflow analysis."),
            Labeled("Platforms & Technology Context:", "Internal Developer Platforms (Backstage), cloud infrastructure, MS Azure, AWS Serverless, REST APIs, enterprise reporting, SQL."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Stakeholder Management & Platform Adoption:", "**Managing platform operations and stakeholder consultation supporting 80–100 internal developers and business users**, ensuring high adoption and operational satisfaction."),
                    Labeled("Delivery Excellence:", "**Directing platform architecture and operational reliability** to ensure consistent, friction-free service delivery across enterprise groups."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Value Delivery & Governance Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving delivery turnaround by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Stakeholder Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align technology adoption with strategic business outcomes."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Operational SLA Commitment:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident management."),
                    Labeled("Major Program Delivery:", "**Accountable for end-to-end infrastructure execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization Delivery:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern Oracle WebLogic and Database architecture, driving consistent delivery across business units."),
                ],
            ),
        ],
        "comparisons": [
            ("Managing strategic client relationships and driving platform adoption", "Directed platform adoption for 80–100 stakeholders and led enterprise solution delivery across retail and healthcare.", "Direct Match", "Direct match for client success and stakeholder management"),
            ("Delivering on operational SLAs and resolving escalations", "Led 24x7 mission-critical operations with formal severity escalation tiers across 10–15 engineers.", "Direct Match", "Demonstrated operational rigor and client commitment"),
            ("Executive stakeholder communication and consultative value realization", "Decade of consulting senior leadership on digital transformation, FinOps, and change management.", "Direct Match", "Backed by verified governance and consulting facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "What enterprise client segments (institutional investors, wealth managers, internal business units) are supported by this Client Success group?",
            "What KPIs (e.g. Net Retention, platform adoption rate, escalation turnaround) define success for this role?",
            "How does Client Success collaborate with Product and Engineering to close the loop on feature requests and client friction points?",
        ],
    },

    # 10. Franklin Templeton - Head of AI Community
    "job-7f9d8d3e": {
        "slug": "franklin_templeton_head_of_ai_community",
        "company": "Franklin Templeton",
        "title": "Head of AI Community",
        "headline": "Head of AI Community & Technology Enablement | AI Implementation, Change Leadership & Enterprise Adoption | Platform Engineering Depth",
        "summary": "**AI community, enablement, and technology leader** with extensive track record championing technology adoption, driving cross-functional change leadership, and scaling internal platforms across enterprise organizations. Successfully drove an **80% increase in Change Management and governance adherence**, scaled developer platforms for **80–100 engineers**, and actively champions **responsible applied AI workflows, agentic automation, and community enablement**.",
        "expertise": [
            "AI Community Leadership & Enterprise Enablement",
            "Change Leadership & Technology Adoption Frameworks",
            "Responsible AI Implementation & Governance (80% gain)",
            "Applied AI & Agentic Workflow Tooling (Python, Copilot)",
            "Developer Experience & Internal Platforms (80–100 users)",
            "Executive Stakeholder Consulting & Educational Roadmaps",
            "Cross-Functional Community Building (Business, Tech, Data)",
            "Hackathons, Best-Practice Playbooks & Knowledge Sharing",
        ],
        "skills": [
            Labeled("AI Enablement & Community:", "AI community leadership, change leadership, technology evangelism, developer enablement, hackathons, best-practice playbooks, user education, responsible AI governance."),
            Labeled("AI Tools & Applied Automation:", "OpenAI Codex, GitHub Copilot, Ollama, Gemini, OpenCode, Hermes, custom Python AI agents, workflow automation (n8n), prompt design."),
            Labeled("Enterprise Platforms & Governance:", "Internal Developer Platforms (Backstage), cloud infrastructure (Azure / AWS), FinOps governance, regulatory compliance, HIPAA/financial controls."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Community & Platform Leadership:", "**Managing engineering and enablement operations for BlueStack IDP**, fostering developer community best practices and toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Platform Capabilities:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Change Leadership & Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Enablement:", "**Gathered business requirements and partnered across internal cross-functional organizations** to drive adoption of automated workflows, modern tooling, and operational governance."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Modernization Leadership:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("Team Coaching & Development:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Architecture & Standards:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern Oracle WebLogic and Database architecture, establishing technical standards across engineering teams."),
                ],
            ),
        ],
        "comparisons": [
            ("Building and scaling enterprise AI communities and adoption programs", "Decade of experience leading change management, standardizing technical best practices, and driving platform adoption.", "Direct Match", "Direct match for Head of Community and technology enablement"),
            ("Driving governance, responsible adoption, and change leadership", "Drove an 80% increase in FinOps and Change Management adherence; established enterprise architectural standards.", "Direct Match", "Backed by verified governance and change leadership metrics"),
            ("Hands-on familiarity with modern AI tools and agentic workflows", "Hands-on implementation of custom Python agents, Copilot, Codex, Ollama, Gemini, and workflow automation.", "Direct Match", "Grounded in verified master facts and hands-on exploratory tooling"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "What executive forums and cross-functional working groups currently govern Franklin Templeton's enterprise AI initiatives?",
            "What incentives, hackathons, or recognition programs are planned to accelerate grassroots AI adoption among investment and ops professionals?",
            "How does the AI Community team collaborate with InfoSec and Compliance to ensure safe experimentation with frontier LLMs?",
        ],
    },

    # 11. Franklin Templeton - AI/ML Lead Engineer
    "job-5325e35d": {
        "slug": "franklin_templeton_ai_ml_lead_engineer",
        "company": "Franklin Templeton",
        "title": "AI/ML Lead Engineer",
        "headline": "AI/ML Lead Engineer | Enterprise AI Platforms, MLOps & Distributed Infrastructure | Python, Cloud Platforms & Automated SDLC",
        "summary": "**AI/ML lead engineer and platform architect** with extensive background directing distributed systems, machine learning platform capabilities, and automated cloud workflows. Implemented the **BlueStack platform supporting 80–100 engineers**, accelerated deployment cycle times by **40%**, maintained 24x7 operations across **10–15 engineers**, and brings hands-on proficiency in **Python, custom AI agents, Kubernetes, GitOps, and enterprise data tiers**.",
        "expertise": [
            "AI/ML Platform Engineering & MLOps Infrastructure",
            "Distributed Systems Architecture & Model Serving",
            "Applied AI & Agentic Workflows (Python, Codex, Copilot)",
            "Kubernetes & Cloud Infrastructure (Azure / AWS Serverless)",
            "GitOps & CI/CD Deployment Automation (40% speed gain)",
            "Relational Data Tiers & SQL (PostgreSQL, Oracle PL/SQL)",
            "High-Reliability Architecture (24x7 Mission-Critical SLAs)",
            "FinOps Governance & Compute Cost Optimization (80% gain)",
        ],
        "skills": [
            Labeled("AI, MLOps & Systems:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, Gemini, OpenCode, Hermes, MLOps pipelines, REST APIs, microservices."),
            Labeled("Cloud Platforms & Kubernetes:", "Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Backstage IDP, Docker, MS Azure, AWS Serverless, Atlantis/OpenTofu, SonarQube."),
            Labeled("Databases & Data Integrity:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, schema modeling, high-availability tiers."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Engineering Leadership:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Kubernetes & Scalable Infrastructure:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & FinOps Optimization:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Automation:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Modernization & Reliability:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Operational SLA Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Leading AI/ML platform engineering and model deployment pipelines", "Built and operated cloud developer platforms supporting 80–100 engineers with 40% deployment speedup.", "Direct Match", "Direct match for AI/ML platform engineering and MLOps tooling"),
            ("Kubernetes orchestration and high-reliability cloud infrastructure", "Deep hands-on architecture with Kubernetes, Azure, AWS, and driving 80% adherence in governance.", "Direct Match", "Proven cloud infrastructure and container orchestration depth"),
            ("Hands-on Python systems depth and agentic AI tooling", "Hands-on engineering with custom Python agents, Codex, Copilot, Ollama, Gemini, and automated CI/CD.", "Direct Match", "Authentic technical grounding in modern AI tooling and systems"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "What model serving and orchestration frameworks (e.g. vLLM, Triton, Ray, custom Kubernetes controllers) are standardized at Franklin Templeton?",
            "How does the AI/ML engineering team partner with Quantitative Research on feature stores and backtesting data pipelines?",
            "What automated evaluation and guardrail frameworks are integrated into model deployment pipelines for financial regulatory compliance?",
        ],
    },

    # 12. Amazon / Ring - Senior Product Manager, Builder - Tech
    "job-f97df981": {
        "slug": "amazon_sr_pm_builder_ring",
        "company": "Amazon / Ring",
        "title": "Senior Product Manager, Builder - Tech, Ring",
        "headline": "Senior Product Manager - Technical | AI-Native Devices & Developer Platforms | Hardware/Software Systems & Digital Transformation",
        "summary": "**Technical product manager and engineering leader** with extensive track record directing developer platforms, digital transformation, and mission-critical software systems. Led platform product delivery for the **BlueStack IDP supporting 80–100 engineers**, accelerating deployment cycle times by **40%**, driving an **80% increase in FinOps and governance adherence**, and actively builds **AI-native workflows and agentic prototypes in Python**.",
        "expertise": [
            "Technical Product Management & Product Roadmaps",
            "AI-Native Product Definition & GenAI Integrations",
            "Developer Experience & Productivity Platforms (40% speedup)",
            "Cross-Functional Collaboration (Hardware, Firmware, Cloud)",
            "Data-Driven Product Strategy & FinOps Governance (80% gain)",
            "Iterative Prototyping & Technical Architecture",
            "User Journey Mapping & Digital Self-Service Portals",
            "Executive Stakeholder Consulting & Working Backwards",
        ],
        "skills": [
            Labeled("Product Management & Strategy:", "Technical product strategy, PRDs, roadmaps, Working Backwards, user journey mapping, data-driven flywheels, feature prioritization, customer telemetry."),
            Labeled("AI, Prototyping & Software:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, Gemini, REST APIs, SQL, schema modeling, rapid prototyping."),
            Labeled("Cloud Platforms & Systems:", "MS Azure, AWS Serverless, Kubernetes, Backstage IDP, Docker, FinOps adherence, Change Leadership, high-reliability architecture."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Product Leadership:", "**Managing engineering and platform product delivery for BlueStack IDP**, directing feature roadmaps, developer toolchains, and automated workflows supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Scalable System Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Governance Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment cycle times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Product Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align product strategy, increase governance, and optimize operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, elevating digital self-service."),
                    Labeled("Operational Reliability & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident management."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Technical product management for AI-native builder platforms", "Directed product roadmaps for BlueStack developer platform for 80–100 engineers with 40% velocity improvement.", "Direct Match", "Direct match for technical product manager builder scope"),
            ("Cross-functional leadership across software, cloud, and systems", "Led cross-functional teams spanning engineering, operations, security, and product for digital transformations.", "Direct Match", "Demonstrated Amazon Working Backwards and cross-functional leadership"),
            ("Applied AI experimentation and rapid prototyping", "Hands-on exploration building custom Python agents, evaluating Copilot and Codex, and designing automated workflows.", "Direct Match", "Pragmatic, builder-first technical perspective grounded in facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How does the Ring Builder team balance on-device edge AI processing constraints with cloud GenAI capabilities?",
            "What telemetry and user engagement metrics are most indicative of product-market fit for Ring's AI-enabled features?",
            "How does the team navigate privacy, trust, and responsible AI principles in consumer home security products?",
        ],
    },

    # 13. Amazon / AWS - Senior AI Acceleration Lead, Customer Success COE
    "job-ae23ccef": {
        "slug": "aws_sr_ai_acceleration_lead",
        "company": "Amazon / AWS",
        "title": "Senior AI Acceleration Lead, Customer Success COE, AWS Specialist Organization",
        "headline": "Senior AI Acceleration & Customer Success Leader | Enterprise Cloud Transformation, AI Adoption & FinOps | AWS Specialist Org",
        "summary": "**Senior AI acceleration and customer success leader** with extensive track record accelerating enterprise technology adoption, guiding executive stakeholders through digital transformation, and scaling cloud platforms. Implemented **BlueStack IDP for 80–100 engineers**, accelerated deployment turnaround by **40%**, drove an **80% increase in FinOps and Change Management adherence**, and brings deep expertise in **applied AI implementation, cloud governance, and consultative delivery**.",
        "expertise": [
            "Enterprise AI Acceleration & Adoption Strategy",
            "Customer Success Center of Excellence (COE) Leadership",
            "Executive Stakeholder Consulting & Value Realization",
            "Cloud Transformation & Migration (AWS Serverless / Azure)",
            "FinOps Governance, TCO & Cloud Economics (80% gain)",
            "Change Leadership & Technology Enablement",
            "Responsible AI Implementation & Risk Governance",
            "Cross-Functional Program Execution & Scale",
        ],
        "skills": [
            Labeled("AI Acceleration & Consulting:", "AI acceleration strategy, customer success COE, executive stakeholder consulting, cloud adoption frameworks, value realization, change management, training playbooks."),
            Labeled("Cloud Platforms & Architecture:", "AWS Serverless, MS Azure, Kubernetes, GitOps, Backstage IDP, Docker, REST APIs, enterprise middleware."),
            Labeled("AI Tools & Automation:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, Gemini, n8n, automated delivery pipelines."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Enablement & Acceleration:", "**Managing engineering and enablement operations for BlueStack IDP**, directing technology acceleration and supporting toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Scalable Cloud Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Enterprise Acceleration & FinOps:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Stakeholder Advisory & Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align technology adoption with strategic business outcomes."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Large-Scale Enterprise Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Operational SLA Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization & Delivery:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Leading enterprise AI acceleration and customer success initiatives", "Decade of leadership consulting enterprise executives on cloud adoption, platform acceleration, and governance.", "Direct Match", "Direct match for AI Acceleration Lead and Customer Success scope"),
            ("Deep FinOps governance and economic value realization", "Achieved 80% improvement in FinOps and Change Management adherence; extensive budget and vendor oversight.", "Direct Match", "Backed by verified FinOps and governance metrics"),
            ("Technical fluency across AWS and enterprise AI capabilities", "Deep architecture experience in cloud systems, AWS Serverless, AI agent tooling, and enterprise integration.", "Direct Match", "Grounded in verified technical ledger facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How does the Customer Success COE partner with AWS Account Teams and Specialist Solution Architects during early AI pilot phases?",
            "What standardized acceleration frameworks (e.g. AWS GenAI Jumpstart, workshops) have driven the highest conversion from PoC to production?",
            "What are the common organizational roadblocks enterprise customers face when scaling generative AI applications across regulated business units?",
        ],
    },

    # 14. Amazon / AWS - Customer Solutions Manager, Media & Entertainment, TMEGS
    "job-3ca6b741": {
        "slug": "aws_csm_media_entertainment",
        "company": "Amazon / AWS",
        "title": "Customer Solutions Manager, Media & Entertainment, TMEGS",
        "headline": "Customer Solutions Manager | Media, Entertainment & Gaming Heritage | Enterprise Cloud Delivery, Architecture & Executive Alignment",
        "summary": "**Customer solutions and technology delivery leader** with authentic background in interactive media and entertainment (Hasbro, Universal Music, virtual worlds) combined with 15+ years directing enterprise cloud transformations and platform engineering. Led platform delivery for **80–100 engineers**, accelerated deployment velocity by **40%**, managed **24x7 operations across 10–15 engineers**, and excels at aligning executive technical leaders with strategic cloud outcomes.",
        "expertise": [
            "Enterprise Customer Solutions Management & Delivery",
            "Media, Entertainment & Interactive Systems Heritage",
            "Cloud Transformation & Migration Programs (AWS / Azure)",
            "Executive Stakeholder Consulting & Strategic Roadmaps",
            "24x7 Mission-Critical Operational SLAs & Reliability",
            "FinOps Governance, TCO & Cloud Economics (80% gain)",
            "Cross-Functional Delivery (Sales, Architecture, Eng)",
            "Contract Negotiation, Vendor Management & Budgeting",
        ],
        "skills": [
            Labeled("Customer Solutions & Delivery:", "Customer solutions management, executive stakeholder consulting, cloud migration programs, governance frameworks, statement of work, delivery roadmaps."),
            Labeled("Media & Interactive Systems:", "Real-time virtual worlds, digital media platforms, MMO architecture, real-time networking, full-stack web/API delivery for major brands (Universal Music, Hasbro)."),
            Labeled("Cloud Platforms & DevOps:", "AWS Serverless, MS Azure, Kubernetes, GitOps, Backstage IDP, Docker, REST APIs, CI/CD automation."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Delivery & Customer Solutions:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Cloud Architecture & Automation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Enterprise Modernization & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Executive Stakeholder Partnership:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align technology adoption with strategic business outcomes."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Mission-Critical Program Execution:", "**Accountable for end-to-end infrastructure design and execution plan** supporting major digital platform transition and rewrite."),
                    Labeled("24x7 Operational SLA Delivery:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                ],
            ),
            Role(
                company="(Concurrent) Independent Contractor",
                dates="April 1999 – November 2012",
                title="Game Designer, Project Lead, Game Developer",
                bullets=[
                    Labeled("Media & Interactive Entertainment Delivery:", "**Created commercial game designs and interactive products for major enterprise brands including Hasbro and Universal Music**, directing full lifecycle delivery from concept through production."),
                    Labeled("Scalable Media Platforms:", "**Architected and implemented browser-based Flash social and music-oriented MMO (Planet Cazmo)** with real-time networking and high-concurrency player interactions."),
                ],
            ),
        ],
        "comparisons": [
            ("Managing strategic media, entertainment, and gaming customer accounts", "Authentic interactive media delivery heritage (Universal Music, Hasbro, MMO platform) combined with 15+ years of enterprise cloud delivery.", "Direct Match", "Unique combination of authentic media heritage and enterprise cloud delivery"),
            ("Leading multi-million dollar cloud transformations and migration programs", "Accountable for large-scale enterprise rewrites, managing 10–15 engineers on 24x7 SLAs, and driving 80% FinOps adherence.", "Direct Match", "Proven executive program delivery and financial governance"),
            ("AWS cloud fluency and consultative technical depth", "Deep architecture experience in cloud systems, AWS Serverless, microservices, and container platforms.", "Direct Match", "Grounded in verified technical ledger facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_game_03", "fact_game_04"],
        "questions": [
            "What major media and entertainment workloads (e.g. cloud rendering, virtual production, streaming media pipelines) represent the highest growth areas for TMEGS?",
            "How does the Customer Solutions Manager coordinate with AWS Professional Services and partner SIs on multi-year migration deliverables?",
            "What are the typical governance and cost optimization reviews conducted with media executive sponsors?",
        ],
    },

    # 15. Amazon / AWS - Sr. Customer Solutions Manager, ISV Industry & Private Equity
    "job-83cfc9b8": {
        "slug": "aws_csm_isv_pe",
        "company": "Amazon / AWS",
        "title": "Sr. Customer Solutions Manager, ISV Industry & Private Equity",
        "headline": "Sr. Customer Solutions Manager | ISV & Private Equity Portfolio Acceleration | Cloud Migration, FinOps & Value Realization",
        "summary": "**Senior customer solutions and cloud transformation leader** with extensive track record partnering with C-suite stakeholders, private equity portfolio executives, and software organizations to accelerate cloud modernization. Led platform delivery for **80–100 engineers**, accelerated deployment cycle times by **40%**, achieved an **80% increase in FinOps and Change Management adherence**, and brings deep expertise in **cloud economics, governance, and consultative delivery**.",
        "expertise": [
            "ISV & Private Equity Portfolio Solutions Delivery",
            "Executive C-Suite Stakeholder Consulting & Strategic Alignment",
            "Cloud Transformation & Enterprise Modernization (AWS / Azure)",
            "FinOps Governance, TCO Reduction & Cloud Economics (80% gain)",
            "Deployment Velocity & Time-to-Market Acceleration (40% speedup)",
            "Contract Negotiation, Vendor Oversight & Budgeting",
            "Cross-Functional Delivery (Sales, ProServe, Partners)",
            "Risk Mitigation, Compliance & Operational SLAs",
        ],
        "skills": [
            Labeled("Solutions Management & Consulting:", "Customer solutions management, executive stakeholder consulting, ISV product acceleration, PE portfolio value creation, cloud migration roadmaps, statement of work."),
            Labeled("Cloud Economics & FinOps:", "FinOps governance, TCO optimization, cloud migration business cases, budget management, Change Leadership, risk governance."),
            Labeled("Cloud Platforms & Architecture:", "AWS Serverless, MS Azure, Kubernetes, GitOps, Backstage IDP, Docker, REST APIs, enterprise middleware."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Program Delivery:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Scalable System Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Portfolio Transformation & FinOps Adherence:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Executive Stakeholder Partnership:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align technology adoption with strategic business outcomes."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Major Program Execution:", "**Accountable for end-to-end infrastructure design and execution plan** supporting major digital platform transition and rewrite."),
                    Labeled("24x7 Operational SLA Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization Delivery:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Consulting private equity portfolio executives and ISVs on cloud acceleration", "Decade of consulting senior leadership on technology roadmaps, platform acceleration, and governance.", "Direct Match", "Direct match for ISV and PE customer solutions leadership"),
            ("Driving rapid cloud economics, FinOps, and cost optimization", "Achieved an 80% improvement in FinOps adherence and accelerated delivery turnaround by 40%.", "Direct Match", "Proven quantitative impact on cloud economics and velocity"),
            ("High-stakes enterprise program delivery and governance", "Led 24x7 mission-critical operations and large-scale digital portal modernization.", "Direct Match", "Backed by verified enterprise operational facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How does the ISV & PE CSM team coordinate with Private Equity operating partners during due diligence and post-acquisition cloud integration?",
            "What playbooks are utilized to help SaaS portfolio companies migrate from on-prem or single-tenant hosting to modern multi-tenant AWS architectures?",
            "What KPIs are tracked to quantify value creation and ARR expansion across PE accounts?",
        ],
    },

    # 16. Amazon / AWS - Sr. PM-T, Customer Success Intelligence Team
    "job-153e4a94": {
        "slug": "aws_sr_pm_t_cs_intelligence",
        "company": "Amazon / AWS",
        "title": "Sr. PM-T, Customer Success Intelligence Team, AWS Specialist Organization",
        "headline": "Senior Technical Product Manager | Customer Success Intelligence & Telemetry | Data Platforms, Cloud Modernization & AI Tooling",
        "summary": "**Senior technical product manager and platform engineering leader** with extensive track record building customer intelligence platforms, telemetry pipelines, and developer portals. Led platform product delivery for the **BlueStack IDP supporting 80–100 engineers**, accelerating deployment cycle times by **40%**, driving an **80% increase in FinOps and governance adherence**, and brings deep expertise in **data modeling, analytics, and applied AI workflows**.",
        "expertise": [
            "Technical Product Management (PM-T) & Telemetry Roadmaps",
            "Customer Intelligence, Analytics & Usage Data Pipelines",
            "Amazon Working Backwards & PR/FAQ Documentation",
            "Developer Experience & Productivity Platforms (40% speedup)",
            "Data Integrity, Relational Schemas & SQL",
            "FinOps Governance, Usage Telemetry & Economics (80% gain)",
            "Cross-Functional Leadership (Engineering, Sales, CS, Data)",
            "Applied AI Tooling & Workflow Automation (Python, Copilot)",
        ],
        "skills": [
            Labeled("Product Management (PM-T):", "Technical product strategy, PRDs, PR/FAQs, roadmaps, customer telemetry, usage data analytics, data-driven flywheels, feature prioritization."),
            Labeled("Databases & Data Analytics:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, telemetry pipelines, data governance."),
            Labeled("Cloud & Platform Engineering:", "AWS Serverless, MS Azure, Kubernetes, Backstage IDP, GitOps, Docker, REST APIs, CI/CD automation."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Intelligence & Product Delivery:", "**Managing engineering and platform product delivery for BlueStack IDP**, directing feature roadmaps, telemetry tracking, and automated workflows supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Architecture & Data Flow:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Intelligence & Governance Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment cycle times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Strategy & Requirements:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align product strategy, increase governance, and optimize operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, elevating digital self-service."),
                    Labeled("Operational Reliability & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident management."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Technical product management for customer success intelligence and data systems", "Directed product direction for BlueStack platform supporting 80–100 engineers with 40% velocity improvement.", "Direct Match", "Direct match for technical product management and data intelligence scope"),
            ("Data telemetry, FinOps governance, and customer usage analytics", "Drove 80% increase in FinOps and governance adherence and established operational analytics across enterprise systems.", "Direct Match", "Backed by verified governance and telemetry facts"),
            ("Cross-functional alignment across technical and business stakeholders", "Partnered across matrixed engineering, operations, and business leadership to deliver mission-critical platforms.", "Direct Match", "Proven cross-functional delivery in complex enterprise environments"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What customer success telemetry signals (e.g. cloud consumption drop-offs, service quota limits, support ticket frequency) are most predictive of customer churn?",
            "What data lakehouse infrastructure powers the Customer Success Intelligence platform today?",
            "How do insights generated by this team feed back into product roadmaps across AWS service teams?",
        ],
    },

    # 17. Amazon - Principal PM-T, Growth, Outbound Communications
    "job-9153eb57": {
        "slug": "amazon_principal_pm_t_growth",
        "company": "Amazon",
        "title": "Principal PM-T, Growth, Outbound Communications",
        "headline": "Principal Technical Product Manager | Growth & Outbound Communications | High-Throughput Messaging, Cloud Scale & Data Systems",
        "summary": "**Principal technical product manager and systems architect** with extensive track record defining product strategy, directing high-scale distributed communication platforms, and driving customer growth. Led technical architecture for the **Blue Shield Member Portal rewrite**, scaled internal developer platforms for **80–100 engineers**, accelerated deployment cycle times by **40%**, and brings deep expertise in **high-throughput messaging, database modeling, and cross-functional leadership**.",
        "expertise": [
            "Principal Technical Product Management (PM-T)",
            "Outbound Communications & High-Scale Notification Systems",
            "Customer Growth, Engagement & Retention Strategies",
            "Amazon Working Backwards & Long-Term Strategy",
            "High-Throughput Distributed Architecture & APIs",
            "Data Modeling, Schema Design & SQL (PostgreSQL, Oracle)",
            "Cross-Functional Leadership across Product, Eng & Analytics",
            "FinOps Governance, Cost-per-Message & Scaling (80% gain)",
        ],
        "skills": [
            Labeled("Product Leadership (PM-T):", "Technical product vision, PR/FAQs, roadmaps, customer journey mapping, growth experimentation, funnel analytics, feature specification, executive reviews."),
            Labeled("Distributed Communications & APIs:", "High-throughput messaging systems, notification architecture, REST APIs, microservices, enterprise middleware integration, real-time message routing."),
            Labeled("Databases & Analytics:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, Transact-SQL, schema design, high-availability transactional data tiers."),
            Labeled("Key Leadership & Governance:", "Team Building and Management, 24x7 Production Operations, Budgeting & FinOps Governance, Regulatory Compliance, AI Implementation & Agentic Workflows, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Product Vision & Management:", "**Managing engineering and platform product delivery for BlueStack IDP**, directing feature roadmaps, developer toolchains, and automated workflows supporting **80–100 internal developers and stakeholders**."),
                    Labeled("High-Scale Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align product strategy, increase governance, and optimize operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal & Communications Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, modernizing member digital notifications and self-service."),
                    Labeled("24x7 Mission-Critical Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("High-Throughput Middleware Architecture:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic architecture, powering mission-critical transaction flows."),
                ],
            ),
        ],
        "comparisons": [
            ("Defining technical vision and product strategy for outbound communications and growth", "Led product direction for BlueStack IDP and architected complete rewrite of the Blue Shield Member Portal communication tier.", "Direct Match", "Direct match for Principal PM-T scope and high-scale communications"),
            ("High-throughput messaging architecture and transactional reliability", "Managed 24x7 operations across 10–15 engineers and architected high-throughput middleware tiers.", "Direct Match", "Proven high-scale production reliability and messaging architecture"),
            ("Data-driven growth, experimentation, and cross-functional leadership", "Drove 40% delivery speedup and 80% improvement in FinOps adherence across complex matrixed enterprise organizations.", "Direct Match", "Demonstrated quantitative product impact and executive alignment"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What messaging channels (e.g. push notifications, email, SMS, in-app messaging) fall under Outbound Communications, and how are contact frequency limits enforced?",
            "What experimentation and uplift modeling harnesses are used to measure incremental engagement and prevent notification fatigue?",
            "How does Outbound Communications collaborate with Information Security and Privacy on customer communication preferences and GDPR/CCPA consent?",
        ],
    },
}
