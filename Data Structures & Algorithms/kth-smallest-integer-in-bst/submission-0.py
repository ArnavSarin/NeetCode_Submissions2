# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        ans = []
        while len(stack)>0:
            node = stack.pop()

            ans.append(node.val)
                
            if node.right != None:
                stack.append(node.right)
            
            if node.left != None:
                stack.append(node.left)

        return sorted(ans)[k-1]
        
            
