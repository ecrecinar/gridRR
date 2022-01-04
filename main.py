import matplotlib.pyplot as plt
import shapely.geometry
import pyproj
import random
import numpy as np
import json

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
    transformed_ne = transformed_sw[0] + \
        (3 * step_size), transformed_sw[1] + (3 * step_size)
    # print(transformed_sw)
    # print(transformed_ne)
    grid_points = []
    cells = [[] for _ in range(9)]
    x = transformed_sw[0]
    while x <= transformed_ne[0]:
        y = transformed_sw[1]
        while y <= transformed_ne[1]:
            point = shapely.geometry.Point(
                to_original_transformer.transform(x, y))
            grid_points.append(point)
            y += step_size
        x += step_size

    X = []
    Y = []

    for i in range(len(grid_points)):
        # print(grid_points[i].x, ",", grid_points[i].y)
        X.append(grid_points[i].x)
        Y.append(grid_points[i].y)

    # i = 1
    # plt.close()
    # plt.scatter(Y, X)
    # plt.ticklabel_format(useOffset=False)
    # plt.scatter([Y[i], Y[i+1], Y[i+4], Y[i+5]], [X[i], X[i+1], X[i+4], X[i+5]])
    # plt.show()

    cells = []
    for i in range(11):
        if i == 3 or i == 7:
            continue
        cells.append([(Y[i],X[i]), (Y[i+1],X[i+1]), (Y[i+4],X[i+4]),(Y[i+5],X[i+5])])

    return cells
    # print(cells)


def RR(probability):
    """[summary]

    Args:
        cell (Square): The correct cell the location lies on
        probability (float): The probability to return the correct cell

    Returns:
        Square:
    """
    if(random.random() < probability):
        return 5
    else:
        return np.random.choice(range(0,9),1,[0.125,0.125,0.125,0.125,0,0.125,0.125,0.125,0.125])[0]


def get_trajectory(file):
    locations = dict()
    trajectory = []
    lines = []
    with open(file) as f:
        lines = f.readlines()
    
    for line in lines:
        current_loc = [x.strip() for x in line.split(',')]
        cells = create_grid(STEPSIZE, float(current_loc[0]), float(current_loc[1]))
        index = RR(PROB)
        trajectory.append(cells[index])
        if str(cells[index]) in locations:
            locations[str(cells[index])] = locations[str(cells[index])] + 1
        else:
            locations[str(cells[index])] = 1
    return trajectory

user1_trajectory =  get_trajectory('user1_data.txt')   
# print(user1_trajectory)

user2_trajectory =  get_trajectory('user2_data.txt')   
# print(user2_trajectory)

user3_trajectory =  get_trajectory('user3_data.txt')   
# print(user3_trajectory)

max_entry = max(len(user1_trajectory), len(user2_trajectory), len(user3_trajectory))
print(len(user1_trajectory))
print(len(user2_trajectory))
print(len(user3_trajectory))

all_grids = user1_trajectory
all_grids.extend(user2_trajectory)
all_grids.extend(user3_trajectory)
print(all_grids)
print(len(all_grids))

# time_grid_data = {}
# counts = {}

# for i in range(len(all_grids)):
#     counts[str(all_grids[i])] = 0

# for i in range(max_entry):
#     time_grid_data[i] = counts


# for i in range(max_entry):
#     print(time_grid_data[i][str(user1_trajectory[i])])
#     print(time_grid_data[i][str(user2_trajectory[i])])
#     if i < len(user1_trajectory):
#         time_grid_data[i][str(user1_trajectory[i])] = time_grid_data[i][str(user1_trajectory[i])] + 1
#     if i < len(user2_trajectory):
#         time_grid_data[i][str(user2_trajectory[i])] = time_grid_data[i][str(user2_trajectory[i])] + 1
#     if i < len(user3_trajectory):
#         time_grid_data[i][str(user3_trajectory[i])] = time_grid_data[i][str(user3_trajectory[i])] + 1

# # print(time_grid_data)
# with open("test.json", "w") as outfile:
#     json.dump(time_grid_data, outfile)