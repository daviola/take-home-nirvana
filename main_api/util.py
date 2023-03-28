import asyncio
from aiohttp import ClientSession


async def fetch_url_async(session: ClientSession, url: str):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.json()


async def fetch_async_from_multiple_urls(session: ClientSession, urls: list):
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(fetch_url_async(session, url)))
    responses = await asyncio.gather(*tasks)
    return responses
