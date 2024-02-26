# Dependencies
from pathlib import Path

import bleach
import frontmatter
import markdown

# from pydantic import BaseModel
#
# Possibly do data validation before serving
#
# class Loadhorses(Basemodel):
#    id: int
#    title: str
#    description: str = None
#    date:
#    content: str = None
#
#    return BaseModel

# allowed parameters for bleach
allowed_tags = [
    "div",
    "img",
    "h1",
    "h2",
    "h3",
    "p",
    "a",
    "ul",
    "ol",
    "li",
    "strong",
    "em",
    "br",
]
allowed_attributes = {
    "div": ["class"],
    "img": ["src", "alt", "title", "width", "height"],
    "a": ["href", "title", "rel"],
}


def load_horses(directory: str) -> list:
    # Variable for directory path, empty list to load horses
    horses: list = []
    path = Path(directory)

    # Concatenate the files of 'directory' into a list of files
    files = sorted(
        path.glob("*.md"),
        key=lambda x: x.name,
        reverse=False,
    )

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as content:
                horse = frontmatter.load(content)
                #                print(f"Geladene Daten: {horse.metadata}")
                html = bleach.clean(
                    (markdown.markdown(horse.content)),
                    tags=allowed_tags,
                    attributes=allowed_attributes,
                )
                rendered_horse_setcard = {
                    "kategorie": horse.get("kategorie", None),
                    "vater": horse.get("vater", None),
                    "muttervater": horse.get("muttervater", "Nicht bekannt"),
                    "name": horse.get("name", "Nicht vergeben"),
                    "zuchtgebiet": horse.get("zuchtgebiet", "Nicht bekannt"),
                    "geburtsjahr": horse.get("geburtsjahr", "Nicht bekannt"),
                    "farbe": horse.get("farbe", "Nicht bekannt"),
                    "zuechter": horse.get("zuechter", "Nicht bekannt"),
                    "besitzer": horse.get("besitzer", "Nicht bekannt"),
                    "eigenleistung": horse.get("eigenleistung", "Nicht bekannt"),
                    "zucht": horse.get("zucht", "Kein Zuchtrekord"),
                    "horsetelex": horse.get("horsetelex", "Kein Eintrag"),
                    "profilbild": horse.get("profilbild", None),
                    "medien": horse.get("medien", None),
                    "zusatz": horse.get("zusatz", None),
                    "body": html,
                }
                horses.append(rendered_horse_setcard)

        except Exception as e:
            print(f"\033[1mFehler beim Laden von {file}: {e}")

    return horses
