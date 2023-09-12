#!/usr/bin/python3

"""Define a class Student"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if type(attrs) is list:
            my_dict = {}
            for ele in attrs:
                if type(ele) is str:
                    for key in self.__dict__.keys():
                        if key == ele:
                            my_dict[key] = self.__dict__[key]
            return my_dict

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for key in json.keys():
            if key == 'first_name':
                self.first_name = json[key]
            elif key == 'last_name':
                self.last_name = json[key]
            elif key == 'age':
                self.age = json[key]
