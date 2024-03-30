import os

# import asyncio
from typing import Any
import aiohttp
from dotenv import load_dotenv

load_dotenv()

stations_url = os.getenv("stations")


async def get_stations() -> Any:
    async with aiohttp.ClientSession() as session:
        async with session.get(stations_url) as response:
            result = await response.json()
            return result


# asyncio.run(get_stations())
