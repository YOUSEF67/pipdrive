import logging

mock_deals = []

def create_deal(title: str, url: str, gist_id: str):
    deal = {
        "gist_id": gist_id,
        "title": title,
        "url": url
    }
    mock_deals.append(deal)
    logging.info(f"[MOCK] Created deal for gist {gist_id}")
    return deal

def get_deals():
    return mock_deals
