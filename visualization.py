import requests
import urllib
import pyproj
import matplotlib.pyplot as plt
import matplotlib.colors as c
from shapely.geometry import Polygon, Point
from utils import colors
import numpy as np
import math
import json


def plot_cell(cell: Polygon, color="blue", alpha=0.3):
    plt.fill(*cell.exterior.xy, color=color, alpha=alpha)


def plot_trajectory(cells, color="blue", alpha=0.3):
    for cell in cells:
        plot_cell(cell[0], color=color, alpha=alpha)


def plot_trajectories(gridified_trajectories, directory, show_result=False):
    plt.figure(figsize=(10, 10))
    index = 0
    for gt in gridified_trajectories:
        plot_trajectory(gt, color=colors[index])
        index += 1
        index %= len(colors)
    plt.savefig(directory + "/gridified_trajectories.png", transparent=True, dpi=1000)
    if show_result:
        plt.show()
    plt.close()


def heatmap(directory, show_result):
    # WARNING: We highly suggest you do not lay your eyes on this abomination of a function. You've been warned.
    # We also totally yanked it from someone else: https://www.geodose.com/2018/01/creating-heatmap-in-python-from-scratch.html
    
    x = []
    y = []

    with open(directory + '/data.json') as json_file:
        data = json.load(json_file)
        for k, v in data.items():
            coords = k.strip('()').split(',')
            x.extend([float(coords[0])]*v)
            y.extend([float(coords[1])]*v)

    # DEFINE GRID SIZE AND RADIUS(h)
    grid_size = 0.00005
    h = 0.001

    # GETTING X,Y MIN AND MAX
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)

    # CONSTRUCT GRID
    x_grid = np.arange(x_min-h, x_max+h, grid_size)
    y_grid = np.arange(y_min-h, y_max+h, grid_size)
    x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

    # GRID CENTER POINT
    xc = x_mesh+(grid_size/2)
    yc = y_mesh+(grid_size/2)

    # FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL
    def kde_quartic(d, h):
        dn = d/h
        P = (15/16)*(1-dn**2)**2
        return P

    # PROCESSING
    intensity_list = []
    for j in range(len(xc)):
        intensity_row = []
        for k in range(len(xc[0])):
            kde_value_list = []
            for i in range(len(x)):
                # CALCULATE DISTANCE
                d = math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
                if d <= h:
                    p = kde_quartic(d, h)
                else:
                    p = 0
                kde_value_list.append(p)
            # SUM ALL INTENSITY VALUE
            p_total = sum(kde_value_list)
            intensity_row.append(p_total)
        intensity_list.append(intensity_row)
    # HEATMAP OUTPUT
    intensity = np.array(intensity_list)
    # intensity = np.ma.masked_array(intensity, intensity < 10)
    cdict = {'red':  ((0.0, 0.0, 0.0),
                   (0.25, 0.0, 0.0),
                   (0.5, 0.0, 0.0),
                   (0.75, 0.2, 0.2),
                   (0.95, 1.0, 1.0),
                   (1.0, 0.9, 0.9)),

          'green': ((0.0, 0.0, 0.0),
                    (0.25, 0.2, 0.2),
                    (0.5, 0.3, 0.3),
                    (0.75, 0.8, 0.8),
                    (0.95, 0.7, 0.7),
                    (1.0, 0.2, 0.2)),

          'blue':  ((0.0, 0.8, 0.8),
                    (0.5, 1.0, 1.0),
                    (0.75, 0.3, 0.3),
                    (0.95, 0.2, 0.2),
                    (1.0, 0.1, 0.1))
          }
    cdict["alpha"] = ((0.0, 0.0, 0.0),
                   (0.10, 0.0, 0.0),
                   (0.5, 0.9, 0.9),
                   (0.75, 0.9, 0.9),
                   (1.0, 0.9, 0.9))
    cmap = c.LinearSegmentedColormap('BlueRed1', cdict)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.yaxis.set_major_locator(plt.NullLocator())  # remove y axis ticks
    ax.xaxis.set_major_locator(plt.NullLocator())  # remove x axis ticks
    plt.pcolormesh(x_mesh, y_mesh, intensity,
                   shading='auto', cmap=cmap)
    plt.savefig(directory + "/heatmap.png", transparent=True, dpi=1000)
    if show_result:
        plt.show()
    plt.close()


def get_map_image(ne, sw):
    lat = (ne[0] + sw[0]) / 2
    lng = (ne[1] + sw[1]) / 2
    API_KEY = "AIzaSyCD305xYeapGxQjiBaQ1prg_uag0-tK3CE"
    url = "http://maps.googleapis.com/maps/api/staticmap?"
    params = {
        "size": "400x400",
        "markers": str(lat) + "," + str(lng) + "|" + str(ne[0]) + "," + str(ne[1]) + "|" + str(sw[0]) + "," + str(sw[1]),
        "visible": str(ne[0]) + "," + str(ne[1]) + "|" + str(sw[0]) + "," + str(sw[1]),
        "key": API_KEY
    }
    url_params = urllib.parse.urlencode(params)
    url = f"{url}{url_params}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # storing the response in a file (image)
    with open('test.png', 'wb') as file:
        # writing data into the file
        file.write(response.content)


# "pk.eyJ1IjoiYm9yYXNhbnVrIiwiYSI6ImNreWJpZWx3NDBmaDkydnJpd3Rvamo2MGUifQ.Se6DkGL7m-_R8c6r9DrOJg"


def get_map_image2(sw, ne):
    to_proxy_transformer = pyproj.Transformer.from_crs(
        'epsg:4326', 'epsg:3857')
    t_sw = to_proxy_transformer.transform(sw[0], sw[1])
    t_ne = to_proxy_transformer.transform(ne[0], ne[1])
    width = str(int(t_ne[1] - t_sw[1]))
    height = str(int(t_ne[0] - t_sw[0]))
    print(width + "x" + height)
    bbox = "[" + str(sw[1]) + "," + str(sw[0]) + "," + \
        str(ne[1]) + "," + str(ne[0]) + "]"
    url = "https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/" + bbox + \
        "/" + width + "x" + height + \
        "?access_token=pk.eyJ1IjoiYm9yYXNhbnVrIiwiYSI6ImNreWJpZWx3NDBmaDkydnJpd3Rvamo2MGUifQ.Se6DkGL7m-_R8c6r9DrOJg"
    response = requests.request("GET", url)
    # storing the response in a file (image)
    with open('static_map.png', 'wb') as file:
        # writing data into the file
        file.write(response.content)
