#!/usr/bin/python3
"""
    import base class
"""
from models.base import Base

"""
    Rectangle class file
"""


class Rectangle(Base):
    """
        create a class Rectangle which inherit of the baseclass Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initiate the Rectangle
            args:
                width
                height
                x: the position
                y: the position
                id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            the getter function of the width
            return the width
        """
        return self.__width

    @width.setter
    def width(self, value_w):
        """
            the setter function of the width
        """
        if type(value_w) is not int:
            raise TypeError("width must be an integer")
        if value_w <= 0:
            raise ValueError("width must be > 0")
        self.__width = value_w

    @property
    def height(self):
        """
            the getter function of the height
            return the height
        """
        return self.__height

    @height.setter
    def height(self, value_h):
        """
            the setter function of the height
        """
        if type(value_h) is not int:
            raise TypeError("height must be an integer")
        if value_h <= 0:
            raise ValueError("height must be > 0")
        self.__height = value_h

    @property
    def x(self):
        """
            the getter function of x
            return x
        """
        return self.__x

    @x.setter
    def x(self, value_x):
        """
            the setter function of x
        """
        if type(value_x) is not int:
            raise TypeError("x must be an integer")
        if value_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value_x

    @property
    def y(self):
        """
            the getter function of y
        """
        return self.__y

    @y.setter
    def y(self, value_y):
        """
            the setter function of y
        """
        if type(value_y) is not int:
            raise TypeError("y must be an integer")
        if value_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value_y

    def area(self):
        """
            calculates the area
            return the result
        """
        return self.width * self.height

    def display(self):
        """
            displays the rectangle with #
        """
        print('\n' * self.y, end="")
        print((' ' * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """
            return the information of the rectangle
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
            assigns an argument to each attribute
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            else:
                return
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            the dictionary representation of a Rectangle
        """
        dict = {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}
        return dict
