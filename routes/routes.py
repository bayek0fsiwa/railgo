import asyncio
from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from controller import pnr, trains, stations

router = APIRouter()


@router.get("/api/v1/pnr-status/{pnr}", response_class=JSONResponse)
def get_pnr(pnr_number: int):
    if not pnr_number:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    data = asyncio.run(pnr.get_pnr_status(pnr_number=pnr_number))
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"data": data}


@router.get("/api/v1/trains", response_class=JSONResponse)
def get_trains_list(request: Request):
    data = asyncio.run(trains.get_trains())
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["trains"]), "data": data}


@router.get("/api/v1/stations", response_class=JSONResponse)
def get_stations_list(request: Request):
    data = asyncio.run(stations.get_stations())
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["stations"]), "data": data}
