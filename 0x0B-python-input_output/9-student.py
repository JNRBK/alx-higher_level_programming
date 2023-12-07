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

    def to_json(self):
        """
        public method that retreives a dictionary
        representation of a Student instance
        """
        return self.__dict__
