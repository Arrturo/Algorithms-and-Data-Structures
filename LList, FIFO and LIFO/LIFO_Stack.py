from linked_list import *

class Stack:
    """
        _storage: LinkedList
    """

    def __str__(self) -> str:
        node = self._storage.head
        text = ""
        while (node):
            str_val = str(node.value)
            text += (str_val + "\n")
            node = node.next
        return text

    def __len__(self) -> int:
        return len(self._storage)

    def __init__(self):
        self._storage = LinkedList()
    
    def push(self, element: Any) -> None:
        self._storage.push(element)
    
    def pop(self) -> None:
        return self._storage.pop()