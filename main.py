from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routes.routes import router

app = FastAPI()

app.include_router(router=router)


@app.get("/", response_class=JSONResponse)
def root(request: Request):
    return {"message": "Hello There! 😘"}

# http://localhost:8001/redis-stack/browser
