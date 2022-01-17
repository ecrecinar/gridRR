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
