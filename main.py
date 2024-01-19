#!/usr/bin/env python3

# Libraries
import os
import pathlib
from datetime import datetime

import frontmatter
import markdown
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from lib.tools import load_posts

# Create App
app = FastAPI()

# Setting base dir for templates
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(
    directory=[
        BASE_DIR / "templates",
    ]
)

# Mounting static directory for static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Defining routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    directory = "posts"
    posts = load_posts(directory)
    today = datetime.now().strftime("%Y-%m-%d")

    response = templates.TemplateResponse(
        "home.html", {"request": request, "posts": posts, "today": today}
    )

    return response


@app.get("/archive", response_class=HTMLResponse)
async def archive(request: Request):
    posts = "posts"
    html = ""

    # Iterate over whole posts directory
    for post in os.listdir(posts):
        if post.endswith(".md"):
            with open(os.path.join(posts, post), "r", encoding="utf-8") as inputfile:
                text = inputfile.read()
                html += markdown.markdown(text) + "<hr>"

    return html


def main():
    pass


if __name__ == "__main__":
    main()
