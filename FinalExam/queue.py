class _QueueNode:

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:

    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.is_empty():
            self._qhead = node
        else:
            self._qtail.next = node

        self._qtail = node
        self._size += 1

    def dequeue(self):
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._size -= 1
        return node.item
