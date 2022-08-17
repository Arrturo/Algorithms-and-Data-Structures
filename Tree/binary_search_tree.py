from typing import Any, List

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None
    
        def __repr__(self) -> str:
            return f'{self.value}'

    def min(self):
        if self.left_child != None:
            self.left_child.min()
        return self


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root
    
    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child == None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(node.left_child, value)
        else:
            if node.right_child == None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(node.right_child, value)
        return node

    def insertlist(self, list: List[Any]) -> None:
        for element in list:
            self.insert(element)

    def contains(self, value: Any) -> bool:
        pass

    def remove(self, value: Any) -> None:
        pass

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        pass

    def show(self):
        pass
