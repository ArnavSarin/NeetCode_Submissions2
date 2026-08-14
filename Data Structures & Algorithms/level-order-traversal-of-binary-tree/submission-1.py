# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = []

        if root == None:
            return ans

        queue = deque([(root, 0)])

        while len(queue)>0:
            node, depth = queue.popleft()

            if depth < len(ans):
                ans[depth].append(node.val)
            else:
                ans.append([node.val])

            if node.left != None:
                queue.append((node.left,depth+1))
            if node.right != None:
                queue.append((node.right,depth+1))

        return ans

