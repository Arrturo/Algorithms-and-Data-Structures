from typing import Any, List
import graphviz

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

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False


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
        node = self.root

        while node is not None:
            if node.value == value:
                return True
            if value < node.value:
                node = node.left_child
            else:
                node = node.right_child
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.is_leaf():
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            node = node.right_child.min()
            node.right_child = self._remove(node.right_child, value)
        if value < node.value:
            node.left_child = self._remove(node.left_child, value)
        if value > node.value:
            node.left_child = self._remove(node.right_child, value)
        return node

    def show(self):
        _show = graphviz.Digraph('BST', filename='BinarySearchTree.gv', format='png')
        _show.attr('node', shape='circle')
        _show.attr(splines='ortho')
        _show.node(f'{self.root}')

        def childrens(node: BinaryNode) -> None:
            if node.left_child:
                _show.edge(f'{node.value}', f'{node.left_child.value}')
            if node.right_child:
                _show.edge(f'{node.value}', f'{node.right_child.value}')

        self.traverse_pre_order(childrens)
        _show.view()
