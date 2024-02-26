#!/usr/bin/env python3

# Libraries
import pathlib

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.lib.load_horses import load_horses

from .core.config import settings

# Create App
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
)

# Setting base dir for templates
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(
    directory=[
        BASE_DIR / "templates",
    ]
)

# Mounting static directory for static files
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


# Defining routes
@app.get("/", response_class=HTMLResponse)
async def get_base(request: Request):
    horses = load_horses("assets/horses/mares")

    return templates.TemplateResponse(
        "home.html", {"request": request, "horses": horses}
    )
