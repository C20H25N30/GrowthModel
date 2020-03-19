# -*- coding: utf-8 -*-

# INTERFACE model for Logger
## AND HAS METHOD ".Log(Object, **kwargs)"
## it serves as a safely composable wrapper

class Logger:
    def __init__(self,logger):
        if str(type(logger)) == "<class 'type'>":
            self.Log = self.classLog
            self.logger = logger()
        else:
            self.Log = self.functionLog
            self.logger = logger
    def functionLog(self, Object, **kwargs):
        self.logger(Object,**kwargs)
    def classLog(self, Object, **kwargs):
        self.logger.Log(Object,**kwargs)

    