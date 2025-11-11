
from functools import cmp_to_key
from typing import Callable
from product import Product

def compare_by_price(a: Product, b: Product) -> int:
    # ascending by price
    if a.price < b.price:
        return -1
    if a.price > b.price:
        return 1
    return 0

def compare_by_quantity_desc(a: Product, b: Product) -> int:
    # descending by quantity
    if a.quantity > b.quantity:
        return -1
    if a.quantity < b.quantity:
        return 1
    return 0

def sort_products(products, cmp):
    key = cmp_to_key(cmp)
    return sorted(products, key=key)
