
from binary_tree import BinarySearchTree
from product import Product

def demo_iterator(tree: BinarySearchTree):
    print("\n=== Iterator Demo (inorder traversal) ===")
    for item in tree:
        print(item)
    print("=== End Iterator Demo ===\n")
