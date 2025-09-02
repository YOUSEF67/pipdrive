from flask import Blueprint, jsonify
import logging

from .github_service import fetch_gists
from .pipedrive_service import create_deal, get_deals
from .storage import add_gists, get_seen_gists, get_all_users

bp = Blueprint("main", __name__)
logging.basicConfig(level=logging.INFO)

@bp.route("/gists/<username>")
def get_user_gists(username):
    gists = fetch_gists(username)
    new_gists = add_gists(username, gists)

    for gist in new_gists:
        create_deal(gist["description"], gist["url"], gist["id"])

    return jsonify({
        "username": username,
        "new_gists": new_gists,
        "already_seen": get_seen_gists(username)
    })

@bp.route("/users")
def users():
    return jsonify({"users": get_all_users()})

@bp.route("/deals")
def deals():
    return jsonify({"deals": get_deals()})
@bp.route("/health")
def health():
    return {"status": "ok"}, 200
@bp.route("/scan", methods=["POST"])
def scan():
    users = get_all_users()
    scanned = {}

    for username in users:
        gists = fetch_gists(username)
        new_gists = add_gists(username, gists)

        for gist in new_gists:
            create_deal(gist["description"], gist["url"], gist["id"])

        scanned[username] = {
            "new_gists": new_gists,
            "already_seen": get_seen_gists(username)
        }

    return jsonify({
        "status": "scan completed",
        "results": scanned
    })
