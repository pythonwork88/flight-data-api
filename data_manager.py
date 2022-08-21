from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f01d2b6be7f859312f7fb7e0f18dd953/flightDeals/prices"
SHEETY_USER = "https://api.sheety.co/f01d2b6be7f859312f7fb7e0f18dd953/flightDeals/users"
response = requests.get(url=SHEETY_USER)
dat = response.json()
print(dat)

class DATA_MANAGER:

    def get_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()["prices"]

        return data

    def change_loc(self, id, new):

        new_loc = f"{SHEETY_PRICES_ENDPOINT}/{id}"
        new_par = {
            "price": {
                "iataCode": new,
            }
        }
        new_response = requests.put(url=new_loc, json=new_par)

    def make_em(self):


        print("Welcome to Vejay's Flight CLub.")
        print("We find the best flight deals and email you.")
        user_first_name = input("What is your first name ? ")
        user_last_name = input("What is your last name ? ")
        emailone = input("What is your email? ")
        emailtwo = input("Type you email again. ")




