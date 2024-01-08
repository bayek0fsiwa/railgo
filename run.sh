#!/bin/sh
# RUN chmod +x script.sh
uvicorn app:app --reload --port=8080 --proxy-headers --forwarded-allow-ips='*'