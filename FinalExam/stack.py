class Stack():
    """
    This Stack class is the Python list implementation of a Stack.

    The instances variables of this class include:
    1. self._items: the Python list that holds the data for the Stack.

    The class methods include:
    a. __init__: This method creates the Python list instance variable.
    b. is_empty: This method returns True, if the Stack is empty or
                 False otherwise.
    c. __len__: This method returns the number of items in the Stack.
    d, peek:
    e. pop:
    f. push:
    """


    def __init__(self):
        """
        This method creates the Python list instance variable.
        """
        self._items = list()


    def is_empty(self):
        """
        This method returns True, if the Stack is empty or False
        otherwise.
        """
        return len(self) == 0


    def __len__(self):
        """
        This method returns the number of items in the Stack.
        """
        return len(self._items)


    def peek(self):
        """
        This method returns the top item on the Stack
        without removing it.
        """
        return self._items[-1]


    def pop(self):
        """
        This method removes and returns the top item on the Stack.
        """
        return self._items.pop()


    def push(self, item):
        """
        This method pushes an item onto the top of the Stack.
        """
        self._items.append(item)