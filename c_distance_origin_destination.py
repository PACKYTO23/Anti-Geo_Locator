import geopy.distance as d

# GET DISTANCE BETWEEN BOTH SETS OF COORDINATES
# GEOPY


def calculate_distance(o_lat, o_lon, d_lat, d_lon):
    """Returns distance between both sets of geographical coordinates."""
    origin_coordinates = (o_lat, o_lon)
    destination_coordinates = (d_lat, d_lon)
    distance_inbetween = float("{:.4f}".format(d.distance(origin_coordinates, destination_coordinates).kilometers))

    return distance_inbetween
