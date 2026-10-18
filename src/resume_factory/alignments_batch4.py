"""Alignment configurations for Batch 4 target roles (Zoox):
- Zoox: Senior Manager, Software Tools Development (job-df12660d)
- Zoox: Manager, Service Operations Systems (job-32f81e3e)
- Zoox: Technical Program Manager - Product Software (job-7f54c878)
- Zoox: Senior/Staff Design Project Manager, Places & Build (job-3a96f885)
- Zoox: Manager, Enterprise Applications (job-6eb18c4c)
"""

from typing import Any
from .model import Labeled, Role

BATCH_4_ALIGNMENTS: dict[str, dict[str, Any]] = {
    # 1. Zoox - Senior Manager, Software Tools Development
    "job-df12660d": {
        "slug": "zoox_sr_mgr_software_tools",
        "company": "Zoox",
        "title": "Senior Manager, Software Tools Development",
        "headline": "Senior Engineering Leader | Developer Tooling & Software Platforms | CI/CD, GitOps & High-Velocity Engineering",
        "summary": "**Software tools engineering and platform leader** with extensive track record directing engineering teams, developer productivity platforms, and automated release infrastructure. Successfully led the **BlueStack Internal Developer Platform** supporting **80–100 engineers**, accelerating deployment cycle times by **40%**, scaling CI/CD and GitOps workflows on Kubernetes, and fostering high-performing engineering cultures.",
        "expertise": [
            "Developer Tools & Platform Engineering",
            "Software Productivity & Velocity (40% speed gain)",
            "Engineering People Management & Mentorship",
            "CI/CD Pipelines & GitOps Automation",
            "Kubernetes & Cloud Infrastructure (Azure / AWS)",
            "Code Quality, Telemetry & SonarQube",
            "High-Reliability Architecture (24x7)",
            "Cross-Functional Platform Strategy",
        ],
        "skills": [
            Labeled("Developer Tools & Platforms:", "Internal Developer Platforms (Backstage), CI/CD, GitOps, Kubernetes, ArgoCD, Kargo, GitHub Actions, Bitbucket, SonarQube, Artifactory, developer experience tooling."),
            Labeled("Languages & Systems:", "Python, JavaScript, Rust, C, Java, Shell scripting, Linux environment, REST APIs, microservices."),
            Labeled("Databases & Cloud:", "MS Azure, AWS Serverless, Docker, PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, high-reliability infrastructure."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration, Vendor Management."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Tools Engineering Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Developer Productivity Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Measurable Velocity Gains:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation Tooling Strategy:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("High-Reliability Operations & Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical platforms across **10–15 engineers**."),
                    Labeled("Systems Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting large-scale enterprise modernization."),
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
            ("Leading engineering teams building software development tools", "Manage engineering team operating BlueStack IDP, CI/CD, and developer toolchains for 80–100 engineers.", "Direct Match", "Direct match for developer tools leadership and platform scope"),
            ("Accelerating release velocity and developer productivity", "Drove 40% reduction in developer deployment times through automated self-service workflows.", "Direct Match", "Grounded in verified quantitative metric"),
            ("Engineering people leadership and operational rigor", "Managed 10–15 engineers on 24x7 operations at Blue Shield and lead platform teams at Stellarus.", "Direct Match", "Demonstrated team building and mentorship excellence"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "What developer toolchains (e.g. Bazel, custom simulation harnesses, onboard logging tools) represent the highest leverage investment areas for the AV software stack?",
            "How does the Tools Development team partner with Autonomous Driving and Systems Software teams to eliminate workflow friction?",
            "What are the target metrics for build latency, test flakiness, and developer environment spin-up times?",
        ],
    },

    # 2. Zoox - Manager, Service Operations Systems
    "job-32f81e3e": {
        "slug": "zoox_mgr_service_operations",
        "company": "Zoox",
        "title": "Manager, Service Operations Systems",
        "headline": "Engineering Manager | Mission-Critical Service Operations Systems | High-Reliability Architecture & 24x7 SLA Delivery",
        "summary": "**Systems engineering manager and operations leader** with deep experience building and managing 24x7 mission-critical software platforms, enterprise service applications, and operational integration tiers. Successfully established formal **24x7 on-call rotations, incident response protocols, and severity escalation tiers across 10–15 engineers**, ensuring flawless operational reliability.",
        "expertise": [
            "Service Operations Systems Leadership",
            "24x7 Mission-Critical Operational SLA Delivery",
            "Engineering People Management & Incident Triage",
            "Enterprise Systems & Middleware Integration",
            "Change Management & FinOps Governance (80% gain)",
            "Cloud Infrastructure & Distributed Architecture",
            "Relational Database Modeling & SQL",
            "Cross-Functional Stakeholder Alignment",
        ],
        "skills": [
            Labeled("Operations & Systems Management:", "24x7 incident operations, on-call rotation management, post-incident reviews (PIR), SLA tracking, Change Management, enterprise business systems."),
            Labeled("Cloud, Middleware & Architecture:", "Enterprise middleware, distributed services, MS Azure, AWS Serverless, Kubernetes, GitOps, CI/CD, REST APIs."),
            Labeled("Databases & Data Integrity:", "Oracle PL/SQL, SQL, PostgreSQL, MySQL, DynamoDB, high-availability transaction modeling."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Operational Tooling Leadership:", "**Accountable for end-to-end support, scaling, and operational maintenance of BlueStack IDP** supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Governance & Stability:", "**Core platform architecture leverages Kubernetes, GitHub Actions, and GitOps** for automated, audit-ready operational workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Operational Adherence & Velocity:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Operations:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Service Operations Management:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical systems across **10–15 engineers**."),
                    Labeled("Incident Triage & Severity Protocols:", "**Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs)** across a **10–15 person engineering team**."),
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
            ("Leading engineering for mission-critical service operations systems", "Managed 24x7 mission-critical operational systems and on-call tiers across 10–15 engineers at Blue Shield.", "Direct Match", "Direct match for high-stakes service operations leadership"),
            ("System reliability, incident management, and uptime SLAs", "Established formal 24x7 on-call rotations, severity escalations, and post-incident reviews.", "Direct Match", "Grounded in verified operational accomplishments"),
            ("Cross-functional business application integration", "Partnered across business units and engineering teams to integrate distributed enterprise applications.", "Direct Match", "Backed by verified facts"),
        ],
        "cited_facts": ["fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_02", "fact_safe_01"],
        "questions": [
            "What enterprise platforms (e.g. Salesforce, SAP, custom fleet dispatch services) comprise the core Service Operations Systems stack?",
            "How are on-call and live incident response workflows coordinated between software engineering and physical fleet depot personnel?",
            "What are the target SLAs for field telemetry ingestion and maintenance dispatch responsiveness?",
        ],
    },

    # 3. Zoox - Technical Program Manager, Product Software
    "job-7f54c878": {
        "slug": "zoox_tpm_product_software",
        "company": "Zoox",
        "title": "Technical Program Manager - Product Software",
        "headline": "Technical Program Manager | Product Software & Developer Platforms | Autonomous Systems Delivery & Scaled Execution",
        "summary": "**Principal technical program manager and software systems leader** with extensive background managing complex software platform delivery, cross-functional engineering execution, and release governance. Proven track record driving an **80% increase in Change Management and FinOps adherence**, accelerating deployment release cycles by **40%**, and coordinating technical roadmaps across distributed engineering teams.",
        "expertise": [
            "Technical Program Management (TPM)",
            "Product Software & Platform Roadmaps",
            "Cross-Functional Software Delivery",
            "Release Governance & Change Leadership (80% gain)",
            "Velocity & Workflow Automation (40% speed gain)",
            "Kubernetes & Cloud Infrastructure Platforms",
            "Risk Mitigation & Dependency Tracking",
            "Executive Stakeholder Communication",
        ],
        "skills": [
            Labeled("Program Delivery & Governance:", "Technical program management, software lifecycle methodologies, sprint coordination, dependency mapping, Change Management, FinOps governance, risk mitigation."),
            Labeled("Software Platforms & Cloud:", "Internal Developer Platforms (Backstage), Kubernetes, MS Azure, AWS Serverless, GitOps, CI/CD, GitHub Actions, Docker."),
            Labeled("Languages & Systems:", "Python, JavaScript, Rust, SQL, REST APIs, microservices, Linux environment."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, Cross-Functional Collaboration, Vendor Management."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Product Software Program Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, coordinating platform feature delivery for **80–100 internal developers and stakeholders**."),
                    Labeled("Automated Deployment Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Program Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Complex Platform Delivery:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("High-Reliability Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
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
            ("Leading technical programs across product software and platforms", "Directed platform delivery for 80–100 engineers with 40% speed gain and 80% governance adherence.", "Direct Match", "Showcased quantitative TPM impact across complex software stacks"),
            ("Cross-functional dependency and risk management", "Gathered requirements and partnered across matrixed engineering squads to align release milestones.", "Direct Match", "Demonstrated cross-functional leadership"),
            ("High technical depth in software systems", "Deep background in Kubernetes, GitOps, CI/CD, Python, and distributed software architectures.", "Direct Match", "Backed by verified technical facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What are the major software milestones leading up to upcoming commercial robotaxi market expansions?",
            "How are TPMs integrated with autonomous vehicle feature teams versus platform and safety verification teams?",
            "What tooling is standardized for release gating and cross-functional dependency tracking across software and hardware?",
        ],
    },

    # 4. Zoox - Senior/Staff Design Project Manager, Places & Build
    "job-3a96f885": {
        "slug": "zoox_design_pm_places_build",
        "company": "Zoox",
        "title": "Senior/Staff Design Project Manager, Places & Build",
        "headline": "Senior Technical Project Manager | Infrastructure Builds, Vendor Management & Large-Scale Deployment",
        "summary": "**Senior technical project manager and infrastructure delivery leader** with extensive track record directing multi-million dollar capital programs, vendor contracts, and enterprise deployment initiatives. Proven success managing complex schedules, driving an **80% increase in FinOps and Change Management adherence**, and leading cross-functional teams to execute high-stakes physical and technical infrastructure milestones.",
        "expertise": [
            "Technical Infrastructure Project Management",
            "Capital Program Delivery & Budget Governance",
            "Vendor Management & Contract Negotiation",
            "Change Leadership & Regulatory Compliance",
            "Cross-Functional Team Collaboration",
            "Schedule Management & Milestones Tracking",
            "High-Reliability Operational Excellence",
            "Executive Stakeholder Consulting",
        ],
        "skills": [
            Labeled("Project Management & Delivery:", "Infrastructure project lifecycle, vendor management, contract negotiation, budget tracking, Microsoft Project, Change Management, FinOps governance."),
            Labeled("Operations & Governance:", "Regulatory Compliance, risk mitigation, audit readiness, SLA tracking, executive status reporting, physical and technical systems integration."),
            Labeled("Key Leadership Skills:", "Team Building and Management, Budgeting, Change Leadership, Cross-Functional Collaboration, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Infrastructure Program Delivery:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, governing delivery milestones for **80–100 internal developers and stakeholders**."),
                    Labeled("Operational Accountability:", "**Accountable for end-to-end support, scaling, and operational maintenance of platform toolchains**, coordinating cross-functional execution."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Budget & Governance Adherence:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment turnaround by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Stakeholder Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Complex Program Execution:", "**Accountable for end-to-end infrastructure design and execution plan** supporting large-scale enterprise transformation."),
                    Labeled("High-Stakes Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**."),
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
            ("Managing complex multi-stakeholder capital and build projects", "Led multi-million dollar enterprise infrastructure and platform delivery across matrixed organizations.", "Direct Match", "Highlighted rigorous project management, budgeting, and delivery execution"),
            ("Budget governance and change management", "Drove 80% increase in FinOps and Change Management adherence across technical programs.", "Direct Match", "Grounded in verified quantitative metrics"),
            ("Vendor management and contract negotiation", "Extensive experience negotiating contracts, managing vendors, and ensuring compliance.", "Direct Match", "Backed by verified master resume competencies"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What specific facilities portfolio (e.g. vehicle depot buildouts, engineering offices, manufacturing expansion) is prioritized for this role?",
            "How does Places & Build coordinate with local city permitting, environmental safety, and autonomous fleet operations?",
            "What architectural design and project controls software (e.g. AutoCAD, Revit, Procore) are standardized across the team?",
        ],
    },

    # 5. Zoox - Manager, Enterprise Applications
    "job-6eb18c4c": {
        "slug": "zoox_mgr_enterprise_applications",
        "company": "Zoox",
        "title": "Manager, Enterprise Applications",
        "headline": "Engineering Manager | Enterprise Applications & Middleware Platforms | Cloud Integration, Governance & Operational Excellence",
        "summary": "**Enterprise applications engineering manager and platform architect** with extensive background directing enterprise application development, business systems integrations, and mission-critical cloud infrastructure. Built and managed 24x7 operational on-call teams of 10–15 engineers, scaled developer platforms for 80–100 users, and achieved an **80% increase in FinOps and Change Management adherence**.",
        "expertise": [
            "Enterprise Applications Engineering Leadership",
            "Middleware & Business Systems Integration",
            "24x7 Mission-Critical Operational SLAs",
            "Engineering Team Management & Hiring",
            "Cloud Platforms & Architecture (Azure / AWS)",
            "Change Leadership & FinOps Governance (80% gain)",
            "Relational Database Architecture & SQL",
            "Vendor Management & Contract Negotiation",
        ],
        "skills": [
            Labeled("Enterprise Applications & Middleware:", "Enterprise application architecture, business systems integration, REST APIs, enterprise middleware, microservices, system modeling."),
            Labeled("Cloud Platforms & DevOps:", "MS Azure, AWS Serverless, Kubernetes, Backstage IDP, GitOps, CI/CD, GitHub Actions, Docker, SonarQube."),
            Labeled("Databases & Data Integrity:", "Oracle PL/SQL, SQL, PostgreSQL, MySQL, DynamoDB, Transact-SQL, schema design, high-availability data tiers."),
            Labeled("Key Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, Vendor Management, Contract Negotiation."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform & Applications Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and supporting enterprise toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Scalable Deployment Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Governance & Efficiency:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy:", "**Gathered business requirements and partnered across internal cross-functional organizations** to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Enterprise Applications & Middleware:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical systems across **10–15 engineers**."),
                    Labeled("Major Application Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
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
            ("Leading engineering teams building enterprise business applications", "Managed enterprise application middleware and platforms supporting 80–100 engineers.", "Direct Match", "Direct match for enterprise applications engineering leadership"),
            ("High-reliability 24x7 operational uptime and incident response", "Built and led 24x7 on-call rotations and severity escalation tiers across 10–15 engineers.", "Direct Match", "Demonstrated operational rigor and people leadership"),
            ("Governance, FinOps, and vendor management", "Achieved 80% increase in FinOps and Change Management adherence; extensive vendor oversight.", "Direct Match", "Backed by verified governance facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What core enterprise applications (e.g. Workday, Coupa, ServiceNow, Jira, Salesforce) fall under this team's architectural purview?",
            "How does Enterprise Applications partner with InfoSec and Data Governance teams on zero-trust access controls?",
            "What are the major enterprise application migration and consolidation priorities for the coming fiscal year?",
        ],
    },

    # 6. Samsara - Sr. Software Engineer II, DevEx
    "job-fb1095fc": {
        "slug": "samsara_sr_swe_devex",
        "company": "Samsara",
        "title": "Sr. Software Engineer II, DevEx",
        "headline": "Staff / Senior Software Engineer II – Developer Experience (DevEx) | CI/CD, GitOps & Internal Platforms | Automated SDLC & AI Tooling",
        "summary": "**Senior Developer Experience (DevEx) and platform engineering leader** with deep expertise architecting enterprise CI/CD systems, internal developer platforms (IDP), and automated SDLC workflows. Proven track record leading **BlueStack IDP** for **80–100 engineers**, accelerating deployment cycle times by **40%**, scaling GitOps and Kubernetes automation, and building hands-on AI agent workflows in Python to eliminate developer friction.",
        "expertise": [
            "Developer Experience (DevEx) & Platform Engineering",
            "CI/CD Systems & GitOps Automation (Kargo, ArgoCD)",
            "Deployment Cycle Time Acceleration (40% speed gain)",
            "AI-Assisted Workflows & Agentic Tooling (Python, Copilot)",
            "Kubernetes & Cloud Infrastructure (Azure / AWS Serverless)",
            "Internal Developer Platforms (Backstage IDP)",
            "Production Safeguards, SonarQube & Governance (80% gain)",
            "Enterprise Scale (80–100 engineers, 24x7 systems)",
        ],
        "skills": [
            Labeled("Developer Experience & Platforms:", "Internal Developer Platforms (Backstage), CI/CD, GitOps, Kubernetes, ArgoCD, Kargo, GitHub Actions, Bitbucket Pipelines, Atlantis/OpenTofu, SonarQube, Artifactory."),
            Labeled("Programming & Automation:", "Python, Go/Rust familiarity, Shell scripting, JavaScript, C, Java, REST APIs, custom Python agents, n8n, Ollama, OpenAI Codex, GitHub Copilot."),
            Labeled("Cloud & Infrastructure:", "MS Azure, AWS Serverless, Docker, Linux environment, high-reliability architecture, FinOps governance."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, AI Implementation, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("DevEx & Platform Engineering Leadership:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipelines, and supporting developer toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("SDLC & Release Automation Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure deployment, GitOps sync, and rapid pull-request to production workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment turnaround by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Automation & Safe Delivery Strategies:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automated infrastructure as code (IaC) and standardized quality guardrails."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Production Safeguards & Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of mission-critical systems across **10–15 engineers**, establishing severity escalation and operational incident response."),
                    Labeled("Enterprise Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting major digital platform transition and rewrite."),
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
            ("Architecting and scaling CI/CD platforms and developer experience (DevEx)", "Architected and managed BlueStack IDP and CI/CD pipelines (GitHub Actions, ArgoCD, Kargo) for 80–100 engineers.", "Direct Match", "Direct match for DevEx platform architecture and developer scaling"),
            ("Accelerating deployment velocity and eliminating developer friction", "Improved developer deployment times by 40% while driving an 80% increase in FinOps and Change Management adherence.", "Direct Match", "Quantified 40% velocity improvement grounded in verified facts"),
            ("AI-enabled developer automation and Python tooling", "Hands-on implementation of custom Python AI agents, OpenAI Codex, Copilot, and automated workflows.", "Direct Match", "Aligns with hands-on AI SDLC tooling while strictly respecting exploratory fact boundaries"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How do the DevEx ('outer-loop') and Dev Agents ('inner-loop') teams coordinate on PR metadata and local sandbox validation?",
            "What are the primary metrics used at Samsara to evaluate AI auto-approval accuracy and prevent regression risks?",
            "What CI engine powers the in-house CI/CD pipeline today (e.g. Buildkite, custom Kubernetes runners), and what are the main scaling bottlenecks with current PR throughput?",
        ],
    },

    # 7. Blue Shield of California - Director, Product Management, Personalization
    "job-0be9317c": {
        "slug": "bsc_director_pm_personalization",
        "company": "Blue Shield of California",
        "title": "Director, Product Management, Personalization",
        "headline": "Director of Product Management | Member Engagement, Personalization & Healthcare Platforms | Enterprise Digital Transformation & Applied AI",
        "summary": "**Healthcare product and technology leader** with extensive track record directing enterprise digital transformation, **member engagement platforms**, and cross-functional technology initiatives at **Blue Shield of California**. Accountable for the architecture and modernization of the **Blue Shield Member Portal**, delivered internal developer platforms accelerating delivery by **40%**, increased FinOps/governance adherence by **80%**, and champions responsible **applied AI workflows** across enterprise scale.",
        "expertise": [
            "Healthcare Member Engagement & Personalization",
            "Digital Transformation & Member Portal Delivery",
            "Product Strategy, Roadmaps & Enterprise Blueprints",
            "Applied AI & Agentic Workflow Evaluation",
            "Cross-Functional Alignment (Clinical, Tech, Operations)",
            "Change Leadership & FinOps Governance (80% gain)",
            "People Management, Coaching & Team Building",
            "Enterprise Architecture & Cloud Modernization",
        ],
        "skills": [
            Labeled("Product Strategy & Governance:", "Digital product roadmaps, member experience strategy, business architecture blueprints, FinOps governance, Change Leadership, regulatory compliance, HIPAA."),
            Labeled("Platforms, AI & Data Systems:", "Blue Shield Member Portal, Internal Developer Platforms (IDP), MS Azure, AWS Serverless, custom Python agents, OpenAI Codex, Copilot, REST APIs, SQL, relational data modeling."),
            Labeled("Leadership & Delivery:", "Team Building and Management, Cross-Functional Collaboration, Executive Stakeholder Consulting, Vendor Management, Contract Negotiation, Budgeting."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Product Leadership:", "**Managing engineering and product delivery team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipelines, and enterprise developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Architecture & Governance:", "**Directing core platform architecture leveraging Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Cross-Functional Transformation & Efficiency:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving delivery turnaround times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Strategic Requirements & Governance:", "**Gathered business requirements and partnered across internal cross-functional organizations** (technology, clinical operations, finance) to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Member Portal Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, elevating digital self-service."),
                    Labeled("Team Leadership & Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and operational incident response."),
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
            ("Driving member engagement, personalization, and digital transformation at Blue Shield", "Architected and delivered the comprehensive rewrite of the Blue Shield Member Portal and led enterprise cloud transformations.", "Direct Match", "Decade of proven institutional leadership and delivery at Blue Shield of California"),
            ("Leading product and engineering teams with strong governance and financial rigor", "Managed 10-15 engineers on 24x7 operations, directed IDP teams for 80-100 users, and drove 80% FinOps adherence.", "Direct Match", "Verified governance and team leadership metrics"),
            ("Championing applied AI and agentic automation workflows", "Hands-on experience building custom Python agents, evaluating Copilot and Codex, and driving automation strategies.", "Direct Match", "Pragmatic applied AI experience respecting strict factual boundaries"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How are clinical data models and real-time claims/benefits feeds currently unified for personalization in the Member Portal?",
            "What are the priority omnichannel member touchpoints (e.g. mobile app, SMS, web, care management) targeted for agentic AI orchestration in 2026?",
            "How does the Personalization team partner with Information Security and Compliance on HIPAA-compliant agentic AI guardrails?",
        ],
    },

    # 8. Perplexity AI - Engineering Manager (API Platform)
    "job-a2ea5040": {
        "slug": "perplexity_em_api_platform",
        "company": "Perplexity AI",
        "title": "Engineering Manager (API Platform)",
        "headline": "Engineering Manager | Developer & API Platforms | High-Reliability Distributed Systems, Python/Rust & Applied AI",
        "summary": "**Engineering manager and API platform leader** with extensive track record building and scaling developer-facing platforms, mission-critical API services, and automated distributed systems. Directed engineering teams operating the **BlueStack platform for 80–100 engineers**, led **24x7 high-reliability operations across 10–15 engineers**, and brings authentic technical fluency in **Python, Rust, and hands-on AI agent orchestration**.",
        "expertise": [
            "API Platform & Developer Tooling Engineering Leadership",
            "High-Traffic Distributed Systems & Microservices",
            "24x7 Mission-Critical Operational Reliability & Incident Triage",
            "AI Agent Orchestration & Applied Automation (Python)",
            "Engineering Team Mentorship, Hiring & Career Growth",
            "Schema Evolution, REST APIs & Data Integrity",
            "GitOps, Kubernetes & Cloud Architecture (Azure / AWS)",
            "Developer Velocity & Tooling (40% deployment speedup)",
        ],
        "skills": [
            Labeled("API & Developer Platforms:", "REST APIs, API platform design, Backstage IDP, Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, microservices architecture, developer tooling."),
            Labeled("Languages & Automation:", "Python, Rust, JavaScript, C, Java, Shell scripting, custom Python AI agents, OpenAI Codex, GitHub Copilot, Ollama, n8n."),
            Labeled("Cloud, Databases & Operations:", "MS Azure, AWS Serverless, Docker, PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema versioning, 24x7 production operations."),
            Labeled("Leadership & Management:", "Engineering Team Management, Technical Direction, Hiring & Mentorship, 24x7 Production Operations, Change Leadership, Cross-Functional Execution."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("API & Developer Platform Management:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("High-Velocity Platform Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure, API integrations, and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Strategic Automation Solutions:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Operational Reliability & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** of business-critical systems across **10–15 engineers**, establishing severity escalation and incident response."),
                    Labeled("Mission-Critical Web & API Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
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
            ("Managing engineering teams building developer and API platforms", "Managed engineering teams building BlueStack developer platforms for 80–100 engineers and led 24x7 operations across 10–15 engineers.", "Direct Match", "Direct match for platform engineering management and team scaling"),
            ("High-traffic API reliability, schema evolution, and 24x7 operations", "Built and led 24x7 on-call rotations, incident management, and architectural modernization for enterprise member portal.", "Direct Match", "Demonstrated high-scale production reliability and operational rigor"),
            ("Technical depth in Python, modern AI agents, and emerging tools", "Hands-on implementation of custom Python agents, Rust familiarity, Copilot/Codex integration, and automated CI/CD.", "Direct Match", "Strong technical fluency combined with seasoned engineering leadership"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How is the API Platform team architecting rate limiting, streaming responses, and quota management for high-concurrency agentic workloads?",
            "What are the primary metrics Perplexity uses to track API platform reliability, latency p99s, and developer adoption across enterprise tiers?",
            "How do the API Platform and Model/Search Infrastructure teams collaborate on API contract versioning as model capabilities evolve?",
        ],
    },

    # 9. Perplexity AI - Product Manager (Builder)
    "job-453e57ff": {
        "slug": "perplexity_pm_builder",
        "company": "Perplexity AI",
        "title": "Product Manager (Builder)",
        "headline": "Technical Product Manager & Platform Leader | Enterprise Productivity & Developer Platforms | Applied AI & Agentic Systems",
        "summary": "**Technical product manager and platform engineering leader** with deep experience envisioning, architecting, and delivering developer productivity platforms and enterprise software. Led the product roadmap for the **BlueStack Internal Developer Platform** supporting **80–100 engineers**, accelerating deployment cycle times by **40%**, driving an **80% increase in FinOps and governance adherence**, and actively experimenting with **agentic AI workflows in Python**.",
        "expertise": [
            "Technical Product Management & Roadmaps",
            "Developer Experience & Productivity Platforms (40% speedup)",
            "Enterprise Systems & Healthcare Domain Expertise",
            "Agentic AI & Nondeterministic Workflow Evaluation",
            "Cross-Functional Collaboration (Design, Eng, Research)",
            "Data-Driven Flywheels & FinOps Governance (80% gain)",
            "Iterative Prototyping & Technical Architecture",
            "Platform Scaling & User Feedback Loops",
        ],
        "skills": [
            Labeled("Product Management & Platforms:", "Technical product strategy, PRDs, roadmaps, Internal Developer Platforms (Backstage), CI/CD, GitOps, Kubernetes, data-driven flywheels, user feedback loops."),
            Labeled("AI & Software Prototyping:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, n8n workflow automation, REST APIs, SQL, schema modeling."),
            Labeled("Cloud & Infrastructure:", "MS Azure, AWS Serverless, Docker, distributed architecture, FinOps governance, enterprise reliability."),
            Labeled("Leadership & Delivery:", "Team Building and Management, Cross-Functional Collaboration, Budgeting, Change Leadership, Executive Stakeholder Consulting."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Product & Platform Ownership:", "**Managing engineering and platform product delivery for BlueStack IDP**, directing feature roadmaps, developer toolchains, and automated workflows supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern System Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Productivity Gains:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment cycle times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Requirements & Cross-Functional Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align product strategy, increase governance, and optimize operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Major Digital Platform Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal, modernizing digital self-service."),
                    Labeled("Operational Leadership & Rigor:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident management."),
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
            ("Technical product management for productivity and developer platforms", "Led product and engineering direction for BlueStack IDP supporting 80–100 engineers with 40% velocity improvement.", "Direct Match", "Direct match for technical product ownership and developer productivity platforms"),
            ("Anticipating enterprise needs and delivering data-driven flywheels", "Partnered across matrixed enterprise organizations driving 80% increases in FinOps and Change Management adherence.", "Direct Match", "Demonstrated enterprise requirements synthesis and quantitative governance"),
            ("Applied AI experimentation and steering agentic systems", "Hands-on exploration building custom Python agents, evaluating Copilot and Codex, and designing automated workflows.", "Direct Match", "Pragmatic, truthful applied AI perspective grounded in hands-on building"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How does the Computer product team balance core consumer research workflows with enterprise-specific agent integrations?",
            "What telemetry and evaluation harnesses are used to measure user intent fulfillment and steer nondeterministic agent outputs?",
            "What are the key product-led growth levers for Computer adoption across technical vs. non-technical enterprise personas?",
        ],
    },

    # 10. Perplexity AI - Member of Technical Staff (Software Engineer, Computer)
    "job-d77f7aaf": {
        "slug": "perplexity_mts_swe_computer",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (Software Engineer, Computer)",
        "headline": "Member of Technical Staff / Software Engineer | Systems, Platforms & Applied AI | Python, Rust, Cloud Architecture & Agentic Tooling",
        "summary": "**Hands-on systems and platform software engineer** with deep experience building resilient production software, automated developer platforms, and cloud infrastructure. Brings authentic polyglot fluency in **Python, Rust, JavaScript, and C**, a track record scaling the **BlueStack platform for 80–100 developers** with **40% faster deployment velocity**, and active hands-on development building **custom Python AI agents and automation harnesses**.",
        "expertise": [
            "High-Performance Systems & Production Software",
            "Polyglot Engineering (Python, Rust, JavaScript, C)",
            "Developer Platforms & GitOps Automation (Kargo, ArgoCD)",
            "AI Agent Tooling & Applied LLM Workflows (Python, Ollama)",
            "Cloud Architecture & Kubernetes (Azure / AWS Serverless)",
            "Deployment Cycle Optimization (40% speed gain)",
            "Relational Data Modeling, Schemas & SQL",
            "High-Reliability Production Systems (24x7)",
        ],
        "skills": [
            Labeled("Languages & Systems:", "Python, Rust, JavaScript, C, Java, Shell scripting, Linux systems, microservices, REST APIs, 3D real-time systems."),
            Labeled("Platforms & Cloud Infrastructure:", "Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Backstage IDP, Docker, MS Azure, AWS Serverless, Atlantis/OpenTofu, SonarQube."),
            Labeled("Applied AI & Automation:", "Custom Python agents, OpenAI Codex, GitHub Copilot, Ollama, workflow automation (n8n), Ansible, prompt harnesses."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Engineering & Systems Architecture:", "**Directing and operating BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Cloud & GitOps Stack:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Automation Velocity & Guardrails:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Engineering:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("High-Scale Web & API Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
                    Labeled("24x7 Reliability & Escalations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
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
            ("Designing, building, and operating production systems at meaningful scale", "Operated BlueStack developer platform for 80–100 engineers and built 24x7 high-reliability infrastructure.", "Direct Match", "Extensive track record delivering rock-solid production systems"),
            ("Proficiency in general-purpose languages (Python, Rust, JavaScript, C)", "Hands-on experience in Python, Rust, JavaScript, C, and Java across enterprise platforms and high-performance systems.", "Direct Match", "Polyglot technical depth verified in master facts"),
            ("Genuine adoption and building of AI systems and agents", "Hands-on implementation of custom Python agents, Copilot/Codex integration, and exploratory AI workflow harnesses.", "Direct Match", "Authentic applied AI practitioner matching Perplexity's builder culture"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How are agent sandboxes and context retrieval boundaries isolated within the Computer runtime architecture?",
            "What are the primary performance and latency benchmarks for multi-step agent actions on the Computer platform?",
            "How does the Computer team evaluate model execution failures vs. environmental/DOM interaction failures?",
        ],
    },

    # 11. Perplexity AI - Member of Technical Staff (Software Engineer, Design System)
    "job-0187aa6c": {
        "slug": "perplexity_mts_design_system",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (Software Engineer, Design System)",
        "headline": "Member of Technical Staff / Frontend Engineer | Design Systems, Component Libraries & Accessibility | Web Architecture, JavaScript & UI Tokens",
        "summary": "**Senior frontend and design systems engineer** with extensive track record building scalable UI architectures, component libraries, and accessible web platforms. Architected frontend systems for the **Blue Shield Member Portal rewrite**, scaled internal developer portal components supporting **80–100 engineers**, and brings deep expertise in **JavaScript, CSS, HTML5, design tokens, and WCAG accessibility standards**.",
        "expertise": [
            "Design Systems & Component Architecture",
            "Frontend Web Engineering (JavaScript, CSS, HTML5)",
            "Design Tokens & Cross-Platform UI Primitives",
            "Web Accessibility Standards (WCAG & ARIA)",
            "Digital Portal Modernization & Member Experience",
            "Developer Experience & Shared UI Scaffolding",
            "Iterative Prototyping & Visual Consistency",
            "Enterprise Scale (80–100 internal developers)",
        ],
        "skills": [
            Labeled("Frontend & Design Systems:", "JavaScript, CSS, HTML5, component library architecture, design tokens, UI primitives, cross-browser compatibility, WCAG/ARIA accessibility."),
            Labeled("Platforms & Developer Toolchains:", "Backstage UI, React/web architecture, GitOps, GitHub Actions, CI/CD, SonarQube, internal developer tooling."),
            Labeled("Languages & Systems:", "Python, Rust, C, REST APIs, JSON schemas, web performance optimization."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Shared UI & Developer Platform Components:", "**Managing engineering team operating BlueStack IDP and developer portal**, integrating Backstage UI primitives, standardized plugins, and developer toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Continuous Integration & UI Scaffolding:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Standardization:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automated infrastructure as code (IaC) and consistent developer standards."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Member Portal Digital Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, modernizing web UI self-service and accessibility."),
                    Labeled("Operational Reliability & Team Leadership:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident response."),
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
            ("Building production design systems and shared component libraries", "Led UI modernization for the Blue Shield Member Portal and built shared developer portal plugins for 80–100 engineers.", "Direct Match", "Extensive experience delivering scalable, consistent web UI systems"),
            ("Frontend fluency in JavaScript, CSS, and accessible web primitives", "Deep technical grounding in JavaScript, CSS, HTML5, and WCAG accessibility standards across consumer-facing portals.", "Direct Match", "Grounded in verified master facts and web portal delivery"),
            ("Developer empathy and cross-team adoption support", "Improved developer turnaround times by 40% through standardized developer platforms and reusable scaffolds.", "Direct Match", "Verified 40% developer productivity improvement"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How is the design token pipeline currently architected across web and native platforms (iOS, macOS, Android, Windows)?",
            "What automated visual regression and accessibility testing harnesses are integrated into Perplexity's PR review pipeline?",
            "How do design system engineers partner with product teams to deprecate legacy bespoke components without introducing breaking changes?",
        ],
    },

    # 12. Perplexity AI - Member of Technical Staff (Software Engineer, Backend Platform)
    "job-f3023a93": {
        "slug": "perplexity_mts_backend_platform",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (Software Engineer, Backend Platform)",
        "headline": "Member of Technical Staff / Backend Engineer | Distributed Systems & Platform Infrastructure | Python, Rust, Kubernetes & High-Reliability Architecture",
        "summary": "**Backend platform and distributed systems engineer** with deep experience building resilient cloud infrastructure, automated execution platforms, and enterprise security controls. Directed and operated the **BlueStack platform for 80–100 engineers**, architected 24x7 mission-critical systems across **10–15 engineers**, and brings strong technical depth in **Python, Rust, Kubernetes, GitOps, and sandboxed automation**.",
        "expertise": [
            "Backend Platform Engineering & Distributed Systems",
            "Sandboxing & Secure Automated Execution",
            "Kubernetes & Cloud Infrastructure (Azure / AWS)",
            "GitOps & CI/CD Automation (Kargo, ArgoCD)",
            "High-Reliability 24x7 Operations & Incident Response",
            "Access Controls, Governance & Compliance (80% gain)",
            "Polyglot Systems Engineering (Python, Rust, C)",
            "Developer Velocity & Tooling (40% speed gain)",
        ],
        "skills": [
            Labeled("Backend Platforms & Cloud:", "Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Backstage IDP, Docker, MS Azure, AWS Serverless, Atlantis/OpenTofu, SonarQube."),
            Labeled("Languages & Systems:", "Python, Rust, C, Java, Shell scripting, Linux environment, REST APIs, microservices, 3D real-time systems."),
            Labeled("Databases & Security:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema design, RBAC, access controls, regulatory compliance."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Platform Infrastructure Operations:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Kubernetes & GitOps Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Governance Guardrails:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Automation:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 High-Reliability Operations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                    Labeled("Enterprise Architecture:", "**Accountable for end-to-end infrastructure design and execution plan** supporting major digital platform transition and rewrite."),
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
            ("Designing and building backend systems running reliably at scale", "Operated BlueStack developer platform for 80–100 engineers and built 24x7 high-reliability infrastructure.", "Direct Match", "Extensive track record delivering resilient backend systems"),
            ("Kubernetes, cloud infrastructure, and security controls", "Deep hands-on architecture with Kubernetes, Azure, AWS, and driving 80% adherence in governance.", "Direct Match", "Strong alignment on container orchestration and security controls"),
            ("Proficiency in Python and Rust for backend platforms", "Hands-on engineering in Python, Rust, C, and Java across enterprise platforms.", "Direct Match", "Polyglot technical depth verified in master facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How are code execution sandboxes isolated and monitored to prevent noisy neighbor and security risks at scale?",
            "What are the primary metrics used to monitor backend platform latency and availability across Perplexity's multi-cloud infrastructure?",
            "How does the Backend Platform team coordinate with Security on BYOK and key management workflows?",
        ],
    },

    # 13. Perplexity AI - Member of Technical Staff (Software Engineer, API Platform)
    "job-c38db86a": {
        "slug": "perplexity_mts_api_platform",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (Software Engineer, API Platform)",
        "headline": "Member of Technical Staff / Software Engineer | API Gateways, Paved Roads & Developer Platforms | Python, Rust, Kubernetes & GitOps",
        "summary": "**API platform and developer infrastructure engineer** with deep experience building mission-critical API routing tiers, paved-road developer platforms, and automated release pipelines. Directed and operated the **BlueStack platform for 80–100 engineers**, accelerated deployment velocity by **40%**, established 24x7 reliability across **10–15 engineers**, and brings strong technical depth in **Python, Rust, Kubernetes, GitOps, and contract-first API design**.",
        "expertise": [
            "API Gateways, Routing & Paved-Road Tooling",
            "Developer Platforms & GitOps Automation (Kargo, ArgoCD)",
            "Deployment Cycle Acceleration (40% speedup)",
            "Kubernetes & Cloud Infrastructure (Azure / AWS)",
            "High-Traffic API Design & Contract Governance",
            "24x7 Mission-Critical Operational Reliability",
            "Polyglot Systems Engineering (Python, Rust, C)",
            "Enterprise Governance & FinOps Adherence (80% gain)",
        ],
        "skills": [
            Labeled("API & Developer Platforms:", "REST APIs, API gateway architecture, Backstage IDP, Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Helm, container builds, SonarQube."),
            Labeled("Languages & Automation:", "Python, Rust, JavaScript, C, Java, Shell scripting, custom Python AI agents, OpenAI Codex, GitHub Copilot, Ollama, n8n."),
            Labeled("Databases & Cloud:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, MS Azure, AWS Serverless, Docker, schema versioning."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Paved-Road Platform Operations:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipelines, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Automated Deployment Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Developer Velocity & Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Automation:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Operational Reliability & Escalations:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                    Labeled("High-Scale Web & API Modernization:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the Blue Shield Member Portal."),
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
            ("Building paved roads, CI/CD pipelines, and API developer platforms", "Architected and operated BlueStack developer platform for 80–100 engineers with 40% velocity improvement.", "Direct Match", "Direct match for paved-road developer platform and CI/CD engineering"),
            ("API design, contract governance, and 24x7 operational reliability", "Led 24x7 operations across 10–15 engineers and architected enterprise member portal rewrite.", "Direct Match", "Proven operational rigor and high-scale production reliability"),
            ("Proficiency in Python and Rust for platform engineering", "Hands-on experience in Python, Rust, JavaScript, and C across enterprise platforms.", "Direct Match", "Polyglot technical depth verified in master facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What API gateway technologies (e.g. Envoy, Kong, custom Rust/Go proxy) are currently leveraged for request routing and rate limiting?",
            "How are breaking API changes caught and enforced in CI before schema updates reach production?",
            "What tooling is used to generate client SDKs and documentation from single-source-of-truth API contracts?",
        ],
    },

    # 14. Perplexity AI - Member of Technical Staff (Software Engineer, Integrations)
    "job-200d1cb6": {
        "slug": "perplexity_mts_integrations",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (Software Engineer, Integrations)",
        "headline": "Member of Technical Staff / Full-Stack & Integrations Engineer | Agentic Workflows & Enterprise Connectors | Python, JavaScript, PostgreSQL & Healthcare Domain Depth",
        "summary": "**Full-stack software and integrations engineer** with deep experience building mission-critical enterprise connectors, data pipelines, and workflow automation. Directed enterprise integration tiers, architected digital platforms at **Blue Shield of California**, led **BlueStack IDP for 80–100 engineers**, and builds hands-on **applied AI agent workflows and data connectors in Python and JavaScript**.",
        "expertise": [
            "Enterprise Integrations & Workflow Automation",
            "Full-Stack Web & Connectors (Python, JavaScript, SQL)",
            "Healthcare & Enterprise Operations Domain Expertise",
            "Agentic AI Applications & Custom Python Tooling",
            "Relational Data Modeling & PostgreSQL / MySQL",
            "High-Reliability Production Systems (99.9% / 24x7 SLAs)",
            "Cloud Architecture & Serverless (AWS / Azure)",
            "Technical Leadership & Cross-Functional Delivery",
        ],
        "skills": [
            Labeled("Integrations & Full-Stack:", "Enterprise API connectors, REST APIs, full-stack application development, Python, JavaScript, TypeScript/React fundamentals, HTML5, CSS, JSON schemas."),
            Labeled("Databases & Data Pipelines:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema design, high-reliability data pipelines, identity resolution."),
            Labeled("Cloud & Automation:", "AWS Serverless, MS Azure, Kubernetes, GitOps, GitHub Actions, custom Python AI agents, OpenAI Codex, GitHub Copilot, n8n, Ollama."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Regulatory Compliance, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Developer Integration & Connectors:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, integrating cross-system plugins, CI/CD pipelines, and supporting developer toolchains for **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Cloud Architecture:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Workflow Velocity & FinOps Adherence:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment turnaround by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Enterprise Requirements & Cross-Functional Alignment:", "**Gathered business requirements and partnered across internal cross-functional organizations** (healthcare operations, data, clinical) to increase system reliability, governance, and operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Digital Portal Modernization & Connectors:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, integrating disparate backend claims and eligibility data tiers."),
                    Labeled("24x7 Mission-Critical Reliability:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
                ],
            ),
            Role(
                company="Safeway Inc.",
                dates="April 2008 – May 2013",
                title="Integration Architect / Infrastructure Solution Engineer",
                bullets=[
                    Labeled("Enterprise Middleware & Integrations:", "**Designed and led strategic enterprise transformation** from legacy middleware to modern scalable database and WebLogic integration architecture."),
                ],
            ),
        ],
        "comparisons": [
            ("Building enterprise data connectors, workflows, and vertical integrations", "Led enterprise middleware integration and architected complete rewrite of the Blue Shield Member Portal data tier.", "Direct Match", "Extensive track record building enterprise connectors and data backbones"),
            ("Domain depth in healthcare and operations verticals", "10+ years directing healthcare payer systems, clinical data integrations, and enterprise operational governance.", "Direct Match", "Rare combination of healthcare domain depth and hands-on systems architecture"),
            ("Applied AI agent workflows and full-stack engineering", "Hands-on implementation of custom Python agents, Codex/Copilot tooling, and workflow automation in Python/JS.", "Direct Match", "Authentic applied AI practitioner matching Perplexity's builder culture"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "What connector protocols and auth standards (e.g. OAuth2, MCP, webhooks, zero-trust tokens) are used to connect user enterprise data to Computer agents?",
            "How are vertical-specific integrations (e.g. healthcare, finance) designed to maintain strict data privacy and tenant isolation within agent runtime sandboxes?",
            "What experimentation frameworks (e.g. Eppo) and adoption metrics are prioritized when rolling out new vertical workflow tools?",
        ],
    },

    # 15. Perplexity AI - Product Manager, Core Experience
    "job-69fc7954": {
        "slug": "perplexity_pm_core_experience",
        "company": "Perplexity AI",
        "title": "Product Manager, Core Experience",
        "headline": "Technical Product Manager | Core Experience & Knowledge Platforms | Developer Portals, Applied AI & Enterprise Transformation",
        "summary": "**Technical product manager and platform engineering leader** with extensive track record directing digital user experiences, developer portals, and cross-functional enterprise transformations. Led platform product delivery for the **BlueStack Internal Developer Platform** supporting **80–100 engineers**, accelerating delivery cycles by **40%**, driving an **80% increase in governance and FinOps adherence**, and championing intuitive, reliable **applied AI workflows in Python**.",
        "expertise": [
            "Core Digital Product Management & User Journeys",
            "Developer Experience & Productivity Platforms (40% gain)",
            "Enterprise Systems & Healthcare Domain Depth",
            "Applied AI & Agentic Interaction Design",
            "Cross-Functional Leadership (Design, Eng, Research)",
            "Data-Driven Flywheels & FinOps Governance (80% gain)",
            "Iterative Prototyping & Feedback Loops",
            "Digital Portal Modernization & Adoption",
        ],
        "skills": [
            Labeled("Product Management & Portals:", "Product strategy, user journey mapping, PRDs, roadmaps, Internal Developer Platforms (Backstage), member self-service portals, user feedback loops."),
            Labeled("AI & Prototyping:", "Python, custom AI agents, OpenAI Codex, GitHub Copilot, Ollama, workflow automation (n8n), REST APIs, SQL, schema modeling."),
            Labeled("Cloud & Governance:", "MS Azure, AWS Serverless, Docker, FinOps adherence, Change Leadership, regulatory compliance, enterprise reliability."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Core Platform Product Leadership:", "**Managing engineering and platform product delivery for BlueStack IDP**, directing core user experience, developer toolchains, and automated workflows supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Modern Architecture & Scaffolding:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("User Velocity & Governance Adoption:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving deployment cycle times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Cross-Functional Strategy & Requirements:", "**Gathered business requirements and partnered across internal cross-functional organizations** to align product strategy, increase governance, and optimize operational efficiency."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("Core Portal Transformation:", "**Accountable for end-to-end infrastructure design and execution plan** supporting the transition and complete rewrite of the **Blue Shield Member Portal**, elevating digital self-service."),
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
            ("Product management for core user experiences and platform portals", "Directed product direction for BlueStack IDP (80–100 engineers) and architected complete rewrite of the Blue Shield Member Portal.", "Direct Match", "Extensive track record delivering intuitive, mission-critical digital portals"),
            ("Data-driven flywheels and cross-functional leadership", "Drove 40% deployment speed gains and an 80% increase in FinOps and Change Management adherence across enterprise organizations.", "Direct Match", "Demonstrated quantitative product impact and enterprise alignment"),
            ("Applied AI interaction design and exploratory workflows", "Hands-on exploration building custom Python agents, evaluating Copilot and Codex, and designing automated workflows.", "Direct Match", "Pragmatic applied AI perspective grounded in hands-on building"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_03", "fact_bsc_mid_01", "fact_bsc_mid_04", "fact_safe_01"],
        "questions": [
            "How is user intent and session context persisted across multi-turn research workflows on web and desktop surfaces?",
            "What quantitative metrics and qualitative research loops does the Core Experience team use to evaluate answer trustworthiness?",
            "How do the Core Experience and Computer teams coordinate on shared navigation patterns and modal states?",
        ],
    },

    # 16. Perplexity AI - Member of Technical Staff (General Software Engineer, Infrastructure)
    "job-f9c7d501": {
        "slug": "perplexity_mts_infra",
        "company": "Perplexity AI",
        "title": "Member of Technical Staff (General Software Engineer, Infrastructure)",
        "headline": "Member of Technical Staff / Infrastructure Engineer | Cross-Cutting Cloud Platforms, Kubernetes & GitOps | Python, Rust, C & 24x7 Reliability",
        "summary": "**Cross-cutting systems and infrastructure engineer** with extensive track record building, scaling, and operating resilient cloud platforms, automated developer tooling, and distributed systems. Directed and operated the **BlueStack platform for 80–100 engineers**, accelerated deployment velocity by **40%**, maintained 24x7 mission-critical operations across **10–15 engineers**, and brings strong technical depth in **Python, Rust, C, Kubernetes, and GitOps**.",
        "expertise": [
            "Cross-Cutting Cloud Infrastructure & Distributed Systems",
            "Kubernetes & Cloud Platforms (Azure / AWS Serverless)",
            "GitOps & CI/CD Automation (Kargo, ArgoCD, GitHub Actions)",
            "Deployment Cycle Optimization (40% speed gain)",
            "24x7 High-Reliability Operations & Incident Triage",
            "FinOps Governance & Infrastructure as Code (80% gain)",
            "Polyglot Systems Engineering (Python, Rust, C, Java)",
            "Developer Infrastructure & Shared Abstractions",
        ],
        "skills": [
            Labeled("Cloud & Container Infrastructure:", "Kubernetes, GitOps, ArgoCD, Kargo, GitHub Actions, Backstage IDP, Docker, MS Azure, AWS Serverless, Atlantis/OpenTofu, SonarQube."),
            Labeled("Languages & Systems:", "Python, Rust, C, Java, Shell scripting, Linux environment, REST APIs, microservices, 3D real-time systems."),
            Labeled("Databases & Storage:", "PostgreSQL, MySQL, DynamoDB, Oracle PL/SQL, schema design, high-availability data tiers."),
            Labeled("Key Technical & Leadership Skills:", "Team Building and Management, 24x7 Production Operations, Budgeting, Change Leadership, Cross-Functional Collaboration."),
        ],
        "roles": [
            Role(
                company="Stellarus",
                dates="June 2025 – Present",
                title="Cloud Developer Platform Senior Manager / Principal Technologist",
                bullets=[
                    Labeled("Cross-Cutting Infrastructure Operations:", "**Managing engineering team responsible for operation and enhancement of BlueStack IDP**, CI/CD pipeline, and developer tools supporting **80–100 internal developers and stakeholders**."),
                    Labeled("Kubernetes & GitOps Foundation:", "**Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu** for automated infrastructure and rapid deployment workflows."),
                ],
            ),
            Role(
                company="Blue Shield of California / Stellarus",
                dates="January 2021 – June 2025",
                title="Principal Technologist - Cloud and Automation",
                bullets=[
                    Labeled("Platform Velocity & FinOps Governance:", "**Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption**, improving developer deployment times by **40%** and increasing adherence to **FinOps and Change Management by 80%**."),
                    Labeled("Infrastructure as Code Automation:", "**Designed and developed solutions and enterprise strategies to increase efficiencies** through automation and infrastructure as code (IaC)."),
                ],
            ),
            Role(
                company="Blue Shield of California",
                dates="May 2013 – January 2021",
                title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
                bullets=[
                    Labeled("24x7 Mission-Critical Reliability:", "**Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy** across **10–15 engineers**, establishing severity escalation and incident triage."),
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
            ("Owning cross-cutting infrastructure spanning compute, deployment, and reliability", "Operated BlueStack developer platform for 80–100 engineers and built 24x7 high-reliability infrastructure.", "Direct Match", "Extensive track record delivering rock-solid cross-cutting platforms"),
            ("Kubernetes, cloud platforms (Azure/AWS), and GitOps automation", "Architected and scaled GitOps pipelines (ArgoCD, Kargo, GitHub Actions) and automated infrastructure via OpenTofu.", "Direct Match", "Direct match for modern cloud infrastructure stack"),
            ("Polyglot depth in Python, Rust, and systems languages", "Hands-on engineering in Python, Rust, C, and Java across enterprise platforms and real-time systems.", "Direct Match", "Polyglot technical depth verified in master facts"),
        ],
        "cited_facts": ["fact_stell_01", "fact_stell_02", "fact_stell_03", "fact_bsc_stell_01", "fact_bsc_stell_02", "fact_bsc_mid_01", "fact_safe_01"],
        "questions": [
            "How are cross-cloud networking and egress costs optimized between Perplexity's training clusters and inference serving tiers?",
            "What shared abstractions are used to standardize canary rollouts and automated rollback triggers across disparate Kubernetes clusters?",
            "How does the Infrastructure team balance fast iteration for research/AI workloads with 99.9%+ availability SLAs for enterprise API traffic?",
        ],
    },
}






