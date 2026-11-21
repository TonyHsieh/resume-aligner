"""Regression tests for JD ingestion (Apple Jobs API and fallbacks)."""

from resume_factory import ingest


class _DummyResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json_data = json_data
        self.text = text

    def json(self):
        return self._json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


def test_fetch_apple_jobs_api_success(monkeypatch):
    calls = []

    def fake_get(url, headers=None, timeout=None):
        calls.append(url)
        return _DummyResponse(
            status_code=200,
            json_data={
                "res": {
                    "postingTitle": "Principal Platform Engineer, People Systems",
                    "reqId": "PIPE-200693795",
                    "jobSummary": "Build configuration-driven platforms at scale.",
                    "description": "<p>Lead architecture across distributed teams.</p>",
                    "minimumQualifications": "15+ years experience in distributed systems.",
                    "preferredQualifications": "Experience with Kubernetes and multi-tenant APIs.",
                }
            },
        )

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://jobs.apple.com/en-us/details/200693795-3956/principal-platform-engineer?team=SFTWR"
    )
    assert calls == ["https://jobs.apple.com/api/v1/jobDetails/200693795-3956"]
    assert title == "Principal Platform Engineer, People Systems"
    assert company == "Apple"
    assert is_closed is False
    assert "Req ID: PIPE-200693795" in text
    assert "Lead architecture across distributed teams." in text
    assert "<p>" not in text


def test_fetch_apple_jobs_api_falls_back_on_non_200(monkeypatch):
    calls = []

    def fake_get(url, headers=None, timeout=None):
        calls.append(url)
        if "/api/v1/jobDetails/" in url:
            return _DummyResponse(status_code=404)
        return _DummyResponse(
            status_code=200,
            text="<html><head><title>Fallback Title</title></head><body><p>Fallback JD body content for verification.</p></body></html>",
        )

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://jobs.apple.com/en-us/details/200693795-3956/principal-platform-engineer"
    )
    assert len(calls) == 2
    assert "Fallback JD body content for verification." in text
    assert is_closed is False


def test_fetch_apple_jobs_api_falls_back_when_payload_incomplete(monkeypatch):
    def fake_get(url, headers=None, timeout=None):
        if "/api/v1/jobDetails/" in url:
            return _DummyResponse(status_code=200, json_data={"res": {"postingTitle": ""}})
        return _DummyResponse(
            status_code=200,
            text="<html><head><title>Role</title></head><body><p>HTML fallback description</p></body></html>",
        )

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, _, _, _ = ingest.fetch_url_content(
        "https://jobs.apple.com/en-us/details/200694341-0836/some-role"
    )
    assert "HTML fallback description" in text


def test_fetch_oraclecloud_multisection_and_company(monkeypatch):
    def fake_get(url, headers=None, timeout=None):
        return _DummyResponse(
            status_code=200,
            json_data={
                "Title": "Data Products Program Lead (Contract to Hire)",
                "ExternalDescriptionStr": "<p>Overview of the data products program.</p>",
                "ExternalResponsibilitiesStr": "<p>Own product scope and consumer readiness.</p>",
                "ExternalQualificationsStr": "<p>15+ years experience in enterprise data architecture.</p>",
            },
        )

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://hcjy.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs/preview/13172/?location=San+Ramon"
    )
    assert title == "Data Products Program Lead (Contract to Hire)"
    assert company == "CooperCompanies"
    assert is_closed is False
    assert "DESCRIPTION:\nOverview of the data products program." in text
    assert "RESPONSIBILITIES:\nOwn product scope and consumer readiness." in text
    assert "QUALIFICATIONS:\n15+ years experience in enterprise data architecture." in text


def test_fetch_careers_oracle_com_routes_to_oraclecloud_api(monkeypatch):
    seen_urls = []

    def fake_get(url, headers=None, timeout=None):
        seen_urls.append(url)
        return _DummyResponse(
            status_code=200,
            json_data={
                "Title": "Platform Software Engineering Architect",
                "ExternalDescriptionStr": "<p>Design OCI platform services.</p>",
            },
        )

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://careers.oracle.com/en/sites/jobsearch/job/350911/?keyword=Platform"
    )
    assert seen_urls == [
        "https://eeho.fa.us2.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitionDetails/350911"
    ]
    assert title == "Platform Software Engineering Architect"
    assert company == "Oracle"
    assert is_closed is False
    assert "DESCRIPTION:\nDesign OCI platform services." in text


def test_fetch_mercor_next_data(monkeypatch):
    fake_html = """<!DOCTYPE html><html><head>
    <script id="__NEXT_DATA__" type="application/json">
    {"props": {"pageProps": {"jobs": [
        {
            "id": "76f19dab-be4a-4e1b-9971-3b3372666a05",
            "title": "Tech Lead, Applied AI - Evals",
            "location": "San Francisco",
            "workplaceType": "OnSite",
            "descriptionPlain": "Lead the Applied AI evaluations engineering team.\\nArchitect benchmarking platforms."
        }
    ]}}}
    </script></head><body></body></html>"""

    def fake_get(url, headers=None, timeout=None):
        return _DummyResponse(status_code=200, text=fake_html)

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://www.mercor.com/careers/76f19dab-be4a-4e1b-9971-3b3372666a05/"
    )
    assert title == "Tech Lead, Applied AI - Evals"
    assert company == "Mercor"
    assert is_closed is False
    assert "Location: San Francisco" in text
    assert "Workplace Type: OnSite" in text
    assert "Lead the Applied AI evaluations engineering team." in text


def test_fetch_metacareers_schema_org(monkeypatch):
    fake_html = """<!DOCTYPE html><html><head>
    <script>
    {
        "@context": "https://schema.org",
        "@type": "JobPosting",
        "title": "Engineering Manager - Strategic Infrastructure Capacity Planning",
        "jobLocation": [
            {"address": {"addressLocality": "Menlo Park", "addressRegion": "California"}}
        ],
        "baseSalary": {
            "value": {"minValue": 200000, "maxValue": 275000, "unitText": "YEAR"}
        },
        "description": "<p>Lead capacity engineering for global infrastructure.</p>",
        "responsibilities": "<p>Capacity planning for all of Meta software and services.</p>",
        "qualifications": "<p>15+ years experience in distributed systems and platform operations.</p>"
    }
    </script></head><body></body></html>"""

    def fake_get(url, headers=None, timeout=None):
        return _DummyResponse(status_code=200, text=fake_html)

    monkeypatch.setattr(ingest.requests, "get", fake_get)
    text, title, company, is_closed = ingest.fetch_url_content(
        "https://www.metacareers.com/profile/job_details/1585750969597972/"
    )
    assert title == "Engineering Manager - Strategic Infrastructure Capacity Planning"
    assert company == "Meta"
    assert is_closed is False
    assert "Menlo Park, California" in text
    assert "$200,000 - $275,000 / YEAR" in text
    assert "Lead capacity engineering for global infrastructure." in text
    assert "Capacity planning for all of Meta software and services." in text
    assert "15+ years experience in distributed systems and platform operations." in text



