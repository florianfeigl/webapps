#!/usr/bin/env python3

# Libraries
import pathlib
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .core.config import settings
from .lib.utils import load_posts

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
app.mount("/static", StaticFiles(directory="static"), name="static")

# Global variable
today = datetime.now().strftime("%Y-%m-%d")


# Defining routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Loading posts from directory 'content/posts'
    posts = load_posts("content/posts")

    response = templates.TemplateResponse(
        "home.html", {"request": request, "posts": posts, "today": today}
    )

    return response


# @app.get("/archive", response_class=HTMLResponse)
# async def archive(request: Request):
#    posts = "posts"
#    html = ""
#
#    # Iterate over whole posts directory
#    for post in os.listdir(posts):
#        if post.endswith(".md"):
#            with open(os.path.join(posts, post), "r", encoding="utf-8") as inputfile:
#                text = inputfile.read()
#                html += markdown.markdown(text) + "<hr>"
#
#    return html


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
