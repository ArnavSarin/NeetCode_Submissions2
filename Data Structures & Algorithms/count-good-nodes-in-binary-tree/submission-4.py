# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if root == None:
            return 0

        ans = 0
        stack = [(root,float("-inf"))]

        while len(stack)>0:
            node, maximum = stack.pop()

            if node.val >= maximum:
                print("GOT HERE")
                print(node.val)
                print(maximum)
                ans += 1
            
            if node.left != None:
                stack.append((node.left,max(node.val, maximum)))

            if node.right != None:
                stack.append((node.right,max(node.val, maximum)))

        return ans
