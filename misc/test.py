# l = []

# l.append([("A", i) for i in range(15)])
# l.append([("B", i) for i in range(15, 20)])
# l.append([("C", i) for i in range(20, 25)])

# log = []
# for item in l:
#     for p in item:
#         log.append(p)

# condensed_log = []

# current_item = log[0][0]
# start_time = log[0][1]
# end_time = start_time
# for i in range(len(log)):
#     if i == len(log) - 1:
#         condensed_log.append((current_item, start_time, end_time))

#     if log[i][0] == current_item:
#         end_time = log[i][1]
#     else:
#         condensed_log.append((current_item, start_time, end_time))
#         current_item = log[i][0]
#         start_time = log[i][1]
#         end_time = start_time

# for item in log:
#     print(item)

# for item in condensed_log:
#     print(item)


# user1_trajectory = get_trajectory('user1_data.txt')
# # print(user1_trajectory)

# user2_trajectory =  get_trajectory('user2_data.txt')
# # print(user2_trajectory)

# user3_trajectory =  get_trajectory('user3_data.txt')
# # print(user3_trajectory)

# max_entry = max(len(user1_trajectory), len(user2_trajectory), len(user3_trajectory))
# print(len(user1_trajectory))
# print(len(user2_trajectory))
# print(len(user3_trajectory))

# all_grids = user1_trajectory
# all_grids.extend(user2_trajectory)
# all_grids.extend(user3_trajectory)
# print(all_grids)
# print(len(all_grids))

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

# create_grid(100, 13.37, 12.04)

# i = 10
# plt.close()
# plt.figure(figsize=(6, 6))
# plt.scatter([lng], [lat], color="red")
# plt.ticklabel_format(useOffset=False)
# plt.scatter(Y, X, color="black")
# plt.scatter([Y[i], Y[i+1], Y[i+4], Y[i+5]],
#             [X[i], X[i+1], X[i+4], X[i+5]], color="blue")
# plt.show()


# EPSG_3857_SW_X = -20026376.39
# EPSG_3857_SW_Y = -20048966.10
# EPSG_3857_NE_X = 20026376.39
# EPSG_3857_NE_Y = 20048966.10

# import os

# print(sorted((f for f in os.listdir() if not f.startswith(".")), key=str.lower))

# import matplotlib.pyplot as plt
# import numpy as np
# import math

# x=[20,28,15,20,18,25,15,18,18,20,25,30,25,22,30,22,38,40,38,30,22,20,35,33,35]
# y=[20,14,15,20,15,20,32,33,45,50,20,20,20,25,30,38,20,28,33,50,48,40,30,35,36]

# #DEFINE GRID SIZE AND RADIUS(h)
# grid_size=1
# h=10

# #GETTING X,Y MIN AND MAX
# x_min=min(x)
# x_max=max(x)
# y_min=min(y)
# y_max=max(y)

# #CONSTRUCT GRID
# x_grid=np.arange(x_min-h,x_max+h,grid_size)
# y_grid=np.arange(y_min-h,y_max+h,grid_size)
# x_mesh,y_mesh=np.meshgrid(x_grid,y_grid)

# #GRID CENTER POINT
# xc=x_mesh+(grid_size/2)
# yc=y_mesh+(grid_size/2)

# #FUNCTION TO CALCULATE INTENSITY WITH QUARTIC KERNEL
# def kde_quartic(d,h):
#     dn=d/h
#     P=(15/16)*(1-dn**2)**2
#     return P

# #PROCESSING
# intensity_list=[]
# for j in range(len(xc)):
#     intensity_row=[]
#     for k in range(len(xc[0])):
#         kde_value_list=[]
#         for i in range(len(x)):
#             #CALCULATE DISTANCE
#             d=math.sqrt((xc[j][k]-x[i])**2+(yc[j][k]-y[i])**2)
#             if d<=h:
#                 p=kde_quartic(d,h)
#             else:
#                 p=0
#             kde_value_list.append(p)
#         #SUM ALL INTENSITY VALUE
#         p_total=sum(kde_value_list)
#         intensity_row.append(p_total)
#     intensity_list.append(intensity_row)

# #HEATMAP OUTPUT
# intensity=np.array(intensity_list)
# plt.pcolormesh(x_mesh,y_mesh,intensity)
# plt.plot(x,y,'ro')
# plt.colorbar()
# plt.show()

# cell = Polygon([(1,1),(1,2),(2,2),(2,1),(1,1)])
# id = str(*cell.exterior.centroid.coords)
# print(id)

import json
from shapely.geometry import Polygon
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.colors as c

x = []
y = []

with open('data.json') as json_file:
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
cm = {'red':  ((0.0, 0.0, 0.0),
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
cm["alpha"] = ((0.0, 0.0, 0.0),
               (0.10, 0.0, 0.0),
               (0.5, 0.9, 0.9),
               (0.75, 0.9, 0.9),
               (1.0, 0.9, 0.9))
blue_red1 = c.LinearSegmentedColormap('BlueRed1', cm)
fig, ax = plt.subplots(1, 1, figsize=(8,8))
ax.yaxis.set_major_locator(plt.NullLocator())  # remove y axis ticks
ax.xaxis.set_major_locator(plt.NullLocator())  # remove x axis ticks
plt.pcolormesh(x_mesh, y_mesh, intensity,
               shading='auto', cmap=blue_red1)
# plt.plot(x,y,'ro')
plt.savefig("result.png", transparent=True, dpi=1000)
plt.show()
