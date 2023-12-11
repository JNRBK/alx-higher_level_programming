#!/usr/bin/python3
"""define class Base"""
import json


class Base:
    """ class base
    Args:
    __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
        @id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the Json string representation
        of list_dictionaries
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method to write json string to a file
        Args:
        @list_objs: list of objects
        """
        if list_objs is not None:
            list_objs = [ob.to_dictionary() for ob in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='utf8') \
                as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of json
        string representation
        """
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attributes already set
        Args:
        dictionary:
        """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum
