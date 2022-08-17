import tree
import binary_tree
# import binary_search_tree

#TREE

# TreeNode

node3 = tree.TreeNode(4)
node4 = tree.TreeNode(9)
node5 = tree.TreeNode(8)
node6 = tree.TreeNode(2)
node1 = tree.TreeNode(3, [node3, node4])
node2 = tree.TreeNode(0, [node5])
tree_node = tree.TreeNode(1, [node1, node2])
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
tree = tree.Tree(tree_node)
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


# BINARY TREE
node = binary_tree.BinaryNode(10)

node1 = binary_tree.BinaryNode(2)
node2 = binary_tree.BinaryNode(4)
node3 = binary_tree.BinaryNode(6)

node4 = binary_tree.BinaryNode(9)
node5 = binary_tree.BinaryNode(1)
node6 = binary_tree.BinaryNode(3)

tree = binary_tree.BinaryTree(node)

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