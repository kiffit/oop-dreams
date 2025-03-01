# Thomas Safago
# 02/28/2025


class Node:
    # Attributes
    __parent = None
    __children = None

    # Constructors
    def __init__(self):
        self.set_parent(None)
        self.set_children([])

    # Methods
    def add_child(self, child):
        if child not in self.get_children():
            self.get_children().append(child)
            child.set_parent(self)

    def remove_child(self, child):
        if child in self.get_children():
            self.get_children().remove(child)
            child.set_parent(None)

    def is_root(self):
        return self.get_parent() is None

    def depth(self):
        depth = 0
        curr = self.get_parent()

        while curr is not None:
            depth += 1
            curr = curr.get_parent()

        return depth

    # Getters
    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    # Setters
    def set_parent(self, parent):
        self.__parent = parent

    def set_children(self, children):
        self.__children = children
