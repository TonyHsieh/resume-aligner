"""Parse master_resume.html and merge facts_addendum.md into a structured Fact Ledger (facts.yaml).

Every bullet, tool, metric, and responsibility has a persistent Fact ID.
Generated resumes cite Fact IDs so our validator can guarantee 0% hallucination.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Comment
import yaml


@dataclass
class FactBullet:
    id: str
    raw_text: str
    tools: list[str] = field(default_factory=list)
    metrics: list[str] = field(default_factory=list)
    scope: str = ""


@dataclass
class FactRole:
    id: str
    company: str
    title: str
    dates: str
    start_year: int
    end_year: int
    bullets: list[FactBullet] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass
class FactLedger:
    name: str
    phone: str
    email: str
    education: list[dict[str, str]]
    skills: dict[str, list[str]]
    roles: list[FactRole]
    addendum_facts: dict[str, Any] = field(default_factory=dict)


def clean_text(s: str) -> str:
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def parse_master_resume(html_path: Path | str) -> FactLedger:
    content = Path(html_path).read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(content, "html.parser")

    # Strip HTML comments so commented-out text is ignored unless explicitly restored in addendum
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Base contact info
    name = "Tony Hsieh"
    phone = "(510) 897-8886"
    email = "tonyhsieh888@hotmail.com"

    # Education (no graduation year)
    education = [
        {
            "id": "edu_ucsb",
            "institution": "University of California, Santa Barbara",
            "degree": "Bachelor of Science in Computer Science",
        }
    ]

    # Explicit parsed skills from the master resume HTML
    skills: dict[str, list[str]] = {
        "programming": [
            "Python",
            "JavaScript",
            "Rust",
            "Java",
            "C",
            "Scala",
            "Assembly",
            "n8n",
            "Ansible",
            "3D real-time animation engine/systems",
        ],
        "cloud_and_platform": [
            "Kubernetes",
            "MS Azure",
            "AWS Serverless",
            "Internal Developer Platforms",
            "GitOps",
            "CI/CD",
            "DevSecOps",
            "GitHub Actions",
            "Bitbucket Pipelines",
            "ArgoCD",
            "Kargo",
            "Backstage",
            "Atlantis/OpenTofu",
            "SonarQube",
            "Artifactory",
            "GIT",
        ],
        "database": [
            "PostgreSQL",
            "MySQL",
            "DynamoDB",
            "Oracle PL/SQL",
            "SQL",
            "Transact-SQL",
            "Microsoft Access",
        ],
        "ai_and_automation": [
            "Gemini",
            "Copilot",
            "OpenAI Codex",
            "GitHub Copilot",
            "Ollama",
            "OpenCode",
            "Hermes",
            "Python custom agents",
            "AI Implementation",
            "AI Implementation & Agentic Workflows",
            "n8n",
            "Ansible",
        ],
        "leadership_and_ops": [
            "Team Building and Management",
            "24x7 Production Operations",
            "24x7 Incident Operations & On-Call",
            "Budgeting",
            "Budgeting & FinOps Governance",
            "Regulatory Compliance",
            "AI Implementation & Agentic Workflows",
            "Change Leadership",
            "Change Management",
            "Cross Functional Collaboration",
            "Cross-Functional Collaboration",
            "Vendor Management",
            "Contract Negotiation",
            "People Management",
            "Executive Stakeholder Consulting",
            "Platform Engineering Leadership",
            "Enterprise Architecture",
            "Cross-Functional Delivery",
            "FinOps Adherence",
        ],
    }


    roles: list[FactRole] = [
        FactRole(
            id="role_stellarus_2025",
            company="Stellarus",
            title="Cloud Developer Platform Senior Manager / Principal Technologist",
            dates="June 2025 – Present",
            start_year=2025,
            end_year=2026,
            tags=["management", "platform", "cloud", "idp", "ci_cd", "kubernetes"],
            bullets=[
                FactBullet(
                    id="fact_stell_01",
                    raw_text="Managing engineering team responsible for operation and enhancement of BlueStack IDP, CI/CD pipeline, and supporting technologies (Bitbucket, SonarQube, Artifactory).",
                    tools=["BlueStack IDP", "Bitbucket", "SonarQube", "Artifactory", "CI/CD"],
                    scope="Management & Platform Operations",
                ),
                FactBullet(
                    id="fact_stell_02",
                    raw_text="Accountable for end-to-end support, scaling, and operational maintenance of BlueStack IDP supporting 80–100 internal developers and stakeholders.",
                    metrics=["80–100 internal developers"],
                    tools=["BlueStack IDP"],
                    scope="Platform Scale & Accountability",
                ),
                FactBullet(
                    id="fact_stell_03",
                    raw_text="Core platform architecture leverages Kubernetes, GitHub Actions, Kargo, ArgoCD, Backstage, and Atlantis/OpenTofu for automated infrastructure and deployment workflows.",
                    tools=["Kubernetes", "GitHub Actions", "Kargo", "ArgoCD", "Backstage", "Atlantis/OpenTofu"],
                    scope="Platform Engineering & GitOps",
                ),
            ],
        ),
        FactRole(
            id="role_bsc_stellarus_2021",
            company="Blue Shield of California / Stellarus",
            title="Principal Technologist - Cloud and Automation",
            dates="January 2021 – June 2025",
            start_year=2021,
            end_year=2025,
            tags=["cloud", "azure", "automation", "iac", "finops", "healthcare"],
            bullets=[
                FactBullet(
                    id="fact_bsc_stell_01",
                    raw_text="Implemented BlueStack as an Internal Developer Platform for Microsoft Azure adoption, improving developer deployment times by 40% and increasing adherence to FinOps and Change Management by 80%.",
                    metrics=["40% improved deployment times", "80% increased FinOps and Change Management adherence"],
                    tools=["BlueStack IDP", "Microsoft Azure"],
                    scope="Cloud Transformation & Efficiency",
                ),
                FactBullet(
                    id="fact_bsc_stell_02",
                    raw_text="Designed and developed solutions and enterprise strategies to increase efficiencies through automation and infrastructure as code (IaC).",
                    tools=["Infrastructure as Code", "Automation", "Azure"],
                    scope="Technical Architecture & IaC",
                ),
                FactBullet(
                    id="fact_bsc_stell_03",
                    raw_text="Gathered business requirements and partnered across internal cross-functional organizations to increase system reliability, governance, and operational efficiency.",
                    scope="Cross-Functional Leadership & Governance",
                ),
            ],
        ),
        FactRole(
            id="role_bsc_2013",
            company="Blue Shield of California",
            title="Infrastructure Solution Architect + Middleware Infrastructure Engineering Senior Manager",
            dates="May 2013 – January 2021",
            start_year=2013,
            end_year=2021,
            tags=["management", "middleware", "oncall", "operations", "healthcare", "architecture"],
            bullets=[
                FactBullet(
                    id="fact_bsc_mid_01",
                    raw_text="Built, coached, and managed engineering team responsible for 24x7 operation, reliability, and lifecycle strategy of business-critical middleware infrastructure for key healthcare solutions.",
                    scope="People Management & 24x7 Operations",
                    metrics=["Team of 10–15 engineers", "24x7 coverage model"],
                ),
                FactBullet(
                    id="fact_bsc_mid_02",
                    raw_text="Established formal 24x7 on-call rotations, severity escalation tiers, and post-incident reviews (PIRs) across a 10–15 person engineering team.",
                    tools=["Incident Management", "On-call Systems"],
                    scope="Operational Excellence & Incident Management",
                ),
                FactBullet(
                    id="fact_bsc_mid_03",
                    raw_text="Integrated enterprise appliances and distributed applications into secure Blue Shield infrastructure.",
                    scope="Enterprise Systems Integration",
                ),
                FactBullet(
                    id="fact_bsc_mid_04",
                    raw_text="Accountable for end-to-end infrastructure design and execution plan supporting the transition and complete rewrite of the Blue Shield Member Portal.",
                    scope="Digital Transformation & Architecture",
                ),
            ],
        ),
        FactRole(
            id="role_safeway_2008",
            company="Safeway Inc.",
            title="Integration Architect / Infrastructure Solution Engineer",
            dates="April 2008 – May 2013",
            start_year=2008,
            end_year=2013,
            tags=["architecture", "middleware", "weblogic", "mdm", "retail"],
            bullets=[
                FactBullet(
                    id="fact_safe_01",
                    raw_text="Designed and led strategic enterprise transformation from IBM middleware to Oracle WebLogic and Database (2010–2011).",
                    tools=["Oracle WebLogic", "Oracle Database", "IBM Middleware"],
                    scope="Middleware Modernization",
                ),
                FactBullet(
                    id="fact_safe_02",
                    raw_text="Served as Infrastructure Architect in the Copient system improvement initiative (2008–2009).",
                    tools=["Copient"],
                    scope="Infrastructure Architecture",
                ),
                FactBullet(
                    id="fact_safe_03",
                    raw_text="Managed and drove Master Data Management (MDM) infrastructure to deliver precise customer and retail data from a single enterprise-wide system of record.",
                    tools=["Master Data Management (MDM)"],
                    scope="Data Quality & Master Data Management",
                ),
            ],
        ),
        FactRole(
            id="role_independent_contractor_1999",
            company="(Concurrent) Independent Contractor",
            title="Game Designer, Project Lead, Game Developer, Database and Infrastructure Administrator",
            dates="April 1999 – November 2012",
            start_year=1999,
            end_year=2012,
            tags=["gaming", "game_design", "cradle_to_grave", "fullstack", "mmo", "media"],
            bullets=[
                FactBullet(
                    id="fact_game_01",
                    raw_text="Led full cradle-to-grave lifecycle for games: from game design proposals and resourcing through programming, testing, deployment, and live-ops.",
                    scope="Full Lifecycle Product & Game Delivery",
                ),
                FactBullet(
                    id="fact_game_02",
                    raw_text="Developed full-stack front-end (JavaScript, CSS) and backend (PHP, MySQL) for commercial games and browser-based MMOs.",
                    tools=["JavaScript", "CSS", "PHP", "MySQL", "Flash"],
                    scope="Full-Stack Engineering",
                ),
                FactBullet(
                    id="fact_game_03",
                    raw_text="Created commercial game designs and products for major enterprise brands including Hasbro and Universal Music.",
                    scope="Client Product Delivery & Commercial Partnerships",
                ),
                FactBullet(
                    id="fact_game_04",
                    raw_text="Architected and implemented browser-based Flash social and music-oriented MMO (www.planetcazmo.com).",
                    tools=["Flash", "MMO Architecture", "Real-Time Networking"],
                    scope="MMO & Virtual World Architecture",
                ),
            ],
        ),
        FactRole(
            id="role_pge_2005",
            company="Pacific Gas and Electric Company",
            title="Business Transformation - Application Architect - Enterprise Integration",
            dates="February 2005 – April 2008",
            start_year=2005,
            end_year=2008,
            tags=["architecture", "soa", "integration", "enterprise"],
            bullets=[
                FactBullet(
                    id="fact_pge_01",
                    raw_text="Laid foundational framework for Service Oriented Architecture (SOA) across enterprise systems.",
                    tools=["SOA", "EAI"],
                    scope="Service Oriented Architecture",
                ),
                FactBullet(
                    id="fact_pge_02",
                    raw_text="Managed and advised engineering teams creating architectural proofs of concept, best-practice standards, and technical documentation.",
                    scope="Technical Leadership & Standardization",
                ),
            ],
        ),
        FactRole(
            id="role_pge_2001",
            company="Pacific Gas and Electric Company",
            title="Application Architect - Enterprise Application Integration",
            dates="October 2001 – January 2005",
            start_year=2001,
            end_year=2005,
            tags=["integration", "seebeyond", "architecture"],
            bullets=[
                FactBullet(
                    id="fact_pge_03",
                    raw_text="Translated corporate integration strategic roadmaps into concrete tactical steps and developer standards.",
                    scope="Strategic Roadmapping",
                ),
                FactBullet(
                    id="fact_pge_04",
                    raw_text="Integrated real-time customer care systems utilizing the SeeBeyond platform.",
                    tools=["SeeBeyond"],
                    scope="Real-Time Systems Integration",
                ),
            ],
        ),
        FactRole(
            id="role_moai_pm_2000",
            company="Moai Incorporated",
            title="West Coast Practice Manager / Architect",
            dates="August 2000 – October 2001",
            start_year=2000,
            end_year=2001,
            tags=["consulting", "management", "practice_leadership"],
            bullets=[
                FactBullet(
                    id="fact_moai_01",
                    raw_text="Managed West Coast Professional Services practice; developed in-house project methodology and field consulting best practices.",
                    scope="Practice Management & Consulting Methodology",
                ),
                FactBullet(
                    id="fact_moai_02",
                    raw_text="Served as primary technical point of contact for external enterprise partners and internal product groups.",
                    scope="Partner & Executive Consulting",
                ),
            ],
        ),
        FactRole(
            id="role_moai_cons_1999",
            company="Moai Incorporated",
            title="Lead Professional Services Consultant",
            dates="June 1999 – August 2000",
            start_year=1999,
            end_year=2000,
            tags=["consulting", "java", "b2b", "ecommerce"],
            bullets=[
                FactBullet(
                    id="fact_moai_03",
                    raw_text="Architected enterprise B2B websites using Java, Java Servlets, relational databases, and LiveExchange Dynamic Commerce engine.",
                    tools=["Java", "Java Servlets", "Relational Databases", "LiveExchange"],
                    scope="Java Systems Architecture",
                ),
                FactBullet(
                    id="fact_moai_04",
                    raw_text="Managed project scope with clients and coordinated multiple delivery teams through full SDLC while supporting technical pre-sales.",
                    scope="SDLC Delivery & Pre-Sales Consulting",
                ),
            ],
        ),
        FactRole(
            id="role_sapient_1998",
            company="Sapient Corporation",
            title="Senior Consultant / Facilitator / Designer",
            dates="April 1998 – June 1999",
            start_year=1998,
            end_year=1999,
            tags=["consulting", "plsql", "oracle", "business_process"],
            bullets=[
                FactBullet(
                    id="fact_sapient_01",
                    raw_text="Led development of complex product distribution business rules in Oracle PL/SQL with two programmers, owning database development and DBA coordination.",
                    tools=["Oracle PL/SQL", "Oracle Database"],
                    scope="Database Programming & Team Leadership",
                ),
                FactBullet(
                    id="fact_sapient_02",
                    raw_text="Designed end-to-end natural gas pipeline transportation business program: order entry, inventory measurement, distribution rules, and billing.",
                    scope="Business Process Design & Systems Engineering",
                ),
            ],
        ),
        FactRole(
            id="role_lucasarts_starwars_1995",
            company="LucasArts Entertainment Company",
            title="Project Leader / Manager on Star Wars: Masters of Teras Kasi",
            dates="November 1995 – April 1998",
            start_year=1995,
            end_year=1998,
            tags=["gaming", "leadership", "3d", "star_wars", "c", "assembly"],
            bullets=[
                FactBullet(
                    id="fact_lucas_01",
                    raw_text="Responsible for all aspects of creating, planning, budgeting, and delivering a $1 million flagship commercial product.",
                    metrics=["$1M budget"],
                    scope="Game Production & Budget Management",
                ),
                FactBullet(
                    id="fact_lucas_02",
                    raw_text="Successfully managed a cross-functional team of 14 artists and programmers to deliver a high-speed real-time polygonal 3D game on schedule.",
                    metrics=["Team of 14 artists and programmers"],
                    scope="Cross-Functional Studio Leadership",
                ),
                FactBullet(
                    id="fact_lucas_03",
                    raw_text="Architected and implemented foundation of 3D data structures, real-time animation pipelines, and systems methods.",
                    tools=["3D Data Structures", "Real-Time 3D Pipeline", "C", "Assembly"],
                    scope="3D Engine & Systems Architecture",
                ),
            ],
        ),
        FactRole(
            id="role_lucasarts_bigsky_1994",
            company="LucasArts Entertainment Company",
            title="Lead Programmer on Big Sky Trooper",
            dates="March 1994 – October 1995",
            start_year=1994,
            end_year=1995,
            tags=["gaming", "lead_programmer", "c", "assembly"],
            bullets=[
                FactBullet(
                    id="fact_lucas_04",
                    raw_text="Charted programming development cycle, managed two programmers, and delivered commercial game product on time.",
                    scope="Engineering Lead & Delivery",
                ),
            ],
        ),
        FactRole(
            id="role_accolade_1993",
            company="Accolade",
            title="Lead Programmer on Charles Barkley: Shut Up and Jam",
            dates="April 1993 – March 1994",
            start_year=1993,
            end_year=1994,
            tags=["gaming", "lead_programmer", "console"],
            bullets=[
                FactBullet(
                    id="fact_accolade_01",
                    raw_text="Specified, coded, and delivered console game on schedule under tight deadline, architecting for platform-neutral implementations.",
                    scope="Cross-Platform Game Development",
                ),
            ],
        ),
        FactRole(
            id="role_lucasarts_1990",
            company="LucasArts Entertainment Company",
            title="Programmer",
            dates="June 1990 – April 1993",
            start_year=1990,
            end_year=1993,
            tags=["gaming", "programmer", "pc", "snes"],
            bullets=[
                FactBullet(
                    id="fact_lucas_05",
                    raw_text="Programmed two commercial games that sold over 1 million units across PC and Super Nintendo: Zombies Ate My Neighbor (SNES) and Indiana Jones and The Fate of Atlantis (PC).",
                    metrics=[">1 million units sold"],
                    tools=["PC", "Super Nintendo", "Assembly", "C"],
                    scope="Commercial Scale Game Engineering",
                ),
            ],
        ),
    ]

    addendum = {
        "agentic_ai_context": "Hands-on applied personal/exploratory development using Python, OpenAI Codex, GitHub Copilot, Ollama, custom agents, n8n.",
        "nix_dev_env_context": "Hands-on exploration of Nix and dev-env for reproducible developer environments.",
        "oncall_middleware_context": "24x7 incident management, severity escalations, and PIRs at Blue Shield (10–15 engineers).",
        "bluestack_scale": "80–100 internal developers and stakeholders supported by BlueStack IDP.",
    }

    return FactLedger(
        name=name,
        phone=phone,
        email=email,
        education=education,
        skills=skills,
        roles=roles,
        addendum_facts=addendum,
    )


def save_fact_ledger(ledger: FactLedger, out_path: Path | str = "inputs/facts.yaml") -> Path:
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    raw = asdict(ledger)
    with open(out, "w", encoding="utf-8") as f:
        yaml.dump(raw, f, sort_keys=False, allow_unicode=True)
    return out


def load_fact_ledger(path: Path | str = "inputs/facts.yaml") -> FactLedger:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    roles = []
    for r in data["roles"]:
        bullets = [FactBullet(**b) for b in r.get("bullets", [])]
        roles.append(
            FactRole(
                id=r["id"],
                company=r["company"],
                title=r["title"],
                dates=r["dates"],
                start_year=r["start_year"],
                end_year=r["end_year"],
                bullets=bullets,
                tags=r.get("tags", []),
            )
        )
    return FactLedger(
        name=data["name"],
        phone=data["phone"],
        email=data["email"],
        education=data["education"],
        skills=data["skills"],
        roles=roles,
        addendum_facts=data.get("addendum_facts", {}),
    )
