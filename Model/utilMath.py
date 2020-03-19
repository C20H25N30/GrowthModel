# -*- coding: utf-8 -*-

"""
utilMath holds misc. math functions and constants
"""

import numpy as np

# RandGivenPercentile will output a random number from a theoretical set
# with 10th and 90th percentiles which approach those given as arguments. 
def RandGivenPercentile(xT,xN, **kwargs):
    # find est. mean and stdev of theoretical distribution
    mu, sigma = np.average([xT,xN]),np.std([xT,xN])
    # check for recursion limit
    if "recursionLimit" in kwargs.keys(): # then use recursion limit
        recursionLimit = kwargs["recursionLimit"]
    else: # set default
        recursionLimit = 2
    return randGivenPtilesGenAttempt(mu,sigma,0,recursionLimit,**kwargs)

# randGivenPtilesGenAttempt is the primary function within RandGivenPercentile
# separated for the sake of removing redundancy in recursion.
def randGivenPtilesGenAttempt(mu,sigma,depth,limit,**kwargs):
    x = np.random.normal(mu,sigma)
    if "Max" in kwargs.keys():
        if x >= kwargs["Max"]: 
            if depth <= limit:
                return randGivenPtilesGenAttempt(mu,sigma,depth+1,limit,**kwargs)
            else:
                return kwargs["Max"]
    if "Min" in kwargs.keys():
        if x <= kwargs["Min"]: 
            if depth <= limit:
                return randGivenPtilesGenAttempt(mu,sigma,depth+1,limit,**kwargs)
            else:
                return kwargs["Min"]
    return x