import asyncio
import requests


def fetch(url):
    try:
        return requests.get(url)
    except Exception:
        pass


async def kick_off_job(url):
    asyncio.create_task(fetch(url))


async def fetch_all(urls):
    return await asyncio.gather(*(fetch(u) for u in urls))
