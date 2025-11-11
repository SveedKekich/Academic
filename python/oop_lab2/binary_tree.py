
from typing import Generic, TypeVar, Optional, Callable, Iterator, Any, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None

class BinarySearchTree(Generic[T]):
    
    def __init__(self, cmp: Optional[Callable[[T, T], int]] = None):
        self.root: Optional[Node[T]] = None
        self._cmp = cmp

    def _compare(self, a: T, b: T) -> int:
        if self._cmp is not None:
            return self._cmp(a, b)
        if a == b:
            return 0
        if a < b:
            return -1
        return 1

    def insert(self, value: T) -> None:
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            c = self._compare(value, cur.value)
            if c == 0:
                # replace
                cur.value = value
                return
            elif c < 0:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right

    def find(self, value: T) -> Optional[T]:
        cur = self.root
        while cur is not None:
            c = self._compare(value, cur.value)
            if c == 0:
                return cur.value
            elif c < 0:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def _inorder(self, node: Optional[Node[T]], out: List[T]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.value)
        self._inorder(node.right, out)

    def inorder_list(self) -> List[T]:
        out: List[T] = []
        self._inorder(self.root, out)
        return out

    def __iter__(self) -> Iterator[T]:
        return InorderIterator(self.root)

class InorderIterator(Generic[T]):
    def __init__(self, root: Optional[Node[T]]):
        self.stack: List[Node[T]] = []
        self._push_left(root)

    def _push_left(self, node: Optional[Node[T]]):
        while node is not None:
            self.stack.append(node)
            node = node.left

    def __iter__(self):
        return self

    def __next__(self) -> T:
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        value = node.value
        if node.right is not None:
            self._push_left(node.right)
        return value
