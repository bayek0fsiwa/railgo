from fastapi import FastAPI, Request
from routes.routes import router

app = FastAPI()

app.include_router(router=router)


@app.get("/")
def root(request: Request):
    return {"request": request ,"message": "Hello There! 😘"}

# http://localhost:8001/redis-stack/browser
