#!/usr/bin/env zsh
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app -b 0.0.0.0:8000 --timeout 120 --access-logfile - --error-logfile -
