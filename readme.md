Get information about Indian railways like PNR status, Stations list, Trains list...


## To run locally run
- First install dependencies (use PowerShell if using Windows, CMD! should also work fine!)

> python -m pip install -U --no-cache pip -r requirements.txt
- Run the server.py file (no hot reload)
> python server.py
- To run with hot reload use below commands
> uvicorn src.main:app --reload --port=8080

## To run with Docker

- Run 👇
> docker compose up