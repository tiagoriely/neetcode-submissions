class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}
        
        # LRU end (oldest)
        self.left = Node(0, 0)
        # MRU end (most recent)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        # Save the neighbouring nodes before removing
        prev = node.prev # left side
        nxt = node.next # right side

        # Create the new links
        prev.next = nxt # connect prev to nxt (nxt is on the right side of prev)
        nxt.prev = prev # connect nxt to prev (prev is on the left side of nxt)


    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        # Make the end of the list and the former latest node point at a new 'inserted' node
        prev.next = node # Right (end of the list)'s left hand holds the new inserted node
        nxt.prev = node # Former last node points to the new node

        # Make the new node point at the old latest node and end of the linkedlist
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])
        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])
        
        if len(self.cacheMap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]        


        
