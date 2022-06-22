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
        self.tail.next = node
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
        self.head = node.next
        return node.value

    def remove_last(self):
        node = self.head
        while (node.next.next):
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

    # def remove(self, after: Node) -> Any:
    #     node = self.head
    #     while node != after:
    #         node = node.next
    #     removed = node.next
    #     node.next = None
    #     return removed.value

    def __str__(self) -> str:
        node = self.head
        node_value = f'{node.value}'
        while (node.next):  # (node.next != None)
            node = node.next
            node_value =  node_value + ' -> ' + f'{node.value}'
        return node_value

    def __len__(self) -> int:
        node = self.head
        sum = 0 
        if self.head == None:
            return 0
        while node != None:
            node = node.next
            sum += 1
        return sum

#======ASSERTS=======
list_ = LinkedList()

#ASSERT 1
assert list_.head == None

#ASSERT 2
list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

#ASSERT 3
list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

#ASSERT 4
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

#ASSERT 5
first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element
assert str(list_) == '1 -> 5 -> 9 -> 10'

#ASSERT 6
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

#ASSERT 7
second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

#ASSERT 8
assert len(list_) == 2
