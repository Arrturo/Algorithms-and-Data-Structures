import random
from typing import Any, List
import graphviz

class Node:
    # value: Any
    # next: 'Node'

    def __init__(self, value=Any, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # head: Node

    def __init__(self, head=None):
        self.head = head

    def __str__(self) -> str:
        node = self.head
        node_value = f'{node.value}'
        while (node.next):  # (node.next != None)
            node = node.next
            node_value = node_value + ' -> ' + f'{node.value}'
        return node_value

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self) -> int:
        node = self.head
        sum = 0
        if self.head == None:
            return 0
        while node != None:
            node = node.next
            sum += 1
        return sum
        # return len(list(iter(self)))

    def push(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node
    
    def append(self, value: Any) -> None:
        node = Node(value)
        head = self.head

        while head.next:
            head = head.next
        head.next = node
        head.next.next = None

    def appendList(self, list: List[Any]) -> None:
        for i in list:
            self.append(i)
    
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
        self.head = node.next
        return node.value

    def remove_last(self):
        node = self.head
        if self.head == None:
            return None
        if self.head == None:
            return None
        while node.next.next:
            node = node.next
        last = node.next
        node.next = None
        return last.value

    def remove(self, after: Node) -> Any:
        if after.next.next == None:
            removed = after.next
            after.next = None
            return removed.value
        removed = after.next
        after.next = after.next.next
        after.next.next = None
        return removed.value

    def show(self):
        _show = graphviz.Digraph('LL', filename='LinkedList', format='png')
        _show.attr(rankdir="LR")
        _show.attr('node', shape='box')
        _show.attr(arrowhead='vee')

        node = self.head
        while node.next:
            _show.edge(f'{node.value}', f'{node.next.value}')
            node = node.next
        _show.render(f'output/LL{random.random()}', view=True, format="png", quiet_view=False)
