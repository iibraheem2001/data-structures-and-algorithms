import pytest
from binary_tree import BinaryTree, Node
from tree_breadth_first.tree_breadth_first import breadth_first


# @pytest.mark.skip("TODO")
def test_exists():
    assert breadth_first


# @pytest.mark.skip("TODO")
def test_rootless_tree():
    tree = BinaryTree()
    expected = []
    actual = breadth_first(tree)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_node():
    tree = BinaryTree()
    tree.root = Node
    expected = []
    actual = breadth_first(tree)
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_two_nodes():
    tree = BinaryTree()
    tree.root = Node
    tree.root.right = Node
    expected = []
    actual = breadth_first(tree)
    assert actual == expected
