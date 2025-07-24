class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.tail = self.head = None

    def get(self, key: int) -> int:
        # when we get an item, it goes to the back of the queue
        # O(1)
        if key in self.cache:
            cur = self.cache[key] # current node

            # move it to the back
            # cases - at the front, at the back, in the middle
            if self.head == self.tail: # one node only, then return automatically
                return self.cache[key].val

            # at the front
            if self.head == cur:

                self.head = self.head.next # move head pointer forward
                self.head.prev = None # new head points to nothing backwards
                cur.next = None # clear old head's next pointer

                cur.prev = self.tail # old head points backwards to tail
                self.tail.next = cur # tail points forward to old head
                self.tail = cur # update tail pointer to old head

            # at the back, then stays at the back
            elif cur == self.tail:
                return self.cache[key].val
                
            # in the middle
            else:
                prev = cur.prev # store previous node
                next = cur.next # store next node

                prev.next = cur.next # connect previous to next (skip current)
                next.prev = prev # connect next back to previous (skip current)
                cur.next = None # clear current's next pointer

                cur.prev = self.tail # current points backwards to tail
                self.tail.next = cur # tail points forward to current
                self.tail = cur # update tail pointer to current
            
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            # update existing node in hashmap and move to tail
            existing_node = self.cache[key]
            existing_node.val = value # update value in existing node
            
            # move to tail
            if self.head == self.tail: # only one node
                return
            elif existing_node == self.tail: # already at tail
                return
            elif self.head == existing_node: # at front

                # delete, move forward
                self.head = self.head.next # move head pointer forward
                self.head.prev = None # new head points to nothing backwards
                existing_node.next = None # clear old head's next pointer


                existing_node.prev = self.tail # old head points backwards to tail
                self.tail.next = existing_node # tail points forward to old head
                self.tail = existing_node # update tail pointer to old head


            else: # in middle
                prev = existing_node.prev # store previous node
                next = existing_node.next # store next node

                prev.next = existing_node.next # connect previous to next (skip existing)
                next.prev = prev # connect next back to previous (skip existing)
                existing_node.next = None # clear existing's next pointer
                
                existing_node.prev = self.tail # existing points backwards to tail
                self.tail.next = existing_node # tail points forward to existing
                self.tail = existing_node # update tail pointer to existing
        
        else:   
            # check if cache is at capacity for new keys
            if len(self.cache) == self.capacity:
                evicted_key = self.head.key # store key of node being evicted
                self.cache.pop(evicted_key) # remove from hash map
                self.head = self.head.next # move head pointer forward

            # create new node for new key
            new_node = Node(key, value)
            if not self.cache: # empty cache
                self.head = new_node # new node becomes head
                self.tail = new_node # new node becomes tail
            else: # non-empty cache
                new_node.prev = self.tail # new node points backwards to current tail
                self.tail.next = new_node # current tail points forward to new node
                self.tail = new_node # update tail pointer to new node
            
            # add new node to hash map
            self.cache[key] = new_node
