import requests
import urllib
import pyproj
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
from utils import colors


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
    plt.savefig(directory + "/result.png", transparent=True, dpi=1000)
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
