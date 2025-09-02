import requests
import logging

def fetch_gists(username: str):
    """Fetch public gists of a GitHub user."""
    url = f"https://api.github.com/users/{username}/gists"
    try:
        response = requests.get(url, timeout=10)
    except Exception as e:
        logging.error(f"Network error while fetching gists: {e}")
        return []

    if response.status_code != 200:
        logging.error(f"GitHub API error: {response.status_code} {response.text}")
        return []

    gists = response.json()
    return [
        {
            "id": gist["id"],
            "url": gist["html_url"],
            "description": gist["description"] or "No description",
            "created_at": gist["created_at"]
        }
        for gist in gists
    ]
