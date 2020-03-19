# -*- coding: utf-8 -*-

"""
utilMath holds misc. math functions and constants
"""

import numpy as np

# RandGivenPercentile will output a random number from a theoretical set
# with 10th and 90th percentiles which approach those given as arguments


def RandGivenPercentile(xT, xN, **kwargs):
    # find est. mean and stdev of theoretical distribution
    # Calculates mean and variance given xT and xN.
    # I think this still may be overestimate of std.dev because the fxn expects that the two numbers given are randomly drawn from Dist. Whereas these two numbers are indeed from the dist, but reflect two relatively variable and non-random choices
    mu, sigma = np.average([xT, xN]), np.std([xT, xN])
    # check for recursion limit
    # use recursion limit if specified, otherwise use 2.
    if "recursionLimit" in kwargs.keys():
        recursionLimit = kwargs["recursionLimit"]
    else:  # set default recursionLimit
        recursionLimit = 2
    return randGivenPtilesGenAttempt(mu, sigma, 0, recursionLimit, **kwargs)

# randGivenPtilesGenAttempt is the primary function within RandGivenPercentile
# separated for the sake of removing redundancy in recursion.


def randGivenPtilesGenAttempt(mu, sigma, depth, limit, **kwargs):
    x = np.random.normal(mu, sigma)
    # if there is a min/max, and generated value "x" is outside these bounds
    # AND we have not exceeded our recursion depth limit, we will attempt to
    # generate again, if not, we will return the given max.
    # This affords n opportunities to redistribute within the bounds.
    # This reduces the accuracy of the mapping between input and output 10th
    # and 90th percentiles when percentiles that create variance which push
    # tails toward an edge are used.
    # This is acceptable, given that some theoretical distributions, implied
    # by the given percentile values, are impossible when paired with arbitrary
    # limits, i.e. a distribution with a maximum value of 1 that has a 10th
    # percentile of .8 and a 90th percentile of 1.
    if "Max" in kwargs.keys():
        if x >= kwargs["Max"]:
            if depth <= limit:
                return randGivenPtilesGenAttempt(mu, sigma, depth+1, limit, **kwargs)
            else:
                return kwargs["Max"]
    if "Min" in kwargs.keys():
        if x <= kwargs["Min"]:
            if depth <= limit:
                return randGivenPtilesGenAttempt(mu, sigma, depth+1, limit, **kwargs)
            else:
                return kwargs["Min"]
    return x
