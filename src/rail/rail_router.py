from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import JSONResponse
from .rail_router import get_pnr, get_stations_list, get_trains_list


router = APIRouter()


@router.get("/api/v1/pnr-status/{pnr}", response_class=JSONResponse)
def get_pnr(pnr: int):
    if not pnr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    data = get_pnr(pnr)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"message": "OK" ,"data": data}


@router.get("/api/v1/trains", response_class=JSONResponse)
def get_trains_list(request: Request):
    data = get_stations_list()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["trains"]), "data": data}


@router.get("/api/v1/stations", response_class=JSONResponse)
def get_stations_list(request: Request):
    data = get_trains_list()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["stations"]), "data": data}
