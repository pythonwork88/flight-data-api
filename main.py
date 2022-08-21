from notification_manager import NotificationManager as nt
from data_manager import DATA_MANAGER
from flight_search import FlightSearch
from flight_data import FLIGHT_DATA as FL
sheet_data = DATA_MANAGER().get_data()
print(sheet_data)


for sheet in sheet_data["prices"]:
    if sheet["iataCode"] == "":

        city = (sheet["city"])

        location = FlightSearch().get_destination_code(city)

        DATA_MANAGER().change_loc(sheet["id"], location)

    sheet_data = DATA_MANAGER().get_data()
else:
    for sheet in sheet_data:

        FL().search_flight(sheet["iataCode"])
    data = FL().flight_list

new_list = []
for sheet in sheet_data:
    new_fli = FL().search_flight(sheet["iataCode"])



    if not new_fli:
        pass
    else:
        pricetogo = [new_fli["mon"]]
        cityfrom = [new_fli["from"]]
        citygo = [new_fli["to"]]
        datefr = [new_fli["dateFrom"]]
        datetog = [new_fli["dateTo"]]
        new_txt = (f"Low price alert! only £{pricetogo[0]} to fly from {cityfrom[0]} to {citygo[0]}, from {datefr[0][0]} to {datetog[0][0]}.")


    if type(sheet) == dict:
        if sheet["lowestPrice"] >= new_fli["mon"]:
            new_list.append(new_fli)
            print(type(sheet["lowestPrice"]))
            print(type(new_fli["mon"]))
            print(type(new_fli))
            nt().send(new_txt)





print(new_list)

