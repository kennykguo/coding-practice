class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.max_length = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = None
        node.next = None
        return node

    def insert_head(self, node):
        node.next = self.head
        node.prev = None

        if self.head:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert_head(node)
            return

        if len(self.cache) == self.max_length:
            old = self.tail
            self.remove(old)
            del self.cache[old.key]

        node = Node(key, value)
        self.cache[key] = node
        self.insert_head(node)