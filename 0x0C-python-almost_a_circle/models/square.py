#!/usr/bin/python3

"""Module contain a class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a class Square that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns Square info"""

        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return f"[Square] ({id}) {x}/{y} - {size}"

    @property
    def size(self):
        """Gets the size value"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square info"""

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        elif kwargs:
            for key in kwargs.keys():
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square info"""

        squ_dict = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
        return squ_dict
