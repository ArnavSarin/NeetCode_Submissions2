# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr = head 
        arr = []
        while ptr != None:
            arr.append(ptr)
            ptr = ptr.next

        print([i.val for i in arr])

        for i in range (1,len(arr)):
            subtract = i
            if i%2==1:
                subtract = len(arr)-math.ceil(i/2)
           
            if i%2==0:
                subtract = i//2
            
            print(subtract)
            head.next = arr[subtract]
            head = head.next
            
        head.next = None

            

