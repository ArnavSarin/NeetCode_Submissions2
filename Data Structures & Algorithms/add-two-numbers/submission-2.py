# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    

        ptrA, ptrB = l1, l2

        if ptrA != None and ptrB == None:
            return ptrA
        
        if ptrA == None and ptrB != None:
            return ptrB

        total = ptrA.val + ptrB.val

        carry = 0
        if total >= 10:
            carry = 1
            total -= 10

        ans = ListNode(total)
        ptrA = ptrA.next
        ptrB = ptrB.next

        ptrC = ans

        while ptrA != None and ptrB != None:
            total = carry + ptrA.val + ptrB.val
            
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0

            tempNode = ListNode(total)
            ptrC.next = tempNode
            
            ptrA = ptrA.next
            ptrB = ptrB.next
            ptrC = ptrC.next

        while ptrA != None and ptrB == None:
            total = carry + ptrA.val 
            
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0

            tempNode = ListNode(total)
            ptrC.next = tempNode
            
            ptrA = ptrA.next
            ptrC = ptrC.next

        while ptrA == None and ptrB != None:
            total = carry + ptrB.val 
            
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0

            tempNode = ListNode(total)
            ptrC.next = tempNode
            
            ptrB = ptrB.next
            ptrC = ptrC.next

        if carry == 1:
            ptrC.next = ListNode(carry)
            ptrC = ptrC.next
            ptrC.next = None

        return ans
