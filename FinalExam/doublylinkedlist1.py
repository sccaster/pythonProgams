class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_nodeA(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def add_nodeB(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif data < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif data > self.tail.data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            next_node = self.head
            prev_node = self.head
            while (next_node.next is not None
                   and next_node.data < data):
                prev_node = next_node
                next_node = next_node.next
            new_node.next = next_node
            prev_node.next = new_node
            new_node.prev = prev_node
            next_node.prev = new_node

    def add_nodeC(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def method1(self):
        temp_node = None
        current_node = self.head
        self.tail = current_node
        while current_node is not None:
            temp_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp_node
            current_node = current_node.prev
        if temp_node is not None:
            self.head = temp_node.prev

    def method2(self, head_node):
        if head_node is None:
            return
        self.method2(head_node.next)
        print(head_node.data)

    def print_nodesX(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            if current_node.next is not None:
                current_node = current_node.next
            else:
                current_node = None


    def print_nodes(self):
        if self.tail is None:
            return "List is empty"
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev