# -*- coding: utf-8 -*-

"""
utilMath holds misc. math functions and constants
"""

import numpy as np

walkStdev = 0.779

# Walk takes the est. 10th percentile and 90th percentile values of a theoretical dataset
# and creates a random value within a normally distributed set that has matching
# 10th and 90th percentile values.
def Walk(x10th,x90th,**kwargs):
    rng = np.random.normal(0, walkStdev)
    x = rng * ((x90th-x10th)/2) +(x10th+x90th)/2
    if "Max" in kwargs.keys():
        if x > kwargs["Max"]:
            return kwargs["Max"]
    if "Min" in kwargs.keys():
        if x < kwargs["Min"]:
            return kwargs["Min"]
    return x