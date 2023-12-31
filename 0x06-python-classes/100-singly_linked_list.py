#!/usr/bin/python3
class Node:
    """
    __init__ method
    data: of Node
    next_node: None
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    '''property of data'''
    @property
    def data(self):
        return self.__data

    '''data.setter'''
    @data.setter
    def data(self, value):
        self.__data = value
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    '''property of next_node'''
    @property
    def next_node(self):
        return self.__next_node

    '''next_node setter'''
    @next_node.setter
    def next_node(self, value):
        self.__next_node = value
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a node object")


class SinglyLinkedList:
    """
    __init__ method for singlylinkedlist class
    """

    def __init__(self):
        self.head = None

    '''sorted_insert for new nodes at certain position'''
    def sorted_insert(self, value):
        newno = Node(value)

        if not self.head or value < self.head.data:
            newno.next_node = self.head
            self.head = newno
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            newno.next_node = current.next_node
            current.next_node = newno

    '''__str__ for printing list contents'''
    def __str__(self):
        result = ""
        current = self.head
        first_node = True
        while current:
            if not first_node:
                result += '\n'
            result += str(current.data)
            current = current.next_node
            first_node = False
        return result
