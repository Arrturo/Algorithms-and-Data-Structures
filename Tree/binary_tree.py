from typing import Any, Callable
import graphviz
from binarytree import tree

class BinaryNode:
    """
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    """

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self) -> str:
        return f'{self.value}'

    def is_leaf(self) -> bool:
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def add_left_child(self, value: Any) -> None:
        if self.left_child == None:
            self.left_child = value
        else:
            print('Left child already exists')
    
    def add_right_child(self, value: Any) -> None:
        if self.right_child == None:
            self.right_child = value
        else:
            print('Right child already exists')
    
    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)
    
    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)


class BinaryTree:
    """
    root: BinaryNode
    """

    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        _show = graphviz.Digraph('B', filename='BinaryTree.gv', format='png')
        _show.attr('node', shape='circle')
        _show.attr(splines='ortho')
        _show.node(f'{self.root}')
        
        node = self.root

        while node.left_child:
            _show.edge(f'{node.value}', f'{node.left_child.value}')
            if node.right_child != None:
                _show.edge(f'{node.value}', f'{node.right_child.value}')
            node = node.left_child

        node = self.root.right_child

        while node.right_child:
            if node.left_child != None:
                _show.edge(f'{node.value}', f'{node.left_child.value}')
            _show.edge(f'{node.value}', f'{node.right_child.value}')
            node = node.right_child
        _show.view()


node = BinaryNode(10)

node1 = BinaryNode(2)
node2 = BinaryNode(4)
node3 = BinaryNode(6)

node4 = BinaryNode(9)
node5 = BinaryNode(1)
node6 = BinaryNode(3)

tree = BinaryTree(node)

assert tree.root.value == 10

tree.root.add_right_child(node1)
node1.add_left_child(node2)
node1.add_right_child(node3)

tree.root.add_left_child(node4)
node4.add_left_child(node5)
node4.add_right_child(node6)


assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False

assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

print("TRAVERSE IN ORDER:")
tree.traverse_in_order(print)
print("\nTRAVERSE POST ORDER:")
tree.traverse_post_order(print)
print("\nTRAVERSE PRE ORDER:")
tree.traverse_pre_order(print)
tree.show()
