import requests

# DETECT IF BOTH LOCATIONS ARE LOCATED ON WATER
# REVERSE GEOCODING AND GEOLOCATION SERVICE API

R_G_AND_G_S_IS_ON_WATER = "https://geocodeapi.p.rapidapi.com/isonwater"
API_KEY = "e37837191amsh73b18fbdb45f29bp122ac8jsn1741eeaefc5a"  # SEND TO ENVIRONMENT VARIABLES.
API_HOST = "geocodeapi.p.rapidapi.com"


def yes_no_water(o_lat, o_lon, d_lat, d_lon):
    """Return boolean checking if locations are on water and if they do determine if on lake or sea."""
    results = None
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST,
    }

    origin_query = {"lat": o_lat, "lon": o_lon}
    destination_query = {"lat": d_lat, "lon": d_lon}
    origin_response = requests.get(url=R_G_AND_G_S_IS_ON_WATER, headers=headers, params=origin_query)
    destination_response = requests.get(url=R_G_AND_G_S_IS_ON_WATER, headers=headers, params=destination_query)
    origin_data = origin_response.json()
    destination_data = destination_response.json()

    if not origin_data["isOnWater"] and not destination_data["isOnWater"]:
        results = "Neither of your locations is on water."

    elif not origin_data["isOnWater"] and destination_data["isOnWater"]:
        if destination_data["sea"]:
            d_sea_or_lake = "sea"
        else:
            d_sea_or_lake = "lake"

        results = (f"Your origin location isn't on water, "
                   f"but your destination location is, specifically, on a {d_sea_or_lake}.")

    elif origin_data["isOnWater"] and not destination_data["isOnWater"]:
        if origin_data["sea"]:
            o_sea_or_lake = "sea"
        else:
            o_sea_or_lake = "lake"

        results = (f"Your origin location is on water, specifically, on a {o_sea_or_lake}, "
                   f"but your destination location isn't on water.")

    elif origin_data["isOnWater"] and destination_data["isOnWater"]:
        if origin_data["sea"]:
            o_sea_or_lake = "sea"
        else:
            o_sea_or_lake = "lake"

        if destination_data["sea"]:
            d_sea_or_lake = "sea"
        else:
            d_sea_or_lake = "lake"

        results = (f"Your origin location is on water, specifically, on a {o_sea_or_lake}, "
                   f"as well as your destination location, specifically, on a {d_sea_or_lake}.")

    return results
