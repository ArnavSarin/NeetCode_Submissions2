"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
        hm = {}

        ptr = head

        while ptr is not None:
            hm[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head

        while ptr is not None:
            if ptr.next != None: 
                hm[ptr].next = hm[ptr.next]
            else:
                hm[ptr].next = None
            if ptr.random != None:
                hm[ptr].random = hm[ptr.random]
            else:
                hm[ptr].random = None

            ptr = ptr.next
        
        return hm[head]
            



       

        

        