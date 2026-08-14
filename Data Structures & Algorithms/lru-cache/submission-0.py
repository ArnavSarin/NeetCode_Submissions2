class Node: 
    def __init__(self, key = 0, value = 0):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head 


    def remove(self,node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev 

    def insert_at_front(self,node):
        first_node = self.head.next
        
        self.head.next = node
        node.next = first_node

        node.prev = self.head
        first_node.prev = node 
        
    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        
        node = self.hm[key]
        self.remove(node)
        self.insert_at_front(node)

        return node.value
        
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.hm:
            node = Node(key,value)
            self.remove(self.hm[key])
            self.insert_at_front(node)
            self.hm[key] = node
            return
        
        if len(self.hm) == self.capacity:
            lru = self.tail.prev 
            self.remove(lru)
            del self.hm[lru.key]

        node = Node(key,value)
        self.hm[key] = node
        self.insert_at_front(node)
        return



        
