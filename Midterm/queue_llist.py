class _QueueNode:
    """
    This class represents the Node of a Queue implemented as a 
    LinkedList.
    
    The instances variables of this class include:
    1. self.item: holds the item for the Queue Node.
    2. self.next: holds the pointer to the next Node.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 each instance variable to the passed in parameters.
    """
    
    def __init__(self, item):
        """
        This method is the constructor and it initializes each
        nstance variable to the passed in parameters.
        """
        self.item = item
        self.next = None
    
class Queue:
    """
    This Queue class is a singly LinkedList implementation of a Queue.
    
    The instances variables of this class include:
    1. self._qhead: holds the pointer to the first Node of the Queue
    2. self._qhead: holds the pointer to the last Node of the Queue
    3. self._size: holds the number of Nodes on the Queue.
    
    The class methods include: 
    a. __init__: This method is the constructor and it initializes 
                 the Queue instance variables.
    b. is_empty: This method returns True, if the Queue is empty or 
                 False otherwise.
    c. __len__: This method returns the number of items in the Queue.
    d. enqueue: This method adds the given item to the Queue.
    e. dequeue: This method removes and returns the first item in 
                the Queue.
    """
    def __init__(self):
        """
        This method is the constructor and it initializes the Queue 
        instance variables.
        """
        self._qhead = None
        self._qtail = None
        self._size = 0

    def is_empty(self):
        """
        This method returns True if the Queue is empty 
        or False otherwise.
        """
        return self._size == 0

    def __len__(self):
        """
        This method returns the number of items in the Queue
        """
        return self._size

    def enqueue(self, item):
        """
        This method adds the given item to the Queue.
        """
        node = _QueueNode(item)
        if self.is_empty():
            self._qhead = node
        else:
            self._qtail.next = node
        
        self._qtail = node
        self._size += 1
    
    def dequeue(self):
        """
        This method removes and returns the first item in the Queue.
        """
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._size -= 1
        return node.item


