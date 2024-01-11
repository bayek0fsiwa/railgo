from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from services.pnr import make_request
from services.stations import get_stations_list
from services.trains import get_train_list
# from redis import Redis
# import redis
# import json
# import os
from dotenv import load_dotenv

load_dotenv()
# redis_url = os.getenv("redis_url")
# redis_port = os.getenv("redis_port")
# Configs
limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
# r = Redis.from_url(url=redis_url, port=redis_port, db=0)

# r = redis.Redis(host='localhost', port=6379, db=0)


# Just displays clients ip
@app.get("/")
@limiter.limit("2/minute")
async def root(request: Request):
    # client_host = json.loads(request.client.host)
    # ip = r.set("ip", json.dumps(client_host))
    return {"details": "Hello There! 😘"}


# 2306899906
# Get PNR details
@app.get("/v1/pnr-number/{pnr}")
@limiter.limit("2/minute")
async def pnr_status(request: Request, pnr):
    data = make_request(pnr)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found try after sometime")
    return data


# Get all the list of stations
@app.get("/v1/stations")
@limiter.limit("2/minute")
async def station(request: Request):
    data = get_stations_list()
    # cache = r.get("stations")
    # if cache:
    #     print(cache)
    #     return json.loads(cache)
    # else:
    #     r.set("stations", json.dumps(data), ex=864000)
    return data


# Get all the list of trains
@app.get("/v1/trains")
@limiter.limit("2/minute")
async def train(request: Request):
    data = get_train_list()
    # cache = r.get("trains")
    # if cache:
    #     print(cache)
    #     return json.loads(cache)
    # else:
    #     r.set("trains", json.dumps(data), ex=864000)
    return data


# http://localhost:8001/redis-stack/browser
