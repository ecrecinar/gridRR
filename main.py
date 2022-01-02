import matplotlib.pyplot as plt
import shapely.geometry
import pyproj
import random
import numpy as np

PROB = 0.82
STEPSIZE = 100
EPSG_3857_SW_X = -20026376.39
EPSG_3857_SW_Y = -20048966.10
EPSG_3857_NE_X = 20026376.39
EPSG_3857_NE_Y = 20048966.10


def create_grid(step_size, lat, lng):
    """
        Create a local square grid around the given location. The resulting grid aligns with the global grid.

    Args:
        step_size (int): The side length of each square grid cell in meters
        southwest (tuple): The latitude/longitude pair defining the southwest corner of the area
        northeast (tuple): The latitude/longitude pair defining the northeast corner of the area

    Returns:
        array: Array of square objects corresponding to each cell in the grid

    Note: This function is inspired by [this stackoverflow post](https://stackoverflow.com/a/40343603).
    """
    # Transformers between the original latitude/longitude system (ESPG:4326) and a meter-based projection (ESPG:3857)
    to_proxy_transformer = pyproj.Transformer.from_crs(
        'epsg:4326', 'epsg:3857')
    to_original_transformer = pyproj.Transformer.from_crs(
        'epsg:3857', 'epsg:4326')

    loc = shapely.geometry.Point((lat, lng))
    transformed_loc = to_proxy_transformer.transform(loc.x, loc.y)

    # calculate the sw corner for the center grid, then step back once in each direction to find the grid's sw corner.
    transformed_sw = (((int)(transformed_loc[0] / step_size)) * step_size - step_size,
                      ((int)(transformed_loc[1] / step_size)) * step_size - step_size)
    transformed_ne = transformed_sw[0] + (3 * step_size), transformed_sw[1] + (3 * step_size)
    print(transformed_sw)
    print(transformed_ne)
    grid_points = []
    x = transformed_sw[0]
    while x <= transformed_ne[0]:
        y = transformed_sw[1]
        while y <= transformed_ne[1]:
            point = shapely.geometry.Point(
                to_original_transformer.transform(x, y))
            grid_points.append(point)
            y += step_size
        x += step_size



def RR(cells, probability):
    """[summary]

    Args:
        cell (Square): The correct cell the location lies on
        probability (float): The probability to return the correct cell

    Returns:
        Square:
    """
    if(random.random(0, 1) < probability):
        return cells[5]
    else:
        cells[5] = 0
        cells.remove(0)
        return np.random.choice(cells)


# def (step_size, lat, lng, probability):
#    cells = create_grid(step_size, lat, lng)
#    return RR(cells, probability)


# LDP_grid = gridRR(STEPSIZE, LAT, LNG, PROB)

create_grid(100, 0, 0)
