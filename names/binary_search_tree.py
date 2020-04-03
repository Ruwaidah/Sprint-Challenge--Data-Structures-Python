
import sys

sys.path.append("../queue_and_stack")


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Create a node
        node = BinarySearchTree(value)
        if node.value >= self.value:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = node
        else:
            if self.left != None:
                self.left.insert(value)
            else:
                self.left = node

    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
        elif self.value < target:
            if self.right != None:
                return self.right.contains(target)

        return False

    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
