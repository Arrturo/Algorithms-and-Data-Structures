from linked_list import *

class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()
    
    def peek(self) -> Any:
        return self._storage.head.value
    
    def enqueue(self, element: Any) -> None:
        self._storage.append(element)
    
    def dequeue(self) -> Any:
        return self._storage.pop()
    
    def __str__(self) -> str:
        node = self._storage.head
        node_value = f'{node.value}'
        while (node.next):  # (node.next != None)
            node = node.next
            node_value = node_value + ', ' + f'{node.value}'
        return node_value

    def __len__(self) -> int:
        return len(self._storage)

#======ASSERTS=======

queue = Queue()

#ASSERT 1
assert len(queue) == 0

#ASSERT 2
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

#ASSERT 3
client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
