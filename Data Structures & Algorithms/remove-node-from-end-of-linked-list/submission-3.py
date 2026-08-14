# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        arr = []

        while ptr != None:
            arr.append(ptr)
            ptr = ptr.next

        if n > len(arr):
            return head
        
        if n == len(arr):
            return head.next

        value = arr[len(arr)-n]

        prev = None
        ptr = head 

        while ptr != None:

            if ptr == value:
                prev.next = ptr.next

            prev = ptr
            ptr = ptr.next

        return head 

        
        