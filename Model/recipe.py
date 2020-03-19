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

