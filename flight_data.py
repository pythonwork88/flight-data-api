import requests
from pprint import pprint
SEARCH_API = "http://tequila-api.kiwi.com/v2/search"
API_KEY = "cZZi3-SfCvcoC4ou--nJb7ecgHck1r7d"
from datetime import datetime as dt
from datetime import timedelta, date
date = dt.now().strftime("%d/%m/%Y")
next_date = dt.today()
next_date = (next_date + timedelta(days=300)).strftime("%d/%m/%Y")

min_retur = dt.today()
min_retur = (min_retur + timedelta(days=8)).strftime("%d/%m/%Y")

max_retur = dt.today()
max_retur = (max_retur + timedelta(days=28)).strftime("%d/%m/%Y")
print(date)
print(next_date)
print(min_retur)
print(max_retur)


class FLIGHT_DATA:

    def search_flight(self, loc):

        header = {
            "apikey": API_KEY
        }

        flight_param = {
            "fly_from": "LON",
            "fly_to": loc,
            "date_from": date,
            "date_to": next_date,
            "return_from": min_retur,
            "return_to": max_retur,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP",

        }

        response = requests.get(url=SEARCH_API, headers=header, params=flight_param)
        data = response.json()
        if not data:
            print("not found")
        else:
            for d in data["data"][:1]:
                city = d["cityTo"]
                money = d["price"]

                fromm = d["cityFrom"] + "-" + d["flyFrom"]
                too = d["cityTo"] + "-" + d["flyTo"]
                datef = d['local_departure'].split("T")[:1]


                dateto = d["route"][1]["utc_departure"].split("T")[:1]

                new_value = {"town":city, "mon":money , "from":fromm, "to":too, "dateFrom":datef, "dateTo":dateto}


                return new_value




