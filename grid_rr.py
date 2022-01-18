import geo
from visualization import *
import data_processing as dp
from datetime import datetime
import os

DEFAULT_PROB = 0.82
DEFAULT_STEPSIZE = 20


def run(dataset, step_size, rr_prob, show_result, start_time, end_time):
    data = dp.get_trajectories(dataset, start_time, end_time)
    current_time = datetime.now().strftime("%H-%M-%S-%d-%m-%Y")
    directory = "experiments/experiment-" + current_time
    os.makedirs(directory)
    gts = []
    for trajectory in data:
        gts.append(geo.gridify(trajectory=trajectory,
                   step_size=step_size, rr_prob=rr_prob))
    plot_trajectories(gts, directory, show_result)
    dp.save_gts(gts, directory)
    heatmap(directory, show_result)
