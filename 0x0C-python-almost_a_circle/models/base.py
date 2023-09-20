#!/usr/bin/python3

"""
Module contain ``Base`` Class
"""

import json
import csv
import turtle


class Base:
    """
    Define the base class of other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of ``list_dictionaries``"""

        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if list_objs is not None:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
        else:
            list_dicts = None

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation ``json_string``"""

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if dictionary is not None and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + '.json'
        try:
            with open(filename, 'r') as f:
                list_dicts = Base.from_json_string(f.read())

            list_insts = []
            for d in list_dicts:
                list_insts.append(cls.create(**d))

            return list_insts
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save class info to csv file"""

        filename = cls.__name__ + '.csv'

        if list_objs is not None and list_objs != []:
            list_dicts = []

            for obj in list_objs:
                dict_obj = obj.to_dictionary()
                list_dicts.append(dict_obj)

            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            else:
                fields = ['id', 'size', 'x', 'y']

            with open(filename, 'w', newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_dicts)
        else:
            with open(filename, 'w', newline='') as csvfile:
                csvfile.write('[]')

    @classmethod
    def load_from_file_csv(cls):
        """load class info from csv file"""

        filename = cls.__name__ + '.csv'
        if cls.__name__ == 'Rectangle':
            fields = ['id', 'width', 'height', 'x', 'y']
        else:
            fields = ['id', 'size', 'x', 'y']
        try:
            with open(filename, 'r', newline='') as csvfile:
                list_dicts1 = csv.DictReader(csvfile, fieldnames=fields)
                list_dicts2 = []
                list_insts = []
                list_dicts1.__next__()
                for d in list_dicts1:
                    dic = {}
                    for key, value in d.items():
                        dic[key] = int(value)
                    list_dicts2.append(dic)

                for d in list_dicts2:
                    list_insts.append(cls.create(**d))

                return list_insts
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""

        pen = turtle.Turtle()
        pen.pensize(2)
        pen.hideturtle()
        screen = turtle.Screen()
        screen.bgcolor("black")

        if list_rectangles is not None and list_rectangles != []:
            pen.color("red")
            pen.fillcolor("red")
            for rect in list_rectangles:
                pen.up()
                pen.goto(rect.x, rect.y)
                pen.down()
                for i in range(2):
                    pen.forward(rect.width)
                    pen.left(90)
                    pen.forward(rect.height)
                    pen.left(90)

        if list_squares is not None and list_squares != []:
            pen.color("blue")
            for sq in list_squares:
                pen.up()
                pen.goto(sq.x, sq.y)
                pen.down()
                for j in range(4):
                    pen.forward(sq.width)
                    pen.left(90)

        screen.mainloop()
