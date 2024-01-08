FROM python:3.11

WORKDIR /app

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade --no-cache -r /app/requirements.txt

EXPOSE 8080

COPY ./ /app/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

# docker compose exec <service-name> bash/python
# Build instruction
# docker build -t railgo .
# docker run -dp 127.0.0.1:8080:8080 railgo
# check running container
# docker ps
# To stop running container 
# docker stop <the-container-id>
# To remove the container
# docker rm <the-container-id>