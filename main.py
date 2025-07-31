import asyncio
from typing import List
from reviews_parcer import ReviewsParcer
from manager_db import DBManager
from utils import send_notification, URLS


async def open_parcer(url: str):
    parcer = ReviewsParcer(url.strip())
    new_data = await parcer.get_session()
    dbmanager = DBManager()
    count_reviews = dbmanager.save_reviews(new_data, url)
    await send_notification(url, count_reviews)

async def main(): 
    tasks = [open_parcer(url) for url in URLS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())