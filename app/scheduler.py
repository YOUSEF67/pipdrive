from apscheduler.schedulers.background import BackgroundScheduler
import logging
from .github_service import fetch_gists
from .pipedrive_service import create_deal
from .storage import add_gists, get_all_users, get_seen_gists

logging.basicConfig(level=logging.INFO)

def run_scan():
    logging.info("Running scan job...")
    results = {}

    users = get_all_users()
    for username in users:
        gists = fetch_gists(username)
        new_gists = add_gists(username, gists)

        for gist in new_gists:
            create_deal(gist["description"], gist["url"], gist["id"])

        results[username] = {
            "new_gists": new_gists,
            "already_seen": get_seen_gists(username)
        }

    logging.info("Scan completed.")
    return results

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scan, "interval", hours=3)  # every 3h
    scheduler.start()
    logging.info("Scheduler started: scanning every 3 hours.")
