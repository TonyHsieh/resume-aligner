from resume_factory.sheets import match_recruiter_intro
from resume_factory.tracker import Job


def test_match_recruiter_intro_canonical_url():
    job = Job(
        id="job-1",
        source="https://jobs.example.com/posting/123?utm_source=linkedin",
        company="Acme Corp",
        title="Staff Software Engineer",
    )
    intros = [
        {
            "num": 1,
            "header": "Acme Corp – Staff Software Engineer",
            "url": "https://jobs.example.com/posting/123",
            "canonical_url": "https://jobs.example.com/posting/123",
            "note": "Hi [Name], I noticed Acme Corp is hiring. I have 10+ years experience.",
            "query": 'site:linkedin.com/in ("Acme Corp") ("Technical Recruiter")',
        }
    ]
    note, query = match_recruiter_intro(job, intros)
    assert "Acme Corp" in note
    assert "Acme Corp" in query


def test_match_recruiter_intro_prevents_cross_company_contamination():
    # Job is Snout, but intros list only has Xbox Media with same generic title
    job = Job(
        id="job-2",
        source="https://jobs.gem.com/snout/abc123xyz",
        company="Snout",
        title="Principal Software Engineer",
    )
    intros = [
        {
            "num": 1,
            "header": "Activision Blizzard / Microsoft Gaming – Principal Software Engineer, Xbox Media",
            "url": "https://careers.activisionblizzard.com/job/123",
            "canonical_url": "https://careers.activisionblizzard.com/job/123",
            "note": "Hi [Name], I noticed you're hiring a Principal Software Engineer for Xbox Media.",
            "query": 'site:linkedin.com/in ("Xbox" OR "Microsoft") ("Recruiter")',
        }
    ]
    note, query = match_recruiter_intro(job, intros)
    # MUST NOT contain Xbox or Microsoft! Must be tailored to Snout!
    assert "Xbox" not in note
    assert "Microsoft" not in note
    assert "Snout" in note
    assert "Snout" in query


def test_match_recruiter_intro_dynamic_fallback():
    job = Job(
        id="job-3",
        source="https://randomstartup.io/jobs/456",
        company="BioHealth AI",
        title="Solutions Architect",
    )
    intros = []
    note, query = match_recruiter_intro(job, intros)
    assert "BioHealth AI" in note
    assert "Solutions Architect" in note
    assert "BioHealth AI" in query
