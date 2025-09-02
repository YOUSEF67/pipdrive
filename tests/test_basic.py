from app.github_service import fetch_gists

def test_fetch_gists_returns_list():
    gists = fetch_gists("octocat")
    assert isinstance(gists, list)
