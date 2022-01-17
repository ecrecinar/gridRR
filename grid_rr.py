import geo
from utils import colors
from visualization import *
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedLocator
import data_processing as dp
import numpy as np

PROB = 0.82
STEPSIZE = 10

data = dp.get_trajectories()

gts = []
for trajectory in data:
    gts.append(geo.gridify(trajectory=trajectory, step_size=5, rr_prob=1))

plot_trajectories(gts)
