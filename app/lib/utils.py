# Dependencies
import os

import bleach
import frontmatter
import markdown

# from pydantic import BaseModel
#
# Possibly do data validation before serving
#
# class LoadPosts(Basemodel):
#    id: int
#    title: str
#    description: str = None
#    date:
#    content: str = None
#
#    return BaseModel

# tags and attributes for bleach clean
allowed_tags = ['div', 'img', 'p', 'a', 'ul', 'ol', 'li', 'strong', 'em', 'br']
allowed_attributes = {
    'div': ['class'],
    'img': ['src', 'alt', 'title', 'width', 'height'],
    'a': ['href', 'title', 'rel'],
}

def load_posts(directory: str) -> list:
    # Variable for directory path, empty list to load posts
    posts: list = []

    # Concatenate the files of 'directory' into a list of files
    files = sorted(
        [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.endswith(".md")
        ],
        reverse=True,
    )

    for file in files:
        with open(file, "r", encoding="utf-8") as content:
            post = frontmatter.load(content)
            html = bleach.clean(
                (markdown.markdown(post.content)),
                tags=allowed_tags,
                attributes=allowed_attributes,
            )
            rendered_post = {
                "id": post.get("id", None),
                "title": post.get("title", "No Title"),
                "date": post.get("date", "No Date"),
                "body": html,
            }
            posts.append(rendered_post)

    return posts
