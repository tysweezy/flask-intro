# import os, sys, math

class Module:
    def __init__(self, mod):
        self.mod = {} # define module dict

    def create_mod(self, title, body):
        self.title = title
        self.body = body

        if self.title or self.body == None:
            print "Must define module name"
        else:
            self.mod.update({self.title : self.body})
    
    def delete_mod(self):
        pass
   """
    def define_mod(self):
        self.mod = []
    """
class Submod(Module):
    pass
    