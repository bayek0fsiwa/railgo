import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("URL")


def make_request(pnr):
    response = requests.request("GET", f"{url}{pnr}")
    content = json.loads(json.dumps(response.json()))

    return [
        {
            "Pnr": content["Pnr"],
            "TrainNo": content["TrainNo"],
            "TrainName": content["TrainName"],
            "BookingDate": content["BookingDate"],
            "DateOfJourney": content["Doj"],
            "DestinationDateOfJourney": content["DestinationDoj"],
            "From": content["From"],
            "To": content["To"],
            "BoardingStationName": content["BoardingStationName"],
            "ReservationUptoName": content["ReservationUptoName"],
            "Class": content["Class"],
            "ChartPrepared": content["ChartPrepared"],
            "TicketStatus": content["PassengerStatus"][0]["ConfirmTktStatus"],
            "Berth": content["PassengerStatus"][0]["Berth"],
            "BookingStatus": content["PassengerStatus"][0]["BookingStatus"],
            "CurrentStatus": content["PassengerStatus"][0]["CurrentStatus"],
            "BookingBerthNo": content["PassengerStatus"][0]["BookingBerthNo"],
            "CurrentBerthNo": content["PassengerStatus"][0]["CurrentBerthNo"],
            "DepartureTime": content["DepartureTime"],
            "ArrivalTime": content["ArrivalTime"],
            "ExpectedPlatformNo": content["ExpectedPlatformNo"],
            "BookingFare": content["BookingFare"],
            "TicketFare": content["TicketFare"],
            "Rating": content["Rating"],
            "FoodRating": content["FoodRating"],
            "PunctualityRating": content["PunctualityRating"],
            "CleanlinessRating": content["CleanlinessRating"],
            "Duration": content["Duration"],
            "HasPantry": content["HasPantry"],
        }
    ]
