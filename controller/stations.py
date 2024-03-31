import os

# import asyncio
from typing import Any
import aiohttp
from config.redisdb import db
from dotenv import load_dotenv

load_dotenv()

cache = db.cache()
stations_url = os.getenv("stations")


async def get_stations() -> Any:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(stations_url) as response:
                result = await response.json()
                cache.set("stations", result, 86400)
                return cache.get("stations")
    except Exception as error:
        return error

# asyncio.run(get_stations())
