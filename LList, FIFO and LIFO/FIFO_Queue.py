from linked_list import *

class Queue:
    """
        _storage: LinkedList
    """
    def __init__(self):
        self._storage = LinkedList()
    
    def __str__(self) -> str:
        node = self._storage.head
        node_value = f'{node.value}'
        while (node.next):  # (node.next != None)
            node = node.next
            node_value = node_value + ', ' + f'{node.value}'
        return node_value

    def __len__(self) -> int:
        return len(self._storage)

    def peek(self) -> Any:
        return self._storage.head.value
    
    def enqueue(self, element: Any) -> None:
        self._storage.append(element)
    
    def dequeue(self) -> Any:
        return self._storage.pop()
    
    def is_empty(self) -> bool:
        # if self._storage.head == None:
        #     return True
        # return False
        return len(self._storage) == 0
    
    def is_empty(self) -> bool:
        # if self._storage.head == None:
        #     return True
        # return False
        return len(self._storage) == 0

#======ASSERTS=======

queue = Queue()

#ASSERT 1
assert len(queue) == 0

#ASSERT 2
queue.enqueue('client1')
queue.enqueue('client2')
queue.enqueue('client3')

assert str(queue) == 'client1, client2, client3'

#ASSERT 3
client_first = queue.dequeue()

assert client_first == 'client1'
assert str(queue) == 'client2, client3'
assert len(queue) == 2

assert queue.is_empty() == False
