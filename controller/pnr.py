import os
from typing import Any

# import asyncio
# import json
# import requests
import aiohttp
from dotenv import load_dotenv

load_dotenv()

pnr_url = os.getenv("pnr")


async def get_pnr_status(pnr_number: int) -> Any:
    # session = requests.Session()
    # response = await asyncio.to_thread(session.get(f"{pnr_url}/{pnr_number}"))
    # return response.json()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{pnr_url}/{pnr_number}") as response:
            result = await response.json()
            return result


# asyncio.run(get_pnr_status())
