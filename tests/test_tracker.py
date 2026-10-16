from resume_factory.tracker import (
    Tracker,
    canonical_source,
    job_id,
    parse_job_list,
    sha,
)


def test_parse_job_list_urls_labels_paths_and_comments():
    text = """
    # my targets
    Apple - ASE Compute: https://jobs.apple.com/en-us/details/123?utm_source=x
    https://boards.greenhouse.io/acme/jobs/9.
    ./jds/stripe.pdf
    just some prose with no link
    """
    assert parse_job_list(text) == [
        ("https://jobs.apple.com/en-us/details/123?utm_source=x", "Apple - ASE Compute"),
        ("https://boards.greenhouse.io/acme/jobs/9", None),
        ("./jds/stripe.pdf", None),
    ]


def test_canonicalisation_makes_equivalent_links_share_an_id():
    a = "https://Jobs.Apple.com/en-us/details/123/?utm_source=x&b=2&a=1"
    b = "https://jobs.apple.com/en-us/details/123?a=1&b=2"
    assert canonical_source(a) == canonical_source(b)
    assert job_id(a) == job_id(b)
    gd1 = "https://docs.google.com/document/d/ABC_123/edit?tab=t.0"
    gd2 = "https://docs.google.com/document/d/ABC_123/export?format=txt&tab=t.0"
    assert job_id(gd1) == job_id(gd2)
    assert job_id(gd1) != job_id("https://docs.google.com/document/d/ABC_123/edit?tab=t.1")


def test_add_is_idempotent_and_persists(tmp_path):
    path = tmp_path / "tracker.json"
    t = Tracker(path)
    new, known = t.add_list("A: https://x.com/1\nhttps://x.com/2")
    assert (len(new), len(known)) == (2, 0)
    t.save()

    t2 = Tracker(path)
    new, known = t2.add_list("https://x.com/1\nhttps://x.com/3")
    assert [j.source for j in new] == ["https://x.com/3"]
    assert [j.source for j in known] == ["https://x.com/1"]
    assert t2.jobs[job_id("https://x.com/1")].label == "A"  # kept from first add


def test_mark_aligned_and_pending(tmp_path):
    t = Tracker(tmp_path / "t.json")
    (a, b), _ = t.add_list("https://x.com/a\nhttps://x.com/b")
    t.mark_aligned(a.id, jd_hash="jd1", master_hash="m1", outputs={"resume": "out/a.docx"})
    assert [j.id for j in t.pending()] == [b.id]
    assert t.counts()["aligned"] == 1


def test_stale_when_jd_or_master_changes(tmp_path):
    t = Tracker(tmp_path / "t.json")
    (a,), _ = t.add_list("https://x.com/a")
    t.mark_aligned(a.id, jd_hash="jd1", master_hash="m1", outputs={})
    assert t.pending({a.id: "jd1"}, "m1") == []
    assert t.stale_reason(a, "jd2", "m1") == "job description changed"
    assert t.stale_reason(a, "jd1", "m2") == "master resume facts changed"
    assert [j.id for j in t.pending({a.id: "jd2"}, "m1")] == [a.id]


def test_blocked_jobs_are_not_pending_and_status_is_validated(tmp_path):
    t = Tracker(tmp_path / "t.json")
    (a,), _ = t.add_list("https://x.com/a")
    t.set_status(a.id, "blocked", note="HTTP 401: not shared")
    assert t.pending() == []
    try:
        t.set_status(a.id, "done")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid status accepted")


def test_index_markdown(tmp_path):
    t = Tracker(tmp_path / "t.json")
    (a, b, c), _ = t.add_list("Acme SRE: https://x.com/a\nhttps://x.com/b\nhttps://x.com/c")
    t.mark_aligned(a.id, jd_hash="j", master_hash="m", outputs={"resume": "a.docx"}, open_questions=3)
    t.set_status(c.id, "blocked", note="401")
    index = t.render_index({a.id: "CHANGED"}, "m")
    assert "**1 of 3 aligned**" in index
    assert "stale (job description changed)" in index
    assert "⛔" in index and "401" in index
    path = t.write_index()
    assert path.name == "INDEX.md" and path.read_text(encoding="utf-8") == t.render_index()


def test_sha_is_stable():
    assert sha("abc") == sha("abc") != sha("abd")


def test_parse_job_list_handles_google_doc_bom_and_crlf():
    text = "\ufeffhttps://x.com/a\r\n\r\n\r\nhttp://x.com/b\r\n"
    assert parse_job_list(text) == [("https://x.com/a", None), ("http://x.com/b", None)]
