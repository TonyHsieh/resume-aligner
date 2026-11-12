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


def test_match_recruiter_intro_prevents_same_company_generic_title_mismatch():
    job = Job(
        id="job-1b177f62",
        source="https://jobs.apple.com/en-us/details/200692086-3956/senior-enterprise-technical-support-engineer?team=CUST",
        company="Apple",
        title="Senior Enterprise Technical Support Engineer",
    )
    intros = [
        {
            "num": 6,
            "header": "Apple – Senior Creative Gameplay Engineer, Apple Arcade",
            "url": "https://jobs.apple.com/en-us/details/200688914-0836/senior-creative-gameplay-engineer-apple-arcade?team=SFTWR",
            "canonical_url": "https://jobs.apple.com/en-us/details/200688914-0836/senior-creative-gameplay-engineer-apple-arcade?team=SFTWR",
            "note": "Hi [Name], I noticed your team is hiring a Senior Creative Gameplay Engineer for Apple Arcade.",
            "query": 'site:linkedin.com/in "Apple" ("Apple Arcade" OR "Games")',
        }
    ]
    note, query = match_recruiter_intro(job, intros)
    assert "Apple Arcade" not in note
    assert "Apple Arcade" not in query
    assert "Senior Enterprise Technical Support Engineer" in note
    assert "Apple" in query


def test_match_recruiter_intro_prevents_shared_generic_company_word_mismatch():
    job = Job(
        id="job-8d50e706",
        source="https://careers.stanfordhealthcare.org/us/en/job/R-2656947/Product-Engineer-AI-ML",
        company="Stanford Health Care",
        title="Product Engineer - AI/ML",
    )
    intros = [
        {
            "num": 44,
            "header": "Assort Health – Senior Software Engineer - Product",
            "url": "https://jobs.ashbyhq.com/assorthealth/123",
            "canonical_url": "https://jobs.ashbyhq.com/assorthealth/123",
            "note": "Hi [Name], I came across the Senior Product Engineer opening at Assort Health.",
            "query": 'site:linkedin.com/in "Assort Health" ("Recruiter")',
        }
    ]
    note, query = match_recruiter_intro(job, intros)
    assert "Assort Health" not in note
    assert "Stanford Health Care" in note
    assert "Stanford Health Care" in query


def test_match_recruiter_intro_matches_base_url_ignoring_query_params():
    job = Job(
        id="job-113f6c06",
        source="https://www.google.com/about/careers/applications/jobs/results/93344946123088582-senior-product-manager-search-growth?location=San+Francisco",
        company="Google",
        title="Senior Product Manager, Search Growth",
    )
    intros = [
        {
            "num": 125,
            "header": "Google – Senior Product Manager, Search Growth",
            "url": "https://www.google.com/about/careers/applications/jobs/results/93344946123088582-senior-product-manager-search-growth",
            "canonical_url": "https://www.google.com/about/careers/applications/jobs/results/93344946123088582-senior-product-manager-search-growth",
            "note": "Hi [Name], I saw Google's Senior Product Manager, Search Growth opening.",
            "query": 'site:linkedin.com/in "Google" ("Search Growth")',
        }
    ]
    note, query = match_recruiter_intro(job, intros)
    assert "Search Growth" in note
    assert "Search Growth" in query
