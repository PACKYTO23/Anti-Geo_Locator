import requests
from random import randint
import geopy.distance as d
import geopy.point as p

# DESTINATION TO BE BASED ON SELECTED LOCATION, RANDOM OR DISTANCE RANGE AND ORIENTATION OR IP ADDRESS
# REVERSE GEOCODING AND GEOLOCATION SERVICE API

IP_GEO_LOCATION_VISITOR_LOOKUP = "https://ip-geo-location.p.rapidapi.com/ip/check"
API_KEY = "e37837191amsh73b18fbdb45f29bp122ac8jsn1741eeaefc5a"  # SEND TO ENVIRONMENT VARIABLES.
API_HOST = "ip-geo-location.p.rapidapi.com"

MIN_LAT = -90
MAX_LAT = 90
MIN_LON = -180
MAX_LON = 180

M_TO_KM_FACTOR = 1.609344  # 25146/15625
KM_TO_M_FACTOR = 1 / M_TO_KM_FACTOR  # 0.621371192237334


def location_of_choice():
    """Returns set of geographical coordinates given by the user."""
    destination_selection = "location of choice"
    print("Please enter your location of choice (latitude followed by longitude) "
          "in decimal degrees unit format (e.g., 51.477873, 0.000000):\n")

    latitude = float(input("Select latitude:\n"))
    longitude = float(input("Select longitude:\n"))
    coordinates = (latitude, longitude)
    results = (destination_selection, coordinates)

    return results


def pseudo_random_coordinates():
    """Returns pseudo-random set of geographical coordinates."""
    destination_selection = "pseudo-random coordinates"
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
    results = (destination_selection, coordinates)

    return results


def distance_range_orientation(o_lat, o_lon):
    """Returns set of geographical coordinates given the user's distance range from origin point and orientation."""
    destination_selection = "distance range and orientation"
    print("Please enter the distance at which you want to find your destination\n"
          "as well as the orientation of said distance with respect from the origin point.\n"
          "\nConsider the following as for how the degrees for orientation work:\n"
          "0 = North  |  90 = East  |  180 = South  |  270 = West\n"
          "E.g., 45.0 would be precisely Northeast "
          "while 210.827463 would be somewhere in the South-southwest area.\n")

    kilometers = 0
    distance_unit = input("What distance unit do you prefer? 'km' for kilometers, 'm' for miles:\n").lower()
    distance_quantity = float(input("Select amount of distance:\n"))

    if distance_unit == "kilometers" or distance_unit == "km":
        kilometers = distance_quantity
    elif distance_unit == "miles" or distance_unit == "m":
        kilometers = distance_quantity * M_TO_KM_FACTOR

    orientation = float(input("Select degree of orientation:\n"))
    destination_point = str(d.distance(kilometers=kilometers).destination((o_lat, o_lon), bearing=orientation))
    destination_coordinates = destination_point.split(",")
    semi_latitude = destination_coordinates[0].split(" ")
    semi_longitude = destination_coordinates[1].split(" ")
    lat_degrees = int(semi_latitude[0])
    lon_degrees = int(semi_longitude[1])
    lat_arc_minutes = int(semi_latitude[1].split("m")[0])
    lon_arc_minutes = int(semi_longitude[2].split("m")[0])
    lat_arc_seconds = float(semi_latitude[2].split("s")[0])
    lon_arc_seconds = float(semi_longitude[3].split("s")[0])
    lat_direction = semi_latitude[3]
    lon_direction = semi_longitude[4]
    latitude = float("{:.9f}".format(p.Point.parse_degrees(degrees=lat_degrees, arcminutes=lat_arc_minutes,
                                                           arcseconds=lat_arc_seconds, direction=lat_direction)))
    longitude = float("{:.9f}".format(p.Point.parse_degrees(degrees=lon_degrees, arcminutes=lon_arc_minutes,
                                                            arcseconds=lon_arc_seconds, direction=lon_direction)))
    coordinates = (latitude, longitude)
    results = (destination_selection, coordinates, distance_unit)

    return results


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
