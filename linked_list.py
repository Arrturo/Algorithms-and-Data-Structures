from typing import Any

class Node:
    # value: Any
    # next: 'Node'

    def __init__(self, value=Any, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # head: Node
    # tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node
        if self.tail is None:
            self.head = node
            self.tail = node

    def append(self, value: Any) -> None:
        node = Node(value)
        if (self.tail == None):
            self.tail = node
            self.head = node
        self.tail = node

    def node(self, at: int) -> Node:
        counter = 0
        node = self.head

        while (counter != at):
            node = node.next
            counter += 1
            if (node.next == None):
                return node
        return node

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self) -> Any:
        node = self.head
        self.head = None 
        return node

    def remove_last(self) -> Any:
        node = self.tail
        self.tail = None
        return node
    
    def remove(self, after: Node) -> Any:
        after.next = after.next.next
        after.next.next = None
        after.next.value = None

    def print(self) -> str:
        node = self.head
        head = f'{node.value}'
        while (node.next != None):
            node = node.next
            return head + '->' + f'{node.value}'
        return head
