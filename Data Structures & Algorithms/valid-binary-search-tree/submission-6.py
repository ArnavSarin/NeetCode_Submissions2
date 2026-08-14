# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = deque([(root,float("-inf"),float("inf"))])

        while len(queue) > 0:
            node, left, right = queue.popleft()

            if not (left < node.val < right):
                return False 
            
            if node.left != None:
                queue.append((node.left, left, node.val))
            
            if node.right != None:
                queue.append((node.right, node.val, right))

        return True


        
        # if root.left != None:
        #     if root.left.val < root.val:
        #         self.isValidBST(root.left)
        #     else:
        #         return False
        
        # if root.right != None:
        #     if root.right.val > root.val:
        #         self.isValidBST(root.right)
        #     else:
        #         return False

        # if root.left == None and root.right == None:

        # left_root, right_root = True, True
        # if root.left != None:
        #     left_root = self.isValidBST(root.left)
        
        # if root.right != None:
        #     right_root = self.isValidBST(root.right)

        # return left_root and right_root
            
        
        # print(root.val)
        # return True
        

