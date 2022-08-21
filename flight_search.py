import requests
API_KEY = "here give api key"
SEARCH_API = "http://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{SEARCH_API}/locations/query"
        headers = {"apikey": API_KEY}
        query = {"term": city_name, "location_types": "airport"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code


