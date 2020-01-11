from comparable import Comparable

class TreeNode(Comparable):
    """
    This class represents a binary tree node in the BST class.
    where the node data is a Comparable object
    The public instance variables are:
       - element: a Comparable object
       - left: the root node of the left subtree off this node
       - right: the root node of the right subtree off this node
    """
    def __init__(self, element):
        """
        Constructor: 
        Initialize the data element with the passed in parameter.
        Initialize the node pointers to None.
        """
        
        self.element = element
        self.left = None
        self.right = None


    def compare(self, other_node):
        """
        Compare nodes by comparing the elements.
        """
        
        return self.element.compare(other_node.element)

    
    def __str__(self):
        """
        Return the string representation of the HuffElement
        """
    
        return str(self.element)

        
class BST:
    """
    This class represents a binary search tree.
    """

    def __init__(self, list_of_objects = None, bst = None):
        """
        Constructor:
        The constructor parameters have a default values.
        This allows a BST to be created one of three ways:
        1. empty: BST()
        2. from a list: BST(list_of_objects = a_list)
        3. from a BST tree: BST(bst = a_bst)
        """
        
        self.root = None
        self.size = 0
        
        # Create BST from a list of objects
        if list_of_objects is not None:
            for elem in list_of_objects:
                self.insert(elem)
        
        # Create BST from another BST
        if bst is not None:
            self.root = bst

    def __len__(self):
        """
        Return the number of nodes in this tree using len function
        """
        
        return self.size
        
   
    def get_root(self):
        """
        Return the root TreeNode
        """
        
        return self.root
	
    
    def clear(self):
        """
        Remove all nodes from the tree
        """
	
        self.root = None
        self.size = 0

	
    def search(self, element):
        """
        The recursive search helper function.
        Start the recursive search for the element at the root node
        """

        return self.search_rec(self.root, element)


    def search_rec(self, current, element):
        """
        Recursively finds the element in the BST,
        starting with the current node
        Returning True when found and False, otherwise
        """

        found = False
        if current is not None:

            comp = element.compare(current.element)

            if comp < 0:
                found = self.search_rec(current.left, element)
            elif comp > 0:
                found = self.search_rec(current.right, element)
            else:
                found = True

        return found


    def insert(self, element):
        """
        The recursive insert helper function.
        Start the recursive search for the insertion place 
        at the root node, where the parent node is None
        Return true if the element is inserted successfully, 
        and False, otherwise
        """
        
        return self.insert_rec(None, self.root, element)

	
    def insert_rec(self, parent, current, element):
        """
        Recursively finds the insertion position in the BST, 
        starting with the current node
        Return true if the element is inserted successfully, 
        and False, otherwise
        """	    
		
        if self.root is None:
            self.root = TreeNode(element)
            self.size += 1
            return True
            
        if current is None:
            if element.compare(parent.element) < 0:
                parent.left = TreeNode(element)
            else:
                parent.right = TreeNode(element)
            self.size += 1
            return True
		
        comp = element.compare(current.element)
        
        if comp < 0:
            self.insert_rec(current, current.left, element)
        elif comp > 0:
            self.insert_rec(current, current.right, element)
        else:
            return False
		
        return True


    def delete(self, element):
        """
        The recursive delete helper function.
        Start the recursive search for the node to delete
        at the root node, where the parent node is None
        Return true if the element is deleted successfully, 
        and False, otherwise
        """
		
        removed = self.remove(None, self.root, element)
        if removed:
            self.size -= 1
		
        return removed
        

    def remove(self, parent, tree, element):
        """
        Recursively finds the node to delete 
        starting with the tree node
        Return true if the element is deleted successfully, 
        and False, otherwise
        """	    

        found = False
        if tree is None:
            return False

        comp = element.compare(tree.element)

        if comp < 0:
            found = self.remove(tree, tree.left, element)
        elif comp > 0:
            found = self.remove(tree, tree.right, element)
        else:
            self.delete_node(parent, tree)
            found = True
		
        return found
        

    def delete_node(self, parent, tree):
        """
        Deletes the node pointed to by tree.
	    The user's data in the node pointed to by tree will no
	    longer be in the tree.  If tree is a leaf node or has
        only one child pointer that is not None, the node pointed 
        to by tree is deleted; otherwise, the user's data is 
        replaced by its logical predecessor (rightmost node) 
        and that is deleted.
        """
        
        # Case 1: tree.left is None
        if tree.left is None:
            if tree == self.root:
                self.root = tree.right
            elif tree.element.compare(parent.element) < 0:
                parent.left = tree.right
            else:
                parent.right = tree.right
		
        # Case 2: Get element from the right-most node in tree
        else:
            parent_of_right_most = tree
            right_most = tree.left

            # Keep going to the right to find
            # right most node in left subtree

            while right_most.right is not None:
                parent_of_right_most = right_most
                right_most = right_most.right

            # Replace the element in tree
            # with the element in right_most

            tree.element = right_most.element

            if parent_of_right_most.right == right_most:
                parent_of_right_most.right = right_most.left
            else:
                parent_of_right_most.left = right_most.left

   
    def inorder(self):
        """
        The recursive inorder traversal helper function.
        Start the traversal at the root
        """
	
        self.inorder_rec(self.root)


    def inorder_rec(self, sub_root):
        """
        Recursively traverse the BST in order, 
        starting with the sub_root node
        """	    
		
        if sub_root is None:
            return

        self.inorder_rec(sub_root.left)

        print(str(sub_root.element) + " ")

        self.inorder_rec(sub_root.right)


    def postorder(self):
        """
        The recursive postorder traversal helper function.
        Start the traversal at the root
        """
	
        self.postorder_rec(self.root)

	
    def postorder_rec(self, sub_root):
        """
        Recursively traverse the BST post order, 
        starting with the sub_root node
        """	    
        if sub_root is None:
            return

        self.postorder_rec(sub_root.left)

        self.postorder_rec(sub_root.right)

        print(str(sub_root.element) + " ")

	
    def preorder(self):
        """
        The recursive preorder traversal helper function.
        Start the traversal at the root
        """
	
        self.preorder_rec(self.root)
	

    def preorder_rec(self, sub_root):
        """
        Recursively traverse the BST pre order, 
        starting with the sub_root node
        """ 
                
        if sub_root is None:
            return

        print(str(sub_root.element) + " ")

        self.preorder_rec(sub_root.left)

        self.preorder_rec(sub_root.right)


    def path(self, element):
        """
	    Returns a path from the root leading to the passed element
        """
	
        path_list = []
        current = self.root

        while current is not None:
            path_list.append(current)
            comp = element.compare(current.element)
            if comp < 0:
                current = current.left
            elif comp > 0:
                current = current.right
            else:
                break

        return path_list
	
    
    def __iter__(self):
        """
        Returns an iterator for traversing this BST in order
        """
        
        return BSTIterator(self.root)


class BSTIterator:
    """
    An iterator for a BST
    """
    
    def __init__(self, root):
        """
        Initialize an empty list
        Set the current item to index 0
        """
        
        self.bst_nodes = []
        self.cur_node = 0
        self.root = root
        
        self.inorder()


    def __iter__(self):
        """
        Return this iterator
        """
        
        return self


    def __next__(self):
        """
        Walk the Python list to return the next node in the tree
        """
        
        if self.cur_node < len(self.bst_nodes):
            node = self.bst_nodes[self.cur_node]
            self.cur_node += 1
            return node
        else:
            raise StopIteration


    def inorder(self):
        """
        The recursive inorder traversal helper function.
        Start the traversal at the root
        """
        
        self.inorder_rec(self.root)
	
    
    def inorder_rec(self, sub_root):
        """
        Recursively traverse the BST in order, 
        starting with the sub_root node
        """	    
		
        if sub_root is None:
            return

        self.inorder_rec(sub_root.left)
        self.bst_nodes.append(sub_root.element)

        self.inorder_rec(sub_root.right)
