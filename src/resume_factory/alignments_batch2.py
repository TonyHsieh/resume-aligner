"""Alignment configurations for Batch 2 target roles:
- Kaiser Permanente (3 roles)
- Adyen (6 roles)
- Bunkerhill Health (1 role)
- Nova Credit (1 role)
"""

from typing import Any
from .model import Labeled, Role

BATCH_2_ALIGNMENTS: dict[str, dict[str, Any]] = {
    # 1. Kaiser Permanente - Principal Project Management Consultant
    "job-378a371f": {
        "slug": "kaiser_principal_pm_consultant",
        "company": "Kaiser Permanente",
        "title": "Principal Project Management Consultant",
        "headline": "Principal Technical Program & Infrastructure Delivery Leader | Healthcare Systems & Enterprise Governance",
        "summary": "**Principal technical program manager and enterprise solutions leader** with 10+ years directing large-scale healthcare infrastructure, middleware, and platform modernization programs. Proven track record leading matrixed engineering teams, driving 80% improvement in FinOps and Change Management adherence, and managing complex multi-million dollar enterprise scope across regulated healthcare environments.",
        "expertise": [
            "Enterprise Program Management",
            "Healthcare Technology & Payers",
            "Large-Scale Infrastructure Delivery",
            "Cross-Functional Matrix Leadership",
            "Budget & FinOps Governance (80% adherence)",
            "Change Management & Risk Mitigation",
            "Internal Developer Platforms (IDP)",
            "Executive Stakeholder Consulting",
        ],
        "skills": [
            Labeled("Program & Governance:", "Enterprise program lifecycle, cross-functional matrix management, Microsoft Project, FinOps adherence, Change Management, risk mitigation, audit readiness."),
            Labeled("Cloud, Platforms & Operations:", "Internal Developer Platforms (IDP), Backstage, MS Azure, AWS Serverless, Kubernetes, enterprise middleware, 24x7 incident operations & on-call rotations."),
            Labeled("Architecture & Databases:", "Enterprise systems architecture, SQL, Oracle PL/SQL, REST APIs, high-reliability healthcare payer systems."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Enterprise Program Delivery:", "**Direct delivery of the BlueStack Internal Developer Platform (IDP)** supporting **80–100 engineers**, accelerating deployment turnaround times by **40%** through automated governance and GitOps workflows."),
                    Labeled("Platform Operations & Scale:", "**Accountable for end-to-end support, scaling, and operational maintenance** of platform toolchains, coordinating cross-functional engineering priorities."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("FinOps & Change Management:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Governance:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Operations & Incident Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware across **10–15 engineers**."),
                    Labeled("Complex Infrastructure Programs:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("10+ years managing complex projects using lifecycle methodologies", "10+ years directing healthcare infrastructure and platform engineering programs at Blue Shield and Stellarus.", "Direct Match", "Emphasized program governance, budget tracking, and enterprise delivery lifecycle"),
            ("Experience implementing large, complex projects in corporate environment", "Led BlueStack IDP deployment for 80–100 engineers and enterprise middleware for Blue Shield.", "Direct Match", "Showcased 40% deployment improvement and multi-million dollar scope management"),
            ("Leading matrixed cross-functional teams", "Led 10–15 engineers on 24x7 operational rotations and cross-functional teams across engineering, FinOps, and security.", "Direct Match", "Highlighted matrixed leadership and executive stakeholder engagement"),
            ("Budget & FinOps governance", "Drove 80% increase in FinOps adherence and cost management across platform infrastructure.", "Direct Match", "Explicitly grounded in verified metric"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_02", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What is the target program portfolio for this role (e.g., electronic health records, claims modernization, or infrastructure migration)?",
            "How is the matrixed organization structured between PMO, clinical operations, and technical infrastructure teams?",
            "What specific portfolio management and budgeting tools are standardized at Kaiser (e.g. Clarity, Jira Align, SAP)?",
        ],
    },

    # 2. Kaiser Permanente - Healthcare Technology Solutions Architect
    "job-cf9d844a": {
        "slug": "kaiser_solutions_architect",
        "company": "Kaiser Permanente",
        "title": "Healthcare Technology Solutions Architect",
        "headline": "Healthcare Technology Solutions Architect & Platform Leader | Distributed Systems, Cloud & Payer Integration",
        "summary": "**Healthcare technology solutions architect and engineering leader** with deep expertise translating complex healthcare payer and clinical requirements into resilient technical architectures. Led architecture of BlueStack Internal Developer Platform supporting 80–100 engineers and directed enterprise middleware across 24x7 mission-critical operations at Blue Shield of California.",
        "expertise": [
            "Healthcare Solutions Architecture",
            "Enterprise Payer Technology",
            "Internal Developer Platforms (IDP)",
            "Distributed Middleware & APIs",
            "Cloud Infrastructure (Azure / AWS)",
            "Kubernetes & Container Platforms",
            "Enterprise Data Modeling & SQL",
            "Executive Technical Advisory",
        ],
        "skills": [
            Labeled("Architecture & Modeling:", "Solution architecture, enterprise middleware, API design, data modeling (ER, relational), distributed system patterns, BPMN/UML."),
            Labeled("Cloud & Developer Platforms:", "MS Azure, AWS Serverless, Kubernetes, Backstage IDP, GitOps, CI/CD, GitHub Actions, ArgoCD, Kargo."),
            Labeled("Databases & Systems:", "PostgreSQL, MySQL, Oracle PL/SQL, SQL, Transact-SQL, DynamoDB, high-availability healthcare systems."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Platform Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                    Labeled("Platform Operations & Scale:", "**Accountable for end-to-end support, scaling, and operational maintenance** of BlueStack IDP supporting **80–100 internal developers**."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Technical Architecture & IaC:", "**Designed and developed solutions and enterprise strategies** to increase efficiencies through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Healthcare Solution Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("Mission-Critical Middleware:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware for key healthcare solutions across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Middleware Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Translating solution requirements into technical architecture", "Over 8 years as Infrastructure Solution Architect at Blue Shield of California designing payer platforms.", "Direct Match", "Showcased dual-role architect background and verified title"),
            ("Data modeling and distributed systems", "Extensive database modeling with Oracle PL/SQL, PostgreSQL, SQL, and distributed middleware.", "Direct Match", "Framed high-reliability healthcare transaction systems"),
            ("Executive interaction & supervisory experience", "Supervised 10–15 engineers and presented architectural roadmaps to enterprise executives.", "Direct Match", "Grounded in verified team sizes and leadership facts"),
        ],
        "cited_facts": ["fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "Which primary healthcare domains (e.g. ambulatory, acute care, claims payer, or digital member engagement) will this architect support?",
            "What enterprise architecture standards or frameworks (TOGAF, C4 model, FHIR/HL7) are mandated across the organization?",
            "What is the cloud roadmap balance between on-premise clinical data centers and public cloud (Azure/AWS)?",
        ],
    },

    # 3. Kaiser Permanente - Healthcare Technology Product Manager
    "job-ecb88314": {
        "slug": "kaiser_tech_product_manager",
        "company": "Kaiser Permanente",
        "title": "Healthcare Technology Product Manager",
        "headline": "Technical Product Leader | Healthcare Platforms & Developer Experience | Roadmaps, Discovery & Scaled Delivery",
        "summary": "**Technical product and platform leader** with extensive experience defining product roadmaps, developer tooling vision, and architectural strategy within complex healthcare environments. Designed and led product adoption for the BlueStack Internal Developer Platform supporting 80–100 engineers, improving deployment turnaround times by 40% and driving 80% increases in FinOps adherence.",
        "expertise": [
            "Technical Product Strategy",
            "Internal Developer Platforms (IDP)",
            "Healthcare Systems & Payer Technology",
            "Agile Product Roadmaps & Discovery",
            "Developer Experience (DevEx)",
            "Cross-Functional Execution",
            "FinOps & Metrics Governance",
            "Stakeholder & Executive Alignment",
        ],
        "skills": [
            Labeled("Product Strategy & Agile:", "Product discovery, roadmap development, backlog prioritization, Agile/Scrum ceremonies, developer persona analysis, user adoption metrics."),
            Labeled("Platform & Developer Tooling:", "Internal Developer Platforms (Backstage), CI/CD, GitOps, Kubernetes, MS Azure, AWS Serverless, SonarQube, Artifactory."),
            Labeled("Data & Healthcare Technology:", "Healthcare payer systems, data integrity, SQL, Oracle PL/SQL, REST APIs, enterprise middleware."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Product Ownership:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory)."),
                    Labeled("Platform Scale & Customer Success:", "**Accountable for end-to-end support, scaling, and operational maintenance** of BlueStack IDP supporting **80–100 internal developers and stakeholders**."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Measurable Product Outcomes:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Product Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("Operational Metrics & SLAs:", "**Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs)** across a **10–15 person engineering team**."),
                ],
            ),
        ],
        "comparisons": [
            ("Defining product vision and roadmaps from ideation to launch", "Built BlueStack IDP product roadmap, leading adoption across 80–100 engineers with 40% speed gain.", "Direct Match", "Positioned platform engineering as internal product management"),
            ("Healthcare technology and agile methodologies", "10+ years in healthcare payer systems at Blue Shield coupled with agile sprint leadership.", "Direct Match", "Directly aligned healthcare background with product execution"),
            ("Strategic planning and stakeholder collaboration", "Led roadmap planning with business and infrastructure leadership, delivering 80% FinOps adherence.", "Direct Match", "Showcased quantitative business and technical impact"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_02", "fact_bsc_mid_04"],
        "questions": [
            "Is this product management role focused on internal clinical practitioner tools, digital member portals, or foundational core platforms?",
            "How are product teams structured with respect to engineering pods and clinical subject matter experts?",
            "What product discovery and tracking toolchain (e.g. Jira Product Discovery, Aha!, Productboard) is in use?",
        ],
    },

    # 4. Adyen - Developer Relations Engineer
    "job-d9e1afd6": {
        "slug": "adyen_devrel_engineer",
        "company": "Adyen",
        "title": "Developer Relations Engineer",
        "headline": "Senior Developer Relations & Platform Engineer | APIs, Developer Experience & Cloud Automation",
        "summary": "**Developer advocacy and platform engineer** with proven success bridging technical architectures with developer enablement. Architected and evangelized internal developer platforms for 80–100 engineers, produced technical documentation and sample automation workflows, and delivered 40% faster developer deployment turnaround times.",
        "expertise": [
            "Developer Advocacy & Relations",
            "API Architecture & Integration",
            "Developer Experience (DevEx)",
            "Technical Enablement & Documentation",
            "Internal Developer Platforms (IDP)",
            "Cloud & Container Automation",
            "Applied AI Scripting (Python)",
            "Cross-Functional Community Engagement",
        ],
        "skills": [
            Labeled("Developer Enablement & APIs:", "Developer advocacy, REST APIs, technical writing, SDK/API exploration, developer portal design (Backstage), sample code."),
            Labeled("Languages & Tools:", "Python, JavaScript, Java, SQL, C, Scala, Shell scripting, Git, GitHub Actions, CI/CD."),
            Labeled("Cloud Platforms & Infra:", "Kubernetes, MS Azure, AWS Serverless, Docker, GitOps, automated testing, SonarQube."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Platform Enablement:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting developer toolchains supporting **80–100 internal developers**."),
                    Labeled("Automation Workflows:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation & Infrastructure as Code:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Integration & APIs:", "**Integrated enterprise appliances and distributed applications** into secure infrastructure, ensuring reliable developer interfaces."),
                    Labeled("Operational Excellence:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
        ],
        "comparisons": [
            ("Advocate for developers & create technical content", "Built developer documentation, scaffolding, and self-service portals for 80–100 engineers.", "Direct Match", "Positioned internal platform advocacy as direct transferable DevRel experience"),
            ("Strong experience with APIs and modern languages", "Expert in REST APIs, Python, JavaScript, Java, and cloud platforms.", "Direct Match", "Aligned core multi-language background"),
            ("Fostering developer communities and adoption", "Drove BlueStack adoption leading to 40% faster deployment turnaround.", "Direct Match", "Grounded in verified metrics"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_03"],
        "questions": [
            "Which developer community segments (e.g., enterprise merchants, platform partners, or open-source contributors) are primary targets?",
            "What is the team's balance between hands-on code samples/SDKs vs. public speaking, blog authoring, and conference presence?",
            "What specific payment API products will this role focus on (e.g. In-Person Payments, Online Checkout, or Platforms/Capital)?",
        ],
    },

    # 5. Adyen - Implementation Engineer
    "job-6be1d282": {
        "slug": "adyen_implementation_engineer",
        "company": "Adyen",
        "title": "Implementation Engineer",
        "headline": "Senior Technical Implementation & Integration Engineer | Payment APIs, Middleware & High-Reliability Systems",
        "summary": "**Hands-on technical implementation and integration engineer** with deep expertise in API delivery, enterprise middleware, and mission-critical distributed systems. Successfully designed and operated 24x7 systems with 10–15 engineers at Blue Shield of California, leading technical client integrations, complex data transformations, and automated CI/CD delivery.",
        "expertise": [
            "Enterprise Technical Implementation",
            "REST API & Webhook Integrations",
            "Middleware & Messaging Architecture",
            "High-Reliability Systems (24x7)",
            "SQL & Relational Data Engineering",
            "Cloud Automation & GitOps",
            "Client Technical Consulting",
            "Incident Triaging & RCA",
        ],
        "skills": [
            Labeled("APIs & Integration:", "REST APIs, Webhooks, JSON, XML, enterprise middleware, API authentication, message routing, integration architecture."),
            Labeled("Languages & Databases:", "Python, JavaScript, SQL, Java, Oracle PL/SQL, PostgreSQL, MySQL, data transformations."),
            Labeled("Platforms & DevOps:", "Kubernetes, MS Azure, AWS Serverless, GitHub Actions, CI/CD, GitOps, SonarQube."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Integration Delivery:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting integration toolchains for **80–100 developers**."),
                    Labeled("Deployment Automation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Automated Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Solutions Engineering:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Integration Engineering:", "**Integrated enterprise appliances and distributed applications** into secure infrastructure, ensuring robust data exchange."),
                    Labeled("Mission-Critical Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Technical Implementation:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Deep experience in APIs and technical integrations", "Extensive hands-on integration of enterprise middleware, REST APIs, and database pipelines.", "Direct Match", "Showcased technical delivery rigor"),
            ("Customer-facing technical consulting and troubleshooting", "Consulted enterprise stakeholders and led 24x7 incident triage across 10–15 engineers.", "Direct Match", "Directly backed by verified operational facts"),
            ("High reliability and system uptime", "Maintained 24x7 high-uptime operations for core transactional systems.", "Direct Match", "Grounded in verified on-call leadership"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_03", "fact_safe_01"],
        "questions": [
            "What are the typical technical complexities in customer implementations (e.g. legacy ERP integration, omni-channel point-of-sale, or custom tokenization)?",
            "What is the average timeline and team composition for an enterprise merchant onboarding?",
            "How closely does Implementation Engineering collaborate with Core Product and Account Management squads?",
        ],
    },

    # 6. Adyen - Engineering Manager, Capital
    "job-0ed1b63d": {
        "slug": "adyen_em_capital",
        "company": "Adyen",
        "title": "Engineering Manager, Capital",
        "headline": "Engineering Manager | Financial & Platform Systems | Cloud Architecture, Agile Leadership & High-Reliability Operations",
        "summary": "**Software engineering and platform leader** with proven record managing distributed engineering teams, high-availability transaction middleware, and cloud platform delivery. Built and led 24x7 operational on-call rotations across 10–15 engineers, scaled developer platforms for 80–100 users, and achieved 40% improvement in deployment turnaround while enforcing strict FinOps adherence.",
        "expertise": [
            "Engineering Team Leadership",
            "FinTech & Transaction Platforms",
            "24x7 Mission-Critical Operations",
            "Cloud Architecture (Azure / AWS)",
            "People Management & Mentorship",
            "High-Reliability Middleware",
            "Agile Execution & Delivery",
            "FinOps Governance (80% adherence)",
        ],
        "skills": [
            Labeled("Leadership & Management:", "Engineering people management, hiring, career mentorship, 24x7 on-call structure, incident management, sprint execution."),
            Labeled("Platform & Cloud Systems:", "Internal Developer Platforms (IDP), MS Azure, AWS Serverless, Kubernetes, GitOps, CI/CD, SonarQube."),
            Labeled("Languages & Databases:", "Python, JavaScript, SQL, Java, Oracle PL/SQL, PostgreSQL, MySQL, REST APIs, data integrity."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Engineering Leadership:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies."),
                    Labeled("Operational Scale:", "**Accountable for end-to-end support, scaling, and operational maintenance of BlueStack IDP** supporting **80–100 internal developers and stakeholders**."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("FinOps & Cost Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Partnership:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("People & Operational Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware across **10–15 engineers**."),
                    Labeled("Operational Excellence:", "**Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs)** across a **10–15 person engineering team**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Engineering management and people leadership", "Managed 10–15 engineers at Blue Shield and lead platform operations for 80–100 users at Stellarus.", "Direct Match", "Direct match for EM scope, hiring, and mentorship"),
            ("High-reliability financial / transaction systems", "Directed core transaction middleware and 24x7 incident operations in heavily regulated payer ecosystem.", "Direct Match", "High relevance to Adyen Capital's financial underwriting and payout systems"),
            ("Agile execution and operational metrics", "Delivered 40% faster deployment turnaround and 80% higher FinOps adherence.", "Direct Match", "Quantified management achievements"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_02", "fact_safe_01"],
        "questions": [
            "What is the current scale and growth trajectory of the Capital engineering team in North America?",
            "What are the key technical challenges in the Capital product roadmap (e.g. credit decisioning latency, multi-currency underwriting, regulatory reporting)?",
            "How is engineering ownership divided between Amsterdam headquarters and North American engineering hubs?",
        ],
    },

    # 7. Adyen - Senior Software Engineer, Customer Interfaces
    "job-498bec76": {
        "slug": "adyen_senior_swe_customer_interfaces",
        "company": "Adyen",
        "title": "Senior Software Engineer - Customer Interfaces",
        "headline": "Senior Full-Stack & Interface Engineer | High-Scale Web Architecture, APIs & Developer Productivity",
        "summary": "**Senior full-stack and systems engineer** with deep experience building resilient web applications, customer-facing interfaces, and high-performance API platforms. Led developer platform interfaces supporting 80–100 engineers, automated CI/CD deployment pipelines cutting lead times by 40%, and designed robust SQL/REST data layers.",
        "expertise": [
            "Web Application Engineering",
            "REST API Design & Streaming Interfaces",
            "Developer Tooling & UI",
            "Cloud Systems (Kubernetes / Azure / AWS)",
            "SQL & Data Modeling",
            "Automated CI/CD & Testing",
            "Code Quality & Performance",
            "Cross-Functional Delivery",
        ],
        "skills": [
            Labeled("Frontend & Web:", "JavaScript, HTML5, CSS, responsive design, UI component architecture, developer portal interfaces (Backstage)."),
            Labeled("Backend & APIs:", "Python, Java, SQL, REST APIs, JSON, microservices, asynchronous processing."),
            Labeled("Platforms & DevOps:", "Kubernetes, MS Azure, AWS Serverless, GitHub Actions, GitOps, CI/CD, SonarQube, Artifactory."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Interface & Platform Tooling:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory)."),
                    Labeled("Platform Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Speed & Quality:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Solutions Engineering:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Rewrite:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("High-Reliability Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="(Concurrent) Independent Contractor",
                dates="April 1999 – November 2012",
                title="Full-Stack Engineer & Product Lead",
                bullets=[
                    Labeled("Full-Stack Web Engineering:", "**Engineered full-stack front-end (JavaScript, CSS) and backend services (PHP, MySQL, APIs)** for commercial high-concurrency interactive platforms and applications."),
                ],
            ),
        ],
        "comparisons": [
            ("Building end-to-end web interfaces and applications", "Built full-stack web systems, developer portal interfaces, and backend API integration layers.", "Direct Match", "Emphasized web and full-stack engineering background"),
            ("Strong API integration and performance", "Extensive experience designing and optimizing REST API services and database integrations.", "Direct Match", "Showcased high-throughput systems expertise"),
            ("Focus on reliability and quality", "Established automated testing, SonarQube quality gates, and 24x7 operational uptime.", "Direct Match", "Backed by verified facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_game_01"],
        "questions": [
            "What frontend framework and design system standards are established across Adyen Customer Interfaces (e.g. React, TypeScript, Vue)?",
            "What streaming or multi-modal interface capabilities are currently in development?",
            "How does the team handle localization and compliance across global merchant portals?",
        ],
    },

    # 8. Adyen - Software Engineer II (Frontend), Observability
    "job-2383c61f": {
        "slug": "adyen_swe_observability",
        "company": "Adyen",
        "title": "Software Engineer II (Frontend) - Customer Developer Observability",
        "headline": "Frontend & Observability Software Engineer | Telemetry, Developer Portals & Operational Dashboards",
        "summary": "**Frontend and developer experience software engineer** specializing in operational telemetry, developer portals, and monitoring interfaces. Designed developer portal UI and observability tooling across Internal Developer Platforms supporting 80–100 engineers, improving system transparency, deployment monitoring, and incident turnaround.",
        "expertise": [
            "Developer Observability & Telemetry",
            "Frontend Web Engineering (JavaScript / HTML5 / CSS)",
            "Developer Portals (Backstage IDP)",
            "CI/CD & Pipeline Visibility",
            "Operational Metrics & Dashboards",
            "REST APIs & Telemetry Ingestion",
            "Quality Assurance & SonarQube",
            "Cross-Team Enablement",
        ],
        "skills": [
            Labeled("Frontend & UI:", "JavaScript, CSS, HTML5, UI component development, operational dashboards, data visualization, Backstage plugin UI."),
            Labeled("Observability & DevOps:", "Telemetry monitoring, CI/CD pipeline visibility, SonarQube, GitHub Actions, GitOps, Kubernetes, MS Azure, AWS."),
            Labeled("Languages & Data:", "Python, SQL, REST APIs, JSON, log parsing, automated testing."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Portal & Observability:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory)."),
                    Labeled("Portal Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Operational Visibility & Metrics:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation Solutions:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Incident Monitoring & Triage:", "**Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs)** across a **10–15 person engineering team**."),
                    Labeled("Application Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                ],
            ),
        ],
        "comparisons": [
            ("Building developer-facing observability and frontend tooling", "Created Backstage developer portal interfaces and pipeline observability tooling for 80–100 users.", "Direct Match", "Direct match for observability dashboard engineering"),
            ("Frontend skills in JavaScript, CSS, HTML", "Solid frontend web fundamentals and interface architecture.", "Direct Match", "Aligned core web competencies"),
            ("Improving developer workflow velocity", "Reduced deployment turnaround times by 40% through transparent tooling.", "Direct Match", "Backed by verified IDP metrics"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_02", "fact_bsc_mid_04"],
        "questions": [
            "What observability and telemetry stack (e.g. Grafana, Prometheus, OpenTelemetry, Datadog) powers the customer interfaces?",
            "What specific developer metrics (e.g. API latency, error budgets, webhook delivery success rates) do merchants inspect most frequently?",
            "How does the team approach micro-frontend architecture across Adyen's customer portal?",
        ],
    },

    # 9. Adyen - Staff Engineer, Customer Interfaces
    "job-e40fbd4d": {
        "slug": "adyen_staff_engineer_interfaces",
        "company": "Adyen",
        "title": "Staff Engineer - Customer Interfaces",
        "headline": "Staff Systems & Interface Architect | Agentic Workflows, Scaled APIs & Platform Architecture",
        "summary": "**Staff systems and interface architect** with comprehensive background in distributed systems, modern API design, and applied automation workflows. Architected BlueStack developer platforms for 80–100 engineers, led 24x7 mission-critical operations, and developed applied AI agents (OpenAI Codex, Copilot, Python) to automate developer workflows.",
        "expertise": [
            "Staff Platform Architecture",
            "Applied AI & Agentic Workflows",
            "High-Throughput REST APIs",
            "Distributed Middleware Architecture",
            "Cloud & Container Systems (K8s)",
            "Developer Platform Interfaces",
            "Operational Resilience (24x7)",
            "Cross-Functional Technical Strategy",
        ],
        "skills": [
            Labeled("Architecture & Agentic Workflows:", "System architecture, applied AI workflows (OpenAI Codex, Copilot, Ollama, Python agents), API design, distributed patterns."),
            Labeled("Platforms & Cloud:", "Kubernetes, MS Azure, AWS Serverless, Internal Developer Platforms (Backstage), GitOps, CI/CD, SonarQube."),
            Labeled("Languages & Databases:", "Python, JavaScript, SQL, Java, Scala, C, Oracle PL/SQL, PostgreSQL, high-performance data interfaces."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform & Architecture Strategy:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                    Labeled("Platform Scale & Governance:", "**Accountable for end-to-end support, scaling, and operational maintenance** of BlueStack IDP supporting **80–100 internal developers and stakeholders**."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Cloud Transformation & Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Architecture:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Solution Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("Operational Resilience:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Middleware Modernization:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Architectural hat & building agentic workflows", "Architected BlueStack IDP and engineered custom applied AI agents (Codex, Copilot, Python).", "Direct Match", "Direct response to Adyen's specific job description request for agentic workflows"),
            ("High-scale system architecture and API design", "Decade of enterprise middleware and solution architecture handling mission-critical volume.", "Direct Match", "Showcased staff-level architectural breadth"),
            ("Cross-team influence and technical leadership", "Guided platform strategy across 80–100 engineers with 40% deployment speed improvements.", "Direct Match", "Backed by verified accomplishments"),
        ],
        "cited_facts": ["fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What specific agentic workflow use cases (e.g. automated reconciliation, dispute resolution, merchant support agents) are prioritized?",
            "How is technical authority and decision-making balanced between Staff Engineers and Product Engineering Directors?",
            "What are the latency and security boundaries for deploying LLM-driven agents into financial transaction flows?",
        ],
    },

    # 10. Bunkerhill Health - Forward Deployed Engineer
    "job-9bc0e009": {
        "slug": "bunkerhill_forward_deployed_engineer",
        "company": "Bunkerhill Health",
        "title": "Forward Deployed Engineer",
        "headline": "Forward Deployed Systems & Integration Engineer | Healthcare Data Platforms, Clinical APIs & Legacy Bridges",
        "summary": "**Healthcare systems integration and forward-deployed platform engineer** with 10+ years solving complex healthcare payer and clinical interoperability challenges at Blue Shield of California. Proven experience integrating legacy enterprise endpoints, building robust middleware data bridges, and scaling developer platforms supporting 80–100 engineers.",
        "expertise": [
            "Healthcare Interoperability & Integration",
            "Clinical & Payer Data Pipelines",
            "Legacy System Bridging",
            "Forward Deployed Execution",
            "REST APIs & Enterprise Middleware",
            "High-Reliability Operations (24x7)",
            "SQL & Relational Modeling",
            "Rapid Incident Resolution",
        ],
        "skills": [
            Labeled("Healthcare Integration & Data:", "Healthcare data interfaces, legacy system integrations, SQL, relational data modeling, Oracle PL/SQL, REST APIs, JSON, XML."),
            Labeled("Languages & Automation:", "Python, JavaScript, Java, C, Shell scripting, automated ETL/data pipelines, applied AI agents."),
            Labeled("Platforms & Reliability:", "Kubernetes, MS Azure, AWS Serverless, Docker, GitOps, 24x7 incident response, production triage."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform & Tooling Scale:", "**Accountable for end-to-end support, scaling, and operational maintenance of BlueStack IDP** supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Deployment Automation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Integration Solutions:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Healthcare Data Integration:", "**Integrated enterprise appliances and distributed applications** into secure Blue Shield infrastructure."),
                    Labeled("24x7 High-Stakes Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware for key healthcare solutions across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Legacy Transformation:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Tackling unglamorous legacy system integrations that fight back", "Over 8 years resolving complex legacy payer and provider integrations at Blue Shield of California.", "Direct Match", "Direct answer to Bunkerhill's exact JD ethos"),
            ("High-stakes healthcare data integrity", "Led 24x7 operations on critical healthcare transactional systems with 10–15 engineers.", "Direct Match", "Demonstrated operational resilience under clinical/payer constraints"),
            ("Fast-paced technical troubleshooting", "Extensive experience diagnosing production endpoints, data mismatches, and automated remediation.", "Direct Match", "Backed by verified infrastructure facts"),
        ],
        "cited_facts": ["fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_03", "fact_safe_01"],
        "questions": [
            "What specific EHR systems (Epic, Cerner, MEDITECH) and integration mechanisms (FHIR, HL7 v2, direct database/SFTP) are most common in client hospital deployments?",
            "What is the typical balance of on-site health system presence vs. remote forward-deployed engineering?",
            "How does the Carebricks platform isolate client hospital data while maintaining centralized agent deployment?",
        ],
    },

    # 11. Nova Credit - Senior Software Engineer
    "job-fddf259b": {
        "slug": "nova_credit_senior_swe",
        "company": "Nova Credit",
        "title": "Senior Software Engineer",
        "headline": "Senior Backend & Data Infrastructure Software Engineer | Financial APIs, High-Reliability SQL & Cloud Platforms",
        "summary": "**Senior backend and data systems software engineer** with deep experience building resilient data pipelines, financial/payer systems, and high-reliability cloud platforms. Directed 24x7 middleware infrastructure across 10–15 engineers, scaled internal developer platforms supporting 80–100 engineers, and architected reliable SQL/relational data models.",
        "expertise": [
            "Financial Data Infrastructure",
            "Backend Systems & APIs",
            "Relational Data Modeling & SQL",
            "High-Reliability Operations (24x7)",
            "Cloud & Containers (Kubernetes / Azure / AWS)",
            "CI/CD & GitOps Automation",
            "Security & Compliance Controls",
            "Cross-Functional Delivery",
        ],
        "skills": [
            Labeled("Backend & Data Architecture:", "SQL, PostgreSQL, MySQL, Oracle PL/SQL, DynamoDB, REST APIs, microservices, data modeling, data integrity."),
            Labeled("Languages & Frameworks:", "Python, JavaScript, Java, C, Scala, Shell scripting, automated testing."),
            Labeled("Cloud Platforms & DevOps:", "Kubernetes, MS Azure, AWS Serverless, GitHub Actions, GitOps, CI/CD, SonarQube, Artifactory."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform & Tooling Operations:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory)."),
                    Labeled("High-Scale Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Cloud Data Platform Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automated Infrastructure:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("High-Throughput Middleware:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical middleware for key solutions across **10–15 engineers**."),
                    Labeled("Digital Systems Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Database & Middleware Architecture:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Building resilient backend services and data integrations", "Architected high-volume transaction middleware and data pipelines at Blue Shield and Stellarus.", "Direct Match", "Showcased deep data infrastructure and backend rigor"),
            ("Strong database and SQL expertise", "Extensive experience with PostgreSQL, MySQL, Oracle PL/SQL, and relational data integrity.", "Direct Match", "Directly aligned with Nova Credit's credit data modeling needs"),
            ("High reliability and operational excellence", "Led 24x7 on-call incident response for 10–15 engineers on mission-critical platforms.", "Direct Match", "Backed by verified operational facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What are the primary technical bottlenecks in cross-border credit data ingestion and entity resolution?",
            "What database architecture (e.g. Aurora PostgreSQL, DynamoDB) is standardized for Nova Credit's core scoring engine?",
            "How are data privacy compliance standards (e.g. FCRA, GDPR) enforced at the data pipeline architecture level?",
        ],
    },
}
