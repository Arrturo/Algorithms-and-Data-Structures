from typing import Any, Callable, List, Union
import queue

class TreeNode:
    '''
    value: Any
    children: List['TreeNode']
    '''

    def __init__(self, value: Any, children: List['TreeNode'] = []):
        self.value = value
        self.children = children

    def __str__(self) -> str:
        return f'{self.value}'

    def is_leaf(self) -> bool:
        if self.children is None:
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
        #que.put(self)
        while que.empty() == False:
            element = que.get()
            visit(element)
            for child in element.children:
                que.put(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if value == self.value:
            return True
        for child in self.children:
            if value == child.value:
                return True
            child.search(value)
        return False

class Tree:
    """
    root: TreeNode
    """

    def __init__(self, root: TreeNode):
        self.root = root
