from typing import Any, Callable, List

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