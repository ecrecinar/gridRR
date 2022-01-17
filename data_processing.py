from os import system
from pathlib import Path

def get_trajectory(file):
    trajectory = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            current_loc = [float(x.strip()) for x in line.split(',')]
            trajectory.append(current_loc)
    return trajectory


def get_trajectories():
    trajectories = []
    pathlist = Path("data/users").rglob('*.txt')
    for path in pathlist:
        trajectories.append(get_trajectory(path))
    return trajectories


# TODO: Write a function that saves the gridified trajectory