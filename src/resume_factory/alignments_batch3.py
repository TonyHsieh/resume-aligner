"""Alignment configurations for Batch 3 target roles:
- NextPatient: Staff Software Engineer (job-2f90931c)
- NextPatient: Senior Software Engineer (job-9f62a988)
- Snowflake: Staff Product Manager, Enterprise Technology (job-14d955e4)
- Snowflake: Principal Program Manager - Migrations (job-018e6fc1)
"""

from typing import Any
from .model import Labeled, Role

BATCH_3_ALIGNMENTS: dict[str, dict[str, Any]] = {
    # 1. NextPatient - Staff Software Engineer
    "job-2f90931c": {
        "slug": "nextpatient_staff_swe",
        "company": "NextPatient",
        "title": "Staff Software Engineer",
        "headline": "Staff Full-Stack & Healthcare Systems Engineer | Python, JavaScript & PostgreSQL | Legacy Bridges & Modern UX",
        "summary": "**Staff software engineer and systems architect** with 10+ years building resilient web applications, healthcare integrations, and developer platforms. Proven experience bridging legacy health systems with modern patient and member portals, engineering high-reliability backend services using **Python, JavaScript, and PostgreSQL on Linux**, and leveraging applied AI automation to accelerate product delivery.",
        "expertise": [
            "Full-Stack Web Engineering (Python / JS / SQL)",
            "Legacy Healthcare Systems Integration",
            "PostgreSQL & Relational Data Modeling",
            "Digital Patient & Member Portals",
            "Applied AI & Developer Tooling",
            "High-Reliability Architecture (24x7)",
            "Linux Systems & Cloud Automation",
            "Cross-Functional Product Ownership",
        ],
        "skills": [
            Labeled("Languages & Web:", "Python, JavaScript, Rust, SQL, HTML5, CSS, REST APIs, JSON, microservices, Linux environment."),
            Labeled("Databases & Systems:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, Transact-SQL, relational schema design, query optimization."),
            Labeled("Platforms & Automation:", "Kubernetes, MS Azure, AWS Serverless, Docker, GitOps, CI/CD, GitHub Actions, applied AI agents (Codex, Copilot, Ollama)."),
            Labeled("Leadership & Operations:", "Team Building and Management, 24x7 Production Operations, Regulatory Compliance, Cross-Functional Collaboration, Change Leadership."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Product & Platform Engineering:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipelines, and supporting developer toolchains supporting **80–100 internal developers**."),
                    Labeled("Applied AI & Automation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, and GitOps**, supplemented by custom Python scripting and applied AI tooling to streamline developer feature delivery."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Velocity & Scaled Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Architecture & Automation:", "**Designed and developed solutions and enterprise strategies** to increase efficiencies through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Healthcare Portal Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal, modernizing legacy systems into responsive digital experiences."),
                    Labeled("Mission-Critical Reliability:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, ensuring flawless healthcare transaction processing."),
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
            ("Plugging into legacy doctor office systems to modernise patient experience", "Led full architecture for Member Portal rewrite bridging legacy systems at Blue Shield.", "Direct Match", "Emphasized legacy bridge architecture and modernized patient UX"),
            ("Tech stack: Python, JavaScript, and Postgres on Linux", "Extensive production engineering in Python, JavaScript, PostgreSQL, and Linux.", "Direct Match", "Aligned exact core technology stack"),
            ("High-ownership full-stack IC delivery (10+ years experience)", "15+ years delivering full-stack platforms with cradle-to-grave ownership.", "Direct Match", "Showcased end-to-end technical independence and leadership"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_game_01"],
        "questions": [
            "What specific EHR/practice management APIs (e.g. athenahealth, eClinicalWorks, Allscripts) represent the highest volume integration challenges?",
            "How is code ownership and architectural consensus structured across the engineering team?",
            "What are the immediate priorities for expanding AI-driven capabilities within the patient check-in and scheduling workflow?",
        ],
    },

    # 2. NextPatient - Senior Software Engineer
    "job-9f62a988": {
        "slug": "nextpatient_senior_swe",
        "company": "NextPatient",
        "title": "Senior Software Engineer",
        "headline": "Senior Full-Stack & Integration Engineer | Python, JavaScript & PostgreSQL | Healthcare UX & Automated Workflows",
        "summary": "**Senior full-stack software engineer** with deep experience building intuitive web applications, robust database pipelines, and resilient healthcare integrations. Extensive hands-on background developing in **Python, JavaScript, and PostgreSQL on Linux**, with a track record of modernizing dated legacy workflows into seamless self-service patient portals.",
        "expertise": [
            "Full-Stack Web Development",
            "Python, JavaScript & Relational SQL",
            "PostgreSQL Database Optimization",
            "Healthcare Integration Architecture",
            "REST APIs & Webhook Services",
            "Linux Systems & Deployment Automation",
            "High-Reliability Operations (24x7)",
            "Agile Delivery & Feature Ownership",
        ],
        "skills": [
            Labeled("Languages & Frameworks:", "Python, JavaScript, Rust, SQL, HTML5, CSS, REST APIs, JSON, microservices, Linux shell scripting."),
            Labeled("Databases & Data Modeling:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema design, relational data integrity, query tuning."),
            Labeled("DevOps & Platform Tools:", "Docker, Kubernetes, GitOps, CI/CD, GitHub Actions, MS Azure, AWS Serverless, SonarQube."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Regulatory Compliance, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Full-Stack Engineering & Tooling:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies for **80–100 internal developers**."),
                    Labeled("Deployment Velocity:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Workflow Optimization:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation Solutions:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("High-Reliability Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="(Concurrent) Independent Contractor",
                dates="April 1999 – November 2012",
                title="Full-Stack Engineer & Product Lead",
                bullets=[
                    Labeled("End-to-End Application Delivery:", "**Engineered full-stack front-end (JavaScript, CSS) and backend services (PHP, MySQL, APIs)** for commercial high-concurrency interactive platforms and applications."),
                ],
            ),
        ],
        "comparisons": [
            ("Upgrading patient experience & doctor legacy systems", "Led architecture rewriting member portal from legacy interfaces to modern web standards.", "Direct Match", "Direct parallel to doctor office digital transformation"),
            ("Proficiency in Python, JavaScript, and PostgreSQL on Linux", "Extensive production development in Python, JavaScript, PostgreSQL, and Linux.", "Direct Match", "Exact technology stack alignment"),
            ("High ownership in small collaborative teams", "Led full lifecycle delivery from conception to production across platforms.", "Direct Match", "Showcased builder mentality"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_game_01"],
        "questions": [
            "How does the team approach testing and simulating third-party EHR integration failures in local development?",
            "What is the deployment frequency and release verification workflow at NextPatient?",
            "What are the most requested features from clinic staff regarding online scheduling and automated reminders?",
        ],
    },

    # 3. Snowflake - Staff Product Manager, Enterprise Technology
    "job-14d955e4": {
        "slug": "snowflake_staff_pm_enterprise_tech",
        "company": "Snowflake",
        "title": "Staff Product Manager, Enterprise Technology",
        "headline": "Staff Technical Product Leader | Enterprise Platforms, Developer Tooling & Cloud Data Modernization",
        "summary": "**Staff technical product and platform leader** with extensive track record directing product roadmaps, developer tooling strategies, and enterprise cloud modernization. Successfully guided product vision and adoption for the BlueStack Internal Developer Platform supporting 80–100 engineers, delivering 40% improvements in deployment cycle times and driving an 80% increase in FinOps adherence.",
        "expertise": [
            "Enterprise Technical Product Strategy",
            "Internal Developer Platforms (IDP)",
            "Cloud Data & Platform Modernization",
            "Developer Experience & Tooling Vision",
            "FinOps Governance & Cost Metrics (80% adherence)",
            "Agile Roadmaps & Feature Prioritization",
            "Cross-Functional Executive Partnership",
            "Vendor Management & Contract Negotiation",
        ],
        "skills": [
            Labeled("Product Strategy & Roadmaps:", "Product discovery, enterprise requirements gathering, roadmap formulation, sprint backlog prioritization, developer persona analysis."),
            Labeled("Enterprise Platforms & Cloud:", "Internal Developer Platforms (Backstage), Kubernetes, MS Azure, AWS Serverless, GitOps, CI/CD, SonarQube, Artifactory."),
            Labeled("Data & Governance:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, SQL, FinOps controls, Change Management, enterprise audit readiness."),
            Labeled("Leadership & Operations:", "Team Building and Management, Budgeting, Regulatory Compliance, Vendor Management, Contract Negotiation, Change Leadership."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Product Leadership:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory)."),
                    Labeled("Enterprise User Scale:", "**Accountable for end-to-end support, scaling, and operational maintenance of BlueStack IDP** supporting **80–100 internal developers and stakeholders**."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Quantitative Product Outcomes:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Strategy & Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Capability Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Operational Governance:", "**Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs)** across a **10–15 person engineering team**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Platform Migration:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Defining enterprise technology product vision and roadmap", "Built and scaled product roadmap for BlueStack IDP supporting 80–100 engineers with 40% speed gain.", "Direct Match", "Positioned platform engineering as internal enterprise product management"),
            ("Cloud platform adoption and operational efficiency", "Drove Azure adoption, infrastructure automation, and 80% increase in FinOps adherence.", "Direct Match", "Strong quantitative alignment with enterprise tooling"),
            ("Cross-functional executive leadership", "Partnered across business units and engineering teams to govern multi-million dollar platforms.", "Direct Match", "Backed by verified governance facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_02", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What enterprise technology tools and internal customer groups are the primary focus of this product management role at Snowflake?",
            "How does Enterprise Technology partner with Core Engineering to define unified platform standards?",
            "What are Snowflake's target KPIs for internal developer productivity and enterprise tooling adoption?",
        ],
    },

    # 4. Snowflake - Principal Program Manager, Migrations (Professional Services)
    "job-018e6fc1": {
        "slug": "snowflake_principal_pm_migrations",
        "company": "Snowflake",
        "title": "Principal Program Manager - Migrations",
        "headline": "Principal Technical Program Manager | Cloud Migrations & Professional Services | Enterprise Transformation",
        "summary": "**Principal technical program manager and enterprise solutions leader** with extensive background managing large-scale cloud migrations, complex middleware transformations, and professional services delivery. Proven track record leading matrixed technical delivery teams, driving an 80% increase in Change Management and FinOps adherence, and architecting mission-critical system migrations.",
        "expertise": [
            "Enterprise Cloud & Database Migrations",
            "Professional Services & Client Delivery",
            "Large-Scale Technical Program Management",
            "Cross-Functional Matrix Leadership",
            "Change Leadership & Risk Mitigation",
            "FinOps Adherence & Budget Controls (80% gain)",
            "High-Reliability Operations (24x7)",
            "Executive Stakeholder Consulting",
        ],
        "skills": [
            Labeled("Program Delivery & Methodology:", "Enterprise program lifecycle, client consulting, migration runbooks, risk mitigation, Microsoft Project, Change Management, FinOps governance."),
            Labeled("Platforms & Migration Architecture:", "Enterprise database migrations, cloud platforms (MS Azure, AWS Serverless), Kubernetes, Backstage IDP, CI/CD, GitOps."),
            Labeled("Databases & Middleware:", "Oracle PL/SQL, SQL, PostgreSQL, MySQL, DynamoDB, Oracle WebLogic, legacy enterprise systems."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Modernization Delivery:", "**Direct delivery of the BlueStack Internal Developer Platform (IDP)** supporting **80–100 engineers**, accelerating deployment turnaround times by **40%** through standardized automation."),
                    Labeled("Program Scale & Stakeholder Management:", "**Accountable for end-to-end support, scaling, and operational maintenance** of platform toolchains, governing cross-functional delivery."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Enterprise Cloud Migration:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Stakeholder Alignment & Governance:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Migration & Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 High-Stakes Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Strategic Enterprise Database & Middleware Transformation:", "**Designed and led strategic enterprise transformation** from legacy middleware to Oracle WebLogic and Database architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Leading complex enterprise cloud and data migrations", "Led enterprise migration to Azure and strategic middleware transformation to Oracle WebLogic/Database.", "Direct Match", "Emphasized end-to-end migration execution, runbooks, and risk mitigation"),
            ("Professional services and executive consulting", "Managed cross-functional stakeholder roadmaps, governing multi-million dollar scope and change leadership.", "Direct Match", "Demonstrated high-stakes client and advisory excellence"),
            ("FinOps and program governance", "Delivered 80% increase in FinOps and Change Management adherence.", "Direct Match", "Backed by verified governance metrics"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What legacy data platforms (e.g. Teradata, Netezza, Hadoop, Oracle Exadata) represent the most frequent customer migration pathways to Snowflake?",
            "How does Professional Services collaborate with Systems Integrator (SI) partners on enterprise migration engagements?",
            "What automated migration assessment and schema conversion tooling is standard within Snowflake's migration methodology?",
        ],
    },
}
