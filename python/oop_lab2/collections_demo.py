
from product import Product
from collections import deque
import array

def demo(products):
    print("=== Collections Demo ===")
    # 1) Python list (узагальнена коллекція)
    lst = list(products)  # copy
    print("\n-- List initially --")
    for p in lst:
        print(p)

    # add
    new = Product("P006", "NewWidget", "AcmeCo", 12.5, 10)
    lst.append(new)
    print("\nAdded to list:", new)

    # update 
    lst[0].increase_price(10)  # +10%
    print("\nUpdated first product (price increased by 10%):", lst[0])

    # search by code
    code_to_find = "P003"
    found = next((p for p in lst if p.code == code_to_find), None)
    print(f"\nSearch in list for code {code_to_find} ->", found)

    # remove
    removed = lst.pop()  
    print("\nRemoved last element from list:", removed)

    # iterate
    print("\nIterate list:")
    for p in lst:
        print(" -", p.code, p.name)

    # 2) deque (неузагальнена коллекція)
    dq = deque(products)
    print("\n-- Deque initially --")
    for p in dq:
        print(p)

    dq.appendleft(Product("P007", "LeftAdd", "LeftInc", 5.0, 3))
    print("\nAdded to left of deque. First now:", dq[0])

    dq.pop()
    print("\nPopped rightmost element. New rightmost:", dq[-1])

    # update middle element
    if len(dq) >= 3:
        dq[1].increase_price(-5)  
        print("\nUpdated second element in deque (5% discount):", dq[1])

    # search 
    found_dq = next((p for p in dq if p.manufacturer == "Maker3"), None)
    print("\nDeque search by manufacturer 'Maker3' ->", found_dq)

    # 3) array.array (тільки числа)
    prices = array.array('d', (p.price for p in products))
    print("\n-- Array of prices --")
    print(prices.tolist())

    # add price
    prices.append(99.99)
    print("Added price 99.99 ->", prices.tolist())

    # update price 
    prices[0] = prices[0] * 1.2
    print("Updated price[0] by +20% ->", prices.tolist())

    # search
    try:
        idx = prices.index(99.99)
        print("Found 99.99 at index", idx)
    except ValueError:
        print("99.99 not found in prices")

    print("\n=== End of Collections Demo ===")
