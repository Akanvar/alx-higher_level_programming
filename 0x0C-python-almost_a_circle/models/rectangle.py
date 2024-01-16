#!/usr/bin/python3
"""Creates a subclass of Base superclass """

from models.base import Base

class Rectangle(Base):
    """Sub-class of the Base super class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing a constructer for Rectangle class
        """
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.setter_validation("width", value)
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.setter_validation("height", value)
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.setter_validation("x", value)
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.setter_validation("y", value)
            selx.__y = value


