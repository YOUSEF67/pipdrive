import logging
from apscheduler.schedulers.background import BackgroundScheduler
from .storage import add_gists, get_all_users
from .github_service import fetch_gists
from .pipedrive_service import create_deal

logging.basicConfig(level=logging.INFO)

def run_scan():
    logging.info("Running scheduled scan...")
    users = get_all_users()
    for username in users:
        gists = fetch_gists(username)
        new_gists = add_gists(username, gists)
        for gist in new_gists:
            create_deal(gist["description"], gist["url"], gist["id"])
    logging.info("Scheduled scan completed.")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_scan, "interval", hours=3)  # every 3h
    scheduler.start()
    logging.info("Scheduler started: scanning every 3 hours.")