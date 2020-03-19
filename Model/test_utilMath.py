# -*- coding: utf-8 -*-
"""
Testing segments for utilMath.py
"""
"""
import matplotlib.pyplot as plt
import numpy as np
import utilMath

#Testing RandGivenPercentile
def getWalkParams(xT,xN):
    return np.average([xT,xN]),np.std([xT,xN])

# Generator Object
class testWalk:
    def __init__(self,count,xT,xN, **kwargs):
        self.xT = xT
        self.xN = xN
        self.MaxCt = count
        self.Count = 0
        self.kwargs = kwargs
    def __iter__(self):
        return self
    def __next__(self):
        if self.Count >= self.MaxCt:
            raise StopIteration
        self.Count += 1
        return utilMath.RandGivenPercentile(self.xT,self.xN,**self.kwargs)

#parameters
xT = 0.4
xN = 0.9
mu,sigma = np.mean([xN,xT]),np.std(([xN,xT]))
x = testWalk(100000,xN,xT,Max=1, Min = 0, recursionLimit = 3)

#run generator
Array = []
for i in x:
    Array.append(i)

# print stats-lite
mu2,sigma2 = np.mean(Array),np.std(Array)
print("Given Mu, Sigma: ",mu, sigma)
print("Found Mu, Sigma: ", mu2, sigma2)
print("Given 10th: ", xT)
print("Found 10th: ", np.percentile(Array,10))
print("Given 90th: ", xN)
print("Found 90th: ", np.percentile(Array,90))

# print chart
count, bins, ignored = plt.hist(Array, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')

plt.xlim(0,1)
plt.show()
"""
#%%

