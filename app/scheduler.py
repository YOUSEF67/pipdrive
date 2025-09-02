import logging
from apscheduler.schedulers.background import BackgroundScheduler
from .storage import add_gists, get_all_users
from .github_service import fetch_gists
from .pipedrive_service import create_deal

def scan_all():
    logging.info("Scheduled scan started...")
    for user in get_all_users():
        gists = fetch_gists(user)
        new_gists = add_gists(user, gists)
        for gist in new_gists:
            create_deal(gist["description"], gist["url"], gist["id"])
        logging.info(f"User {user}: {len(new_gists)} new gists")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scan_all, "interval", seconds=600)  # every 10 min
    scheduler.start()
    logging.info("Scheduler started (scans every 600s)")
