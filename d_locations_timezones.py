import requests

# DETECT BOTH LOCATION'S TIMEZONES
# REVERSE GEOCODING AND GEOLOCATION SERVICE API

R_G_AND_G_S_GET_TIMEZONE = "https://geocodeapi.p.rapidapi.com/GetTimezone"
API_KEY = "e37837191amsh73b18fbdb45f29bp122ac8jsn1741eeaefc5a"  # SEND TO ENVIRONMENT VARIABLES.
API_HOST = "geocodeapi.p.rapidapi.com"


def timezones(o_lat=35.15, o_lon=-15.78, d_lat=-80, d_lon=58):
    """Returns timezones of both locations."""
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST,
    }

    origin_query = {"latitude": o_lat, "longitude": o_lon}
    destination_query = {"latitude": d_lat, "longitude": d_lon}
    origin_response = requests.get(url=R_G_AND_G_S_GET_TIMEZONE, headers=headers, params=origin_query)
    destination_response = requests.get(url=R_G_AND_G_S_GET_TIMEZONE, headers=headers, params=destination_query)
    origin_data = origin_response.json()
    destination_data = destination_response.json()
    origin_local_time = origin_data["LocalTime_Now"]
    destination_local_time = destination_data["LocalTime_Now"]
    origin_timezone_id = origin_data["TimeZoneId"]
    destination_timezone_id = destination_data["TimeZoneId"]
    origin_time_data = (origin_local_time, origin_timezone_id)
    destination_time_data = (destination_local_time, destination_timezone_id)
    results = (origin_time_data, destination_time_data)

    return results
