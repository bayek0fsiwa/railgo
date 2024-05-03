from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from . import rail_controller


router = APIRouter()


@router.get("/api/v1/trains", response_class=JSONResponse)
def get_trains_list():
    data = rail_controller.get_trains()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["trains"]), "data": data}


@router.get("/api/v1/stations", response_class=JSONResponse)
def get_stations_list():
    data = rail_controller.get_stations()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"count": len(data["stations"]), "data": data}


@router.get("/api/v1/pnr-status/{pnr}", response_class=JSONResponse)
def get_pnr(pnr: int):
    if not pnr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    data = rail_controller.get_pnr_status(pnr)
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"message": "OK", "data": data}
