from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from app.database import Base, engine
from app.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GoTogetherRides AI Ride Matching Engine",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")

app.include_router(router)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        request=request
    )