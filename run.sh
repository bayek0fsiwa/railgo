#!/bin/sh
# RUN chmod +x script.sh
uvicorn src.main:app --reload --port=8080
# python3 server.py