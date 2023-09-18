#!/usr/bin/python3

"""
Module contain ``Base`` Class
"""

import json


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
                dummy = cls(1, 1, 1, 1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1, 1, 1, 1)

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
