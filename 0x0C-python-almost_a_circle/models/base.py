#!/usr/bin/python3
"""Defines a Base class """

class Base:
    """Body of `Base` class
    """
   
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a class constructor
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
