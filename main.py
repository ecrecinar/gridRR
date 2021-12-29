import matplotlib.pyplot as plt
import shapely.geometry
import pyproj
import random

# Default values
PROB = 0.82
STEPSIZE = 100


def create_grid(step_size, southwest, northeast):
    """
        Create a square grid for the rectangular area defined by the southwest and northeast coordinates.


    Args:
        step_size (int): The side length of each square grid cell in meters
        southwest (tuple): The latitude/longitude pair defining the southwest corner of the area
        northeast (tuple): The latitude/longitude pair defining the northeast corner of the area


    Returns:
        array: Array of square objects corresponding to each cell in the grid

    Note: This solution is inspired by [this stackoverflow post](https://stackoverflow.com/a/40343603)
    """
    # Transformers between the original latitude/longitude system (ESPG:4326) and a meter-based projection (ESPG:3857)
    to_proxy_transformer = pyproj.Transformer.from_crs(
        'epsg:4326', 'epsg:3857')
    to_original_transformer = pyproj.Transformer.from_crs(
        'epsg:3857', 'epsg:4326')

    sw = shapely.geometry.Point(southwest)
    ne = shapely.geometry.Point(northeast)

    # Transform the points to the meter-based system
    transformed_sw = to_proxy_transformer.transform(sw.x, sw.y)
    transformed_ne = to_proxy_transformer.transform(ne.x, ne.y)

    grid_points = []
    x = transformed_sw[0]
    while x < transformed_ne[0]:
        y = transformed_sw[1]
        while y < transformed_ne[1]:
            point = shapely.geometry.Point(to_original_transformer.transform(x, y))
            grid_points.append(point)
            print(len(grid_points))
            y += step_size
        x += step_size

    plt.scatter([p.x for p in grid_points], [p.y for p in grid_points])
    plt.show()

    


# def get_grid(cells, location):
#     """
#         Finds the corresponding cell of the location

#     Args:
#         grids (array): Array of square objects corresponding to each cell in the grid
#         location (tuple): x and y coordinates of the location

#     Returns:
#         Square: The square which the location lies on
#     """
#     for cell in cells:
#         if cell.location in  # the boundries of the cell
#         return cell
#     return None


def RR(cell, probability):
    """[summary]

    Args:
        cell (Square): The correct cell the location lies on
        probability (float): The probability to return the correct cell

    Returns:
        Square: 
    """
    if(random.random(0, 1) < probability):
        return cell
    else:
        return None


# def gridRR(location, probability):
#     grid =
#     cell = get_grid(location)
#     return RR(cell, probability)


# cells = create_grid(STEP_SIZE, SOUTHWEST, NORTHEAST)
# LDP_grid = kkgridRR()

create_grid(5000, (-5.0, 40.0), (-4.0, 41.0))