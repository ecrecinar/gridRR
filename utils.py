import random
import numpy as np

colors = [
    "#8B008B",
    "#6A5ACD",
    "#CD5C5C",
    "#FF4500",
    "#2E8B57",
    "#20B2AA",
    "#9ACD32",
    "#0000CD",
    "#BC8F8F"
]


def RR(probability):
    """[summary]

    Args:
        probability (float): The probability to return the correct cell

    Returns:
        index (int): The index of the center cell with given probability, otherwise a random neighbor.
    """
    if(random.random() < probability):
        return 5
    else:
        return np.random.choice(range(0, 9), 1, [0.125, 0.125, 0.125, 0.125, 0, 0.125, 0.125, 0.125, 0.125])[0]
