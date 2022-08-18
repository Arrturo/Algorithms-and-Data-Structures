from typing import Any, Callable
import graphviz

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

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self):
        _show = graphviz.Digraph('B', filename='BinaryTree.gv', format='png')
        _show.attr('node', shape='circle')
        _show.attr(splines='ortho')
        _show.node(f'{self.root}')
        
        # while node.left_child:
        #     _show.edge(f'{node.value}', f'{node.left_child.value}')
        #     if node.right_child != None:
        #         _show.edge(f'{node.value}', f'{node.right_child.value}')
        #     node = node.left_child

        # node = self.root.right_child

        # while node.right_child:
        #     if node.left_child != None:
        #         _show.edge(f'{node.value}', f'{node.left_child.value}')
        #     _show.edge(f'{node.value}', f'{node.right_child.value}')
        #     node = node.right_child
        # _show.view()

        def childrens(node: BinaryNode) -> None:
            if node.left_child:
                _show.edge(f'{node.value}', f'{node.left_child.value}')
            if node.right_child:
                _show.edge(f'{node.value}', f'{node.right_child.value}')
        
        self.traverse_pre_order(childrens)
        _show.view()
