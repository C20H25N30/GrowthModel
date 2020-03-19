# -*- coding: utf-8 -*-
"""
#Testing class Logger from logger.py
import logger as l
def loggerPrint(Object,**kwargs):
    if "data" in kwargs.keys():
        print(kwargs["data"])
    else:
        return
    
class loggerStoreAndPrint:
    def __init__(self):
        self.count = 0
    def Log(self,Object,**kwargs):
        print(self.count, kwargs["data"])
        self.count +=1

L1 = l.Logger(loggerPrint)
L2 = l.Logger(loggerStoreAndPrint)

for i in range(5):
    L1.Log("",data=i)
    
for i in range(5):
    L2.Log("",data=i)
"""
#%%