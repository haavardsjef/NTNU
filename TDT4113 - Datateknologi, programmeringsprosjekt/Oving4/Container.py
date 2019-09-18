"""Container class by Håvard Hjelmeseth for TDT4113"""

class Container():
    """Superclass"""

    def __init__(self):
        self._items = []

    def size(self):
        """Return size of items"""
        return len(self._items)

    def is_empty(self):
        """Returns true if items is empty, false otherwise"""
        return len(self._items) == 0

    def push(self, item):
        """Adds item to end of items"""
        self._items.append(item)

    def pop(self):
        """Removes the relevant item from items, and returns it"""
        raise NotImplementedError

    def peek(self):
        """Returns the relevant item from items"""
        raise NotImplementedError


class Queue(Container):
    """Subclass of container"""

    def __init__(self):
        Container.__init__(self)

    def pop(self):
        assert not self.is_empty()
        return self._items.pop(0)

    def peek(self):
        assert not self.is_empty()
        return self._items[0]

class Stack(Container):
    """Subclass of container"""

    def __init__(self):
        Container.__init__(self)

    def pop(self):
        assert not self.is_empty()
        return self._items.pop()

    def peek(self):
        assert not self.is_empty()
        return self._items[-1]
