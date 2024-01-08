import ipinfo
# import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

access_token = os.getenv("access_token")
handler = ipinfo.getHandlerAsync(access_token)


async def ip_info(ip_address):
     details = await handler.getDetails(ip_address)
     return details

# loop = asyncio.get_event_loop()
# loop.run_until_complete(do_req())
