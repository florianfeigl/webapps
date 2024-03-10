#!/usr/bin/env zsh

mkdir app static migrations
touch app/{__init__.py,main.py,models.py,schemas.py,database.py,crud.py}
touch requirements.txt
python -m venv .venv
