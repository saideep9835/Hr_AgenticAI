def test_tool_invocation():
    from tools import draft_job_description
    result = draft_job_description("Backend Engineer", {})
    assert "title" in result