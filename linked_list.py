from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head

    def push(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node

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

