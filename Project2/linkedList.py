class Node():
    """
    This class represents the Node of the LinkedList.
    The instance variables are public for simplicity.
    
    The instances variables of this class include:
    1. self.data: holds the data for the Node.
    2. self.next: holds the pointer to the next Node.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 each instance variable.
    b. __str__: This method returns the data instance variable as 
                a string. 
    """
    
    def __init__(self, data):
        """
        This method is the constructor and it initializes the 
        data instance variable to the passed in parameter and
        the next instance variable to None.
        """

        self.data = data
        self.next = None

    def __str__(self):
        """
        This method returns the data instance variable as a string.
        """
        return str(self.data)
        
class LinkedList():
    """
    This class is an implementation of the Singly LinkedList ADT
    where both a head pointer and a tail pointer are used. The 
    number of Nodes in the list is kept and updated as Nodes are 
    added and removed. It uses protected instance variables, so
    that the child classes can get direct access.
    
    The instances variables of this class include:
    1. self._head: holds a pointer to the first Node.
    2. self._tail: holds a pointer to the last Node.
    3. self._size: hold the number of Nodes on the LinkedList 
    
    The class methods include: 
    a. __init__: This method is the constructor. It initializes 
                 the protected instance variables.
    b. __len__: This method returns the number of Nodes in the 
                 LinkedList.
    c. is_empty: This method returns True, if the LinkedList is 
                 empty and False, otherwise.
    d. add_first: This method creates a new Node with the passed 
                  in data and adds the Node as the first Node of 
                  the LinkedList.
    e. add_last: This method creates a new Node with the passed 
                 in data and adds the Node as the last Node of 
                 the LinkedList.
    f. remove_first: This method removes the first Node of the 
                     LinkedList and returns it.    
    g. __str__(self): This method returns the data of the 
                      LinkedList as a string
    """
    
    def __init__(self):
        """
        This method is the constructor. It initializes the protected 
        instance variables.        
        """

        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """
        This method returns the number of Nodes in the LinkedList.
        """
        
        return self._size
        
    def is_empty(self):
        """
        This method returns True, if the LinkedList is empty 
        and False, otherwise.
        """
        
        return len(self) == 0
       
    def add_first(self, data):
        """
        This method creates a new Node with the passed in data and
        adds the Node as the first Node of the LinkedList.  Both
        the head and tail pointers are updated properly and the 
        size of the LinkedList is incremented.
        """

        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

        if self.is_empty():
            self._tail = new_node
        self._size += 1
    
    def add_last(self, data):
        """
        This method creates a new Node with the passed in data and
        adds the Node as the last Node of the LinkedList.  Both
        the head and tail pointers are updated properly and the 
        size of the LinkedList is incremented. You may call
        add_first to do this wrok when the LinkedList is empty.
        """
        
        if self.is_empty():
            self.add_first(data)
        else:
            new_node = Node(data)
            self._tail.next = new_node
            self._tail = new_node
            self._size += 1
        
    def remove_first(self):
        """
        This method removes the first Node of the LinkedList and 
        returns it. Both the head and tail pointers are updated 
        properly and the size of the LinkedList is decremented. 
        If the LinkedList is empty, None is returned.
        """
        
        if self.is_empty():
            return None

        current = self._head
        self._head = current.next
        self._size -= 1

        if self.is_empty():
            self._tail = None

        return current.data
        
    def __str__(self):
        """
        This method returns the data of the LinkedList as a string,
        with each Node's data on a separate line starting with the 
        head of the LinkedList.
        """

        data_str = ""
        current = self._head

        for d in range(len(self)):
            data_str += str(current.data) + '\n'
            current = current.next

        return data_str