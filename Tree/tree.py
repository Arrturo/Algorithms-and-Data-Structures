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
            # returns error
            # if child.value == value:
            #     return True
            # child.search(value)
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
        _show = graphviz.Graph('G', filename='Tree.gv', format='png')
        _show.node(f'{self.root}')
        que = queue.Queue()
        que.put(self.root)
        while que.empty() == False:
            element = que.get()
            for child in element.children:
                que.put(child)
                _show.edge(f'{element}', f'{child}')
        _show.view()

# TreeNode

node3 = TreeNode(4)
node4 = TreeNode(9)
node5 = TreeNode(8)
node6 = TreeNode(2)
node1 = TreeNode(3, [node3, node4])
node2 = TreeNode(0, [node5])
tree_node = TreeNode(1, [node1, node2])
tree_node.add(node6)

assert node1.is_leaf() == False
assert node5.is_leaf() == True

print("\nFOR EACH DEEP FIRST:")
tree_node.for_each_deep_first(print)
print("\nFOR EACH LEVEL ORDER:")
tree_node.for_each_level_order(print)
print()
assert tree_node.search(4) == True
assert tree_node.search(5) == False

## Tree

print()
tree = Tree(tree_node)
tree.add(10, 0)
tree.add(3.5, 8)
tree.add(12, 4)
tree.add(15, 1)
tree.add(23, 12)
print("\nFOR EACH DEEP FIRST:")
tree.for_each_deep_first(print)
print("\nFOR EACH LEVEL ORDER:")
tree.for_each_level_order(print)
tree.show()
