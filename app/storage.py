user_gists = {}

def add_gists(username, gists):
    if username not in user_gists:
        user_gists[username] = set()

    new_gists = []
    for gist in gists:
        if gist["id"] not in user_gists[username]:
            user_gists[username].add(gist["id"])
            new_gists.append(gist)
    return new_gists

def get_seen_gists(username):
    return list(user_gists.get(username, []))

def get_all_users():
    return list(user_gists.keys())
