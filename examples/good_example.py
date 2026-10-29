import asyncio
import logging

import requests

logger = logging.getLogger(__name__)


def fetch(url):
    try:
        return requests.get(url, timeout=5)
    except requests.RequestException:
        logger.exception("fetch failed for %s", url)
        raise


async def fetch_all(urls):
    return await asyncio.gather(*(fetch(u) for u in urls), return_exceptions=True)
