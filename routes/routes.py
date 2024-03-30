from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

router = APIRouter()


router.get("/api/v1/pnr-status/{pnr}", response_class=ORJSONResponse)


def get_pnr(pnr: int):
    pass


@router.get("/api/v1/trains", response_class=ORJSONResponse)
def get_trains_list(request: Request):
    pass


@router.get("/api/v1/stations", response_class=ORJSONResponse)
def get_stations_list(request: Request):
    pass
