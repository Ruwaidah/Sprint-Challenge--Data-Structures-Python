from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):
        if len(self.storage) < self.capacity and self.current is None:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        else:
            self.current.value = item
            if self.current.next is None:
                while self.current.prev is not None:
                    self.current = self.current.prev
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node:
            if node.value != None:
                list_buffer_contents.append(node.value)
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
