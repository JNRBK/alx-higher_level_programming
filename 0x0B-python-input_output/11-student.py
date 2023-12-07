#!/usr/bin/python3
"""
Class Student that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        public instance attributes
        Args:
        @first_name: first name
        @last_name: last name
        @age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        public method that retreives a dictionary
        representation of a Student instance ----
        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if (type(attrs) is list and
                all(type(idx) is str for idx in attrs)):
            dic = {}
            for i in attrs:
                if hasattr(self, i):
                    dic[i] = getattr(self, i)
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes """
        for key, value in json.items():
            setattr(self, key, value)
