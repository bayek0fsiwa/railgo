from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .rail import rail_router

app = FastAPI()

app.include_router(router=rail_router)

@app.get("/", response_class=JSONResponse)
def root(request: Request):
    return {"message": "Hello There! 😘"}

