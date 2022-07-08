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


#======ASSERTS=======

stack = Stack()

#ASSERT 1
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)

#ASSERT 2
assert len(stack) == 3

top_value = stack.pop()

#ASSERT 3
assert top_value == 1
assert len(stack) == 2

print(str(stack))
