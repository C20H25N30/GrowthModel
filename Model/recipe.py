# -*- coding: utf-8 -*-

"""
recipe.py provides wrappers for process lists
"""

# Recipe acts as a wrapper and generator for an array of process items.
class Recipe:
    def __init__(self, **kwargs):
        if "Ingredients" in kwargs.keys():
            self.ingredients = kwargs["Ingredients"]
        else:
            self.ingredients = []
        self.idx = 0
    # Iterator returns a deepcopy to prevent resetting of index
    # when/if a process, being run by a recipe invoked by an object
    # calls another object to invoke and run the same recipe
    def Iterator(self):
        return Recipe(Ingredients=self.ingredients)
    def Add(self, *args):
        for process in args:
            self.ingredients.append(process)
    def __iter__(self):
        # whenever iter is called, the index is reset to 0
        #self.idx = 0
        return self
    def __next__(self):
        if self.idx >= len(self.ingredients):
            raise StopIteration
        self.idx+=1
        return self.ingredients[self.idx-1]

# RecipeBook is a wrapper for recipes held in common across the model to
# consolidate storage and to simplify calls. A simple RecipeBook.Get("Name")
# will return a fresh iterator for use in a for loop.
class RecipeBook:
    def __init__(self,**kwargs):
        self.recipes = dict()
        if "defaultReturnFunc" in kwargs.keys():
            self.defaultReturn = kwargs["defaultReturnFunc"]
        else:
            self.defaultReturn = lambda r: print("WARNING: ", r, " NOT FOUND IN RECIPE BOOK")
    def helpGet(self,Request, **kwargs):
        if Request in self.recipes.keys():
            return self.recipes[Request]
        else:
            if "ReturnFunc" in kwargs.keys():
                return kwargs["ReturnFunc"]()
            else:
                self.defaultReturn()
    def Get(self,Request, **kwargs):
        return self.helpGet(Request, **kwargs).Iterator()
    def Set(self,Name,recipe):
        self.recipes[Name]= recipe
