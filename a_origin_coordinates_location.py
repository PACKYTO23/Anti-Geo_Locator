import requests
from random import randint

# ORIGIN TO BE BASED ON IP ADDRESS, SELECTED LOCATION OR RANDOM
# IP GEO LOCATION API

IP_GEO_LOCATION_VISITOR_LOOKUP = "https://ip-geo-location.p.rapidapi.com/ip/check"
API_KEY = "e37837191amsh73b18fbdb45f29bp122ac8jsn1741eeaefc5a"  # SEND TO ENVIRONMENT VARIABLES.
API_HOST = "ip-geo-location.p.rapidapi.com"

MIN_LAT = -90
MAX_LAT = 90
MIN_LON = -180
MAX_LON = 180


def ip_address():
    """Returns set of geographical coordinates via the user's ip address (given the user's permission)."""
    origin_selection = "ip address"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST,
    }

    response = requests.get(url=IP_GEO_LOCATION_VISITOR_LOOKUP, headers=headers)
    latitude = float(response.json()["location"]["latitude"])
    longitude = float(response.json()["location"]["longitude"])
    coordinates = (latitude, longitude)
    city = response.json()["time"]["timezone"].split("/")[1]
    results = (origin_selection, coordinates, city)

    return results


def location_of_choice():
    """Returns set of geographical coordinates given by the user."""
    origin_selection = "location of choice"

    print("Please enter your location of choice (latitude followed by longitude) "
          "in decimal degrees unit format (e.g., 51.477873, 0.000000):\n")

    latitude = float(input("Select latitude:\n"))
    longitude = float(input("Select longitude:\n"))
    coordinates = (latitude, longitude)
    results = (origin_selection, coordinates)

    return results


def pseudo_random_coordinates():
    """Returns pseudo-random set of geographical coordinates."""
    origin_selection = "pseudo-random coordinates"
    lat_whole = str(randint(MIN_LAT, MAX_LAT))
    lon_whole = str(randint(MIN_LON, MAX_LON))
    lat_decimal = ""
    lon_decimal = ""

    if lat_whole == str(-90) or lat_whole == str(90):
        lat_decimal = "000000"
    elif lon_whole == str(-180) or lon_whole == str(180):
        lon_decimal = "000000"
    else:
        for _ in range(6):
            n_1 = str(randint(0, 9))
            n_2 = str(randint(0, 9))
            lat_decimal += n_1
            lon_decimal += n_2

    latitude = float(lat_whole + "." + lat_decimal)
    longitude = float(lon_whole + "." + lon_decimal)
    coordinates = (latitude, longitude)
    results = (origin_selection, coordinates)

    return results
