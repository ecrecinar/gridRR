import geo
from utils import colors
from visualization import *
from matplotlib.ticker import NullFormatter, FixedLocator
import data_processing as dp
from datetime import datetime
import os

DEFAULT_PROB = 0.82
DEFAULT_STEPSIZE = 20


def run(step_size=DEFAULT_STEPSIZE, rr_prob=DEFAULT_PROB, show_result=False):
    data = dp.get_trajectories()
    current_time = datetime.now().strftime("%H-%M-%S-%d-%m-%Y")
    directory = "experiments/experiment-" + current_time
    os.makedirs(directory)
    gts = []
    for trajectory in data:
        gts.append(geo.gridify(trajectory=trajectory,
                   step_size=step_size, rr_prob=rr_prob))
    plot_trajectories(gts, directory, show_result)
