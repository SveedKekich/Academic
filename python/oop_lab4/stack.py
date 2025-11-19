from stack_event_args import StackOverflowEventArgs


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self._items = []
        self.on_overflow = []   

    def push(self, value):
        if len(self._items) >= self.capacity:
            self._raise_overflow(value)
        else:
            self._items.append(value)

    def pop(self):
        if self._items:
            return self._items.pop()
        return None

    def _raise_overflow(self, value):
        event_args = StackOverflowEventArgs(value, self.capacity)
        for handler in self.on_overflow:
            handler(self, event_args)

    def subscribe(self, handler):
        self.on_overflow.append(handler)
