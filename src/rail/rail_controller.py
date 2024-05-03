import os
from typing import Any
import json
import requests
from dotenv import load_dotenv

load_dotenv()

pnr_url = os.getenv("pnr")
stations_url = os.getenv("stations")
trains_url = os.getenv("trains")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}

def get_pnr_status(pnr: int) -> Any:
    try:
        session = requests.Session()
        response = session.get(f"{pnr_url}/{pnr}", headers=headers)
        return json.loads(json.dumps(response.json()))
    #     content = json.loads(json.dumps(response.json()))

    # return [
    #     {
    #         "Pnr": content["Pnr"],
    #         "TrainNo": content["TrainNo"],
    #         "TrainName": content["TrainName"],
    #         "BookingDate": content["BookingDate"],
    #         "DateOfJourney": content["Doj"],
    #         "DestinationDateOfJourney": content["DestinationDoj"],
    #         "From": content["From"],
    #         "To": content["To"],
    #         "BoardingStationName": content["BoardingStationName"],
    #         "ReservationUptoName": content["ReservationUptoName"],
    #         "Class": content["Class"],
    #         "ChartPrepared": content["ChartPrepared"],
    #         "TicketStatus": content["PassengerStatus"][0]["ConfirmTktStatus"],
    #         "Berth": content["PassengerStatus"][0]["Berth"],
    #         "BookingStatus": content["PassengerStatus"][0]["BookingStatus"],
    #         "CurrentStatus": content["PassengerStatus"][0]["CurrentStatus"],
    #         "BookingBerthNo": content["PassengerStatus"][0]["BookingBerthNo"],
    #         "CurrentBerthNo": content["PassengerStatus"][0]["CurrentBerthNo"],
    #         "DepartureTime": content["DepartureTime"],
    #         "ArrivalTime": content["ArrivalTime"],
    #         "ExpectedPlatformNo": content["ExpectedPlatformNo"],
    #         "BookingFare": content["BookingFare"],
    #         "TicketFare": content["TicketFare"],
    #         "Rating": content["Rating"],
    #         "FoodRating": content["FoodRating"],
    #         "PunctualityRating": content["PunctualityRating"],
    #         "CleanlinessRating": content["CleanlinessRating"],
    #         "Duration": content["Duration"],
    #         "HasPantry": content["HasPantry"],
    #     }
    # ]

    except Exception as error:
        return error


def get_stations() -> Any:
    try:
        session = requests.Session()
        response = session.get(f"{stations_url}", headers=headers)
        return response.json()
    except Exception as error:
        return error


def get_trains() -> Any:
    try:
        session = requests.Session()
        response = session.get(f"{trains_url}", headers=headers)
        return response.json()
    except Exception as error:
        return error
