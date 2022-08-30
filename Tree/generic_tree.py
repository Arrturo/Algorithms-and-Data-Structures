from typing import Any, Callable, List, Union
import queue
import graphviz

class TreeNode:
    '''
    value: Any
    children: List['TreeNode']
    '''

    def __init__(self, value: Any, children: List['TreeNode'] = []):
        self.value = value
        self.children = children.copy()

    def __repr__(self) -> str:
        return f'{self.value}'

    def is_leaf(self) -> bool:
        if self.children == []:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        if self.children != []:
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        que = queue.Queue()
        for child in self.children:
            que.put(child)
        # que.put(self)
        while que.empty() == False:
            element = que.get()
            visit(element)
            for child in element.children:
                que.put(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return True
        for child in self.children:
            if child.search(value):
                return True
        return False


class Tree:
    """
    root: TreeNode
    """

    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, value: Any, parent_value: Any) -> None:
        if self.root.search(parent_value):
            node = TreeNode(value)
            que = queue.Queue()
            que.put(self.root)
            while que.empty() == False:
                element = que.get()
                if element.value == parent_value:
                    element.add(node)
                    break  
                for child in element.children:
                    que.put(child)
        else:
            print("parent_value does not exist")

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)
    
    def show(self):
        _show = graphviz.Digraph('G', filename='Tree.gv', format='png')
        _show.attr('node', shape='circle', fixedsize='true')
        _show.node(f'{self.root}')

        def childrens(node: TreeNode) -> None:
            for child in node.children:
                _show.edge(f'{node.value}', f'{child}') 

        self.for_each_level_order(childrens)
        _show.view()