import os

# import asyncio
from typing import Any
import aiohttp
from dotenv import load_dotenv

load_dotenv()

trains_url = os.getenv("trains")


async def get_trains() -> Any:
    async with aiohttp.ClientSession() as session:
        async with session.get(trains_url) as response:
            result = await response.json()
            return result


# asyncio.run(get_trains())