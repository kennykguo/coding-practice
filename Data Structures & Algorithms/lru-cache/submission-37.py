class Node:
    def __init__(self, key, value, next = None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    # these methods only update the dd ll, not the cache dictionary
    def remove(self, node):
        # edge cases: removing at the head, and removing at the tail
        # removing at head, meaning node.prev's node doesn't exist
        if not node.prev:
            # need to update the head
            self.head = self.head.next
        else:
            node.prev.next = node.next
        
        # removing the tail
        if not node.next:
            # need to update the tail
            self.tail = self.tail.prev
        else:
            node.next.prev = node.prev
        return node


    def insert_head(self, node):
        # edge cases: 1 node or multiple nodes already
        # if 1 node or more, then only update head
        # if zero nodes, need to update tail and head
        # see if we need to update the tail node
        if not self.tail and not self.head: # zero nodes
            self.head = node
            self.tail = node
        else: # one node already exists, only update the head ptr when inserting
            node.prev = None
            old_head = self.head # old node
            self.head = node # update head ptr
            node.next = old_head
            old_head.prev = node


    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:
        # remove from the back, if calling get, move to the front
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        node = self.remove(node)
        self.insert_head(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update it's value
            node = self.cache[key]
            node.value = value
            node = self.remove(node)
            self.insert_head(node)
            return
        
        # need to create a new node, check if cache is full
        # cache is full
        if len(self.cache) == self.capacity:
            # print('hello')
            # if self.tail:
            #     print(self.tail.value)
            # if self.head:
            #     print(self.head.value)
            
            # delete the tail
            node = self.remove(self.tail)
            del self.cache[node.key]
            # print(self.cache)
        
        node = Node(key, value)
        self.insert_head(node)
        self.cache[key] = node
        # print(self.cache)







