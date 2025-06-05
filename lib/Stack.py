# Stack.py

class Stack:
    def __init__(self, items=None, max_size=None):
        self.items = items if items is not None else []
        self.max_size = max_size

    def push(self, item):
        if self.full():
            return  # or raise an exception
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def full(self):
        return self.max_size is not None and self.size() >= self.max_size

    def search(self, target):
        # return the distance from the top of the stack (0-based)
        if target in self.items:
            return self.size() - 1 - self.items.index(target)
        return -1
