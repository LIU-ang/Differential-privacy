import math
import random

def exponentialMechanism(score, scoreFuncSensitivity, epsilon):
    prScore = math.exp(epsilon * score / (2 * scoreFuncSensitivity))
    return prScore