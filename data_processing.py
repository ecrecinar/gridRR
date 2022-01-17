from pathlib import Path
import os


def get_datasets():
    return sorted((f for f in os.listdir("data/datasets") if not f.startswith(".")), key=str.lower)


def get_trajectory(file, start_time, end_time):
    trajectory = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            ping = [float(x.strip()) for x in line.split(',')]
            timestamp = ping[2]
            if timestamp < start_time:
                continue
            elif timestamp > end_time:
                break
            trajectory.append(ping)
    return trajectory


def get_trajectories(dataset, start_time, end_time):
    trajectories = []
    pathlist = Path("data/datasets/" + dataset).rglob('*.txt')
    for path in pathlist:
        trajectories.append(get_trajectory(path, start_time, end_time))
    return trajectories


# TODO: Write a function that saves the gridified trajectory
# https://stackoverflow.com/questions/62046624/how-to-save-shapely-geometry-into-a-file-and-load-it-later-into-a-variable