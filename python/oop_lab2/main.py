
from product import Product
from collections_demo import demo as collections_demo
from binary_tree import BinarySearchTree
from comparator import compare_by_price, compare_by_quantity_desc, sort_products
from iterator_demo import demo_iterator

def build_sample_products():
    return [
        Product("P001", "WidgetA", "Maker1", 10.0, 5),
        Product("P002", "GadgetB", "Maker2", 7.5, 10),
        Product("P003", "ThingC",  "Maker3", 12.0, 2),
        Product("P004", "ObjectD", "Maker2", 3.25, 20),
        Product("P005", "ItemE",   "Maker1", 15.0, 1),
    ]

def demo_collections(products):
    collections_demo(products)

def demo_binary_tree(products):
    print("\n=== Binary Tree Demo ===")
    def cmp_price(a, b):
        if a.price < b.price: return -1
        if a.price > b.price: return 1
        return 0

    tree = BinarySearchTree(cmp=cmp_price)
    for p in products:
        tree.insert(p)

    print("\nInorder traversal (should be products sorted by price ascending):")
    for p in tree:
        print(" -", p)

    search = products[2]
    found = tree.find(search)
    print(f"\nFind existing (code={search.code}) ->", found)

    not_in = Product("PX", "NotHere", "NoMaker", 999.0, 1)
    print("Find non-existing by price 999.0 ->", tree.find(not_in))

    ordered = tree.inorder_list()
    print("\nInorder_list result (list):")
    for p in ordered:
        print(" *", p.code, p.price)

    print("\nSorted by price using comparator helper:")
    sorted_by_price = sort_products(products, compare_by_price)
    for p in sorted_by_price:
        print(" >", p.code, p.price)

    print("\nSorted by quantity descending using comparator helper:")
    sorted_by_qty = sort_products(products, compare_by_quantity_desc)
    for p in sorted_by_qty:
        print(" >", p.code, p.quantity)

    from iterator_demo import demo_iterator
    demo_iterator(tree)

if __name__ == '__main__':
    products = build_sample_products()
    demo_collections(products)
    demo_binary_tree(products)
