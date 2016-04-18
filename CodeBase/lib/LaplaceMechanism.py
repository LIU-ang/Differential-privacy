import numpy as np


def laplaceMechanism(x, epsilon):
    x +=  np.random.laplace(0, epsilon, 1)[0]
    return x