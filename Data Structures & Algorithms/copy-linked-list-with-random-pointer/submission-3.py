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

        




        # ptr, i, head2 = head, 0, None
        # while ptr != None:
        #     curr = Node(ptr.val)
        #     hm[ptr] = curr
        #     hm[curr] = ptr

        #     if i==0:
        #         head2 = curr
                
        #     ptr = ptr.next
        #     i+=1 

        # ptr = head2

        # while ptr in hm:
        #     old_ptr = hm[ptr]

        #     if old_ptr.next != None:
        #         next_ptr = hm[old_ptr.next]
        #     else:
        #         next_ptr = None

        #     if old_ptr.random != None:
        #         random_ptr = hm[old_ptr.random]
        #     else:
        #         random_ptr = None
        #     ptr.next = next_ptr
        #     ptr.random = random_ptr

        #     ptr = ptr.next

        # return head2

            



       

        

        