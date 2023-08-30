#!/usr/bin/python3

"""Define a class Node"""


class Node:
    """Represent a node of singly linked list

    Attributes:
        __data: Private instance data
        __next_node: Private instance next_node

    Args:
        data: the integer value to be stored
        next_node: the next_node instance"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """gets the data"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets the data"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @property
    def next_node(self):
        """gets the next_node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node"""

        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Defines a singly linked list

    Attributes:
        __head: Private instance head"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)"""

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next = None

        else:
            curr = self.__head
            last = None
            while curr is not None and value >= curr.data:
                last = curr
                curr = curr.next_node

            if last is not None:
                last.next_node = new_node
            else:
                self.__head = new_node

            new_node.next_node = curr

    def __str__(self):
        """makes SinglyLinkedList printable"""

        list_of_data = []
        temp = self.__head
        while temp is not None:
            list_of_data.append(str(temp.data))
            temp = temp.next_node

        return "\n".join(list_of_data)
