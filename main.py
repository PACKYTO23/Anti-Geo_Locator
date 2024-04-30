import a_origin_coordinates_location as origin
import b_destination_coordinates_location as destination
import c_distance_origin_destination as distance
import d_locations_timezones as timezones
import e_locations_on_water as water
import f_art as art

wanting_more_places = True


def anti_geo_locator():
    def origin_choice():  # Origin's Section----------------------------------------------------------------------------
        selection = None
        location_source = input("Please select the origin option desired.\n\n"
                                "Take into account that the ip address option will require your permission:\n"
                                "IP Address  |  Location of Choice  |  Random Coordinates\n").lower()

        if location_source == "ip address" or location_source == "ip":
            permission = input("Do you grant permission for us to locate your geographical coordinates "
                               "via your ip address?  Yes  |  No:\n").lower()

            if permission == "yes" or permission == "y":
                selection = origin.ip_address()
            elif permission == "no" or permission == "n":
                selection = None

                print("You'll need to select a location of choice or a set of random coordinates.\n\n")

                origin_choice()

        elif location_source == "location of choice" or location_source == "choice":
            selection = origin.location_of_choice()
        elif location_source == "random coordinates" or location_source == "random":
            selection = origin.pseudo_random_coordinates()

        return selection

    origin_source = origin_choice()

    print(f"\n---------------------------------------------------------------------------\n"
          f"This is your origin method: {origin_source[0]}\n"
          f"These are your origin coordinates: {origin_source[1]}"
          f"\n---------------------------------------------------------------------------")  # -------------------------

    def destination_choice():  # Destination's Section------------------------------------------------------------------
        selection = None
        semi_o_coordinates = origin_source[1]
        o_lat = float(semi_o_coordinates[0])
        o_lon = float(semi_o_coordinates[1])
        location_source = input("\nPlease select the destination option desired:\n"
                                "Take into account that the ip address option will require your permission:\n"
                                "Location of Choice  |  Random Coordinates  |  "
                                "Distance Range and Orientation  |  IP Address\n").lower()

        if location_source == "ip address" or location_source == "ip":
            permission = input("Do you grant permission for us to locate your geographical coordinates "
                               "via your ip address?  Yes  |  No:\n").lower()

            if permission == "yes" or permission == "y":
                selection = origin.ip_address()
            elif permission == "no" or permission == "n":
                selection = None

                print("You'll need to select a location of choice or a set of random coordinates.\n\n")

                destination_choice()

        elif location_source == "location of choice" or location_source == "choice":
            selection = destination.location_of_choice()
        elif location_source == "random coordinates" or location_source == "random":
            selection = destination.pseudo_random_coordinates()
        elif location_source == "distance range and orientation" or location_source == "distance":
            selection = destination.distance_range_orientation(o_lat, o_lon)

        return selection

    destination_source = destination_choice()

    print(f"\n---------------------------------------------------------------------------\n"
          f"This is your destination method: {destination_source[0]}\n"
          f"These are your destination coordinates: {destination_source[1]}"
          f"\n---------------------------------------------------------------------------")  # -------------------------

    def coordinates_distance():  # Distance's Section-------------------------------------------------------------------
        selection = None
        semi_o_coordinates = origin_source[1]
        semi_d_coordinates = destination_source[1]
        o_lat = float(semi_o_coordinates[0])
        o_lon = float(semi_o_coordinates[1])
        d_lat = float(semi_d_coordinates[0])
        d_lon = float(semi_d_coordinates[1])
        distance_unit = (input("\nWhat distance unit do you prefer the results in? "
                               "'km' for kilometers, 'm' for miles:\n").lower())

        if len(destination_source) == 3:
            origin_unit = destination_source[2]

            if (origin_unit == "kilometers" or origin_unit == "km" and
                    distance_unit == "kilometers" or distance_unit == "km"):
                selection = "{:.6f}".format(distance.calculate_distance(o_lat, o_lon, d_lat, d_lon))
            elif (origin_unit == "kilometers" or origin_unit == "km" and
                  distance_unit == "miles" or distance_unit == "m"):
                selection = "{:.6f}".format(distance.calculate_distance(o_lat, o_lon, d_lat, d_lon) *
                                            destination.KM_TO_M_FACTOR)
            elif (origin_unit == "miles" or origin_unit == "m" and
                  distance_unit == "kilometers" or distance_unit == "km"):
                selection = "{:.6f}".format(distance.calculate_distance(o_lat, o_lon, d_lat, d_lon) *
                                            destination.M_TO_KM_FACTOR)
            elif (origin_unit == "miles" or origin_unit == "m" and
                  distance_unit == "miles" or distance_unit == "m"):
                selection = "{:.6f}".format(distance.calculate_distance(o_lat, o_lon, d_lat, d_lon))

        else:
            selection = distance.calculate_distance(o_lat, o_lon, d_lat, d_lon)

        results = (selection, distance_unit)

        return results

    distance_source = coordinates_distance()  # ------------------------------------------------------------------------

    def check_timezones():  # Timezones' Section------------------------------------------------------------------------
        semi_o_coordinates = origin_source[1]
        semi_d_coordinates = destination_source[1]
        o_lat = str(semi_o_coordinates[0])
        o_lon = str(semi_o_coordinates[1])
        d_lat = str(semi_d_coordinates[0])
        d_lon = str(semi_d_coordinates[1])
        timezones_location = timezones.timezones(o_lat, o_lon, d_lat, d_lon)

        return timezones_location

    timezones_source = check_timezones()  # ----------------------------------------------------------------------------

    def check_water():  # Water's Section-------------------------------------------------------------------------------
        semi_o_coordinates = origin_source[1]
        semi_d_coordinates = destination_source[1]
        o_lat = str(semi_o_coordinates[0])
        o_lon = str(semi_o_coordinates[1])
        d_lat = str(semi_d_coordinates[0])
        d_lon = str(semi_d_coordinates[1])
        water_location = water.yes_no_water(o_lat, o_lon, d_lat, d_lon)

        return water_location

    water_source = check_water()  # ------------------------------------------------------------------------------------

    if origin_source[1] == destination_source[1]:
        data = (f"\n\n_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                f"Your location of origin was based on {origin_source[0]} at {origin_source[1]}; "
                f"its local time is {timezones_source[0][0]} belonging to the {timezones_source[0][1]} timezone id.\n"
                f"Your location of destination was based on {destination_source[0]} at {destination_source[1]}; "
                f"its local time is {timezones_source[1][0]} belonging to the {timezones_source[1][1]} timezone id.\n"
                f"Your origin is at the exact same point of your destination, so 0.0 {distance_source[1]} it is!\n"
                f"{water_source}\n"
                f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n\n")
    else:
        data = (f"\n\n_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n"
                f"Your location of origin was based on {origin_source[0]} at {origin_source[1]}; "
                f"its local time is {timezones_source[0][0]} belonging to the {timezones_source[0][1]} timezone id.\n"
                f"Your location of destination was based on {destination_source[0]} at {destination_source[1]}; "
                f"its local time is {timezones_source[1][0]} belonging to the {timezones_source[1][1]} timezone id.\n"
                f"The distance between your origin and destination is of {distance_source[0]} {distance_source[1]}.\n"
                f"{water_source}\n"
                f"_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_|-|_\n\n")

    print(data)


def need_more_locations():
    more_locations = input("Would you like to explore and discover more places?  Yes  |  No:\n").lower()

    if more_locations == "no" or more_locations == "n":
        print("\nWe'll explore more interesting locations next time! See you soon! 🤓🗺📍")
        global wanting_more_places
        wanting_more_places = False
    elif more_locations == "yes" or more_locations == "y":
        pass


print(f"\nWelcome to the ANTI-GEO LOCATOR!\n{art.art}\nHere you'll be able to explore locations, distances between them"
      f"and their timezones based on specific characteristics given by you. Let's begin!\n")

while wanting_more_places:
    anti_geo_locator()
    need_more_locations()
