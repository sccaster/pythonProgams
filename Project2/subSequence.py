from copy import deepcopy
from linkedList import LinkedList
from linkedList import Node

class SubSequence(LinkedList):
    """
    This class represents a SubSequence of Cards from the Deck.
    This class inherits from the LinkedList class.

    The CardSorter holds a Python list of these SubSequence objects.

    There are no instance variables for this class, except for those
    inherited from the LinkedList class.

    The class methods include 
    a. __init__: This method calls the LinkedList constructor 
                 using super()
    b. first_card: This method returns a reference to the Card at 
                   the head of the LinkedList without removing it.
    c. add_card: This method adds a Node to the front of the 
                 LinkedList containing the passed in Card.
    d. contains_card: This method searches the LinkedList for the 
                      passed in Card and returns true if Card is in 
                      this SubSequence, or False if not.               
    e. clone_subseq: This method returns a deep copy of this 
                     SubSequence. It traverses this SubSequence and 
                     adds a deepcopy of every Node at the end of the 
                     new SubSequence being returned.
    f. reverse_subseq: This method reverses this SubSequence in place.  
                       It uses three Node pointers: a current_node to 
                       walk the SubSequence, a prev_node to follow the 
                       current_node, and a next_node to grab the Node 
                       in front of current_node, as it walks the
                       LinkedList.
    g. __str__ : This method returns a string of the Cards in the 
                 SubSequence.                  
    """
    
    def __init__(self):
        """
        This method is the SubSequence constructor.  Call the
        LinkedList constructor using super()
        """
        
        super().__init__()
        
    def first_card(self):
        """
        This method returns a reference to the Card at the head 
        of the LinkedList without removing it.
        """
        
        topHead = self._head
        return topHead
        
    def add_card(self, card):
        """
        This method adds a Node to the front of the LinkedList 
        containing the passed in Card
        """

        self.add_first(card)


    def contains_card(self, card):
        """
        This method searches the LinkedList for the passed in Card 
        and returns true if Card is in this SubSequence, or False
        if not.
        """
        current = self._head
        for i in range(len(self)):
            current_card = current.data
            if card.compare(current_card) == 0:
                return True
            current = current.next
        return False
        
    def clone_subseq(self):
        """
        This method returns a deep copy of this SubSequence.  
        It traverses this SubSequence and adds a deepcopy of every 
        Node ( deepcopy is a method in the Python copy module. ).
        Add the copied Node at the END of the new SubSequence 
        being returned.
        """
        
        new_seq = SubSequence()
        current = self._head
        for n in range(len(self)):
            new_seq.add_last(deepcopy(current.data))
            current = current.next
        
        return new_seq
        
    def reverse_subseq(self):
        """
        This method reverses this SubSequence in place.  It uses 
        three Node pointers: a current_node to walk the SubSequence,
        a prev_node to follow the current_node, and a next_node to
        grab the Node in front of current_node, as it walks the
        LinkedList. 
        """

        current_node = self._head
        data_str = ""
        for d in range(len(self)):
            data_str = str(current_node.data) + ' ' + data_str + ' '
            current_node = current_node.next
        return data_str




    def __str__(self): 
        """
        This method returns a string containing the Cards
        in this SubSequence. 
        """

        data_str = ""
        current = self._head

        for d in range(len(self)):
            data_str += str(current.data) + ' '
            current = current.next

        return data_str
    
       
