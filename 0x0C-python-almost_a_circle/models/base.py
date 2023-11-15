#!/usr/bin/python3

'''module for class base'''
class Base:
    '''class atribute'''
    __nb_objects = 0

    '''initialize constructor'''
    def __init__(self, id = None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

