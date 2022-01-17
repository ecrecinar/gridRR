from shapely.geometry import Point, Polygon
import pyproj

from utils import RR

def local_grid(step_size, lat, lng):
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

    loc = Point((lat, lng))
    transformed_loc = to_proxy_transformer.transform(loc.x, loc.y)

    # calculate the sw corner for the center grid, then step back once in each direction to find the grid's sw corner.
    transformed_sw = (((int)(transformed_loc[0] / step_size)) * step_size - step_size,
                      ((int)(transformed_loc[1] / step_size)) * step_size - step_size)
    transformed_ne = transformed_sw[0] + \
        (3 * step_size), transformed_sw[1] + (3 * step_size)

    tX = []
    tY = []
    grid_points = []
    cells = [[] for _ in range(9)]
    x = transformed_sw[0]
    while x <= transformed_ne[0]:
        y = transformed_sw[1]
        while y <= transformed_ne[1]:
            tX.append(x)
            tY.append(y)
            point = Point(
                to_original_transformer.transform(x, y))
            grid_points.append(point)
            y += step_size
        x += step_size

    X = []
    Y = []

    for i in range(len(grid_points)):
        X.append(grid_points[i].x)
        Y.append(grid_points[i].y)

    cells = []
    for i in range(11):
        if i == 3 or i == 7:
            continue
        cells.append([(Y[i], X[i]), (Y[i+1], X[i+1]),
                     (Y[i+5], X[i+5]), (Y[i+4], X[i+4])])

    return cells

def gridify(trajectory, step_size, rr_prob=1):
    gridified_trajectory = []
    for point in trajectory:
        cells = local_grid(step_size, point[0], point[1])
        index = RR(rr_prob)
        gridified_trajectory.append(Polygon(cells[index]))

    return gridified_trajectory