"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(args)



def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    reordered_wagon = each_wagons_id[2:] + each_wagons_id[:2]
    return reordered_wagon[:1] + missing_wagons + reordered_wagon[1:]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_dict = kwargs
    stops_list = list(stops_dict.values())
    route["stops"] = stops_list
    return route




def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extend_route = {**route, **more_route_information}
    return extend_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    new_matrix = [[] for _ in range(3)]

    for old_row_idx in range(3):
        for old_colon_idx in range(3):
            data = wagons_rows[old_row_idx][old_colon_idx]
            new_matrix[old_colon_idx].append(data)

    return new_matrix


