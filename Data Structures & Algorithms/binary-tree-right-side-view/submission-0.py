# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []

        levels = []
        queue = deque([(root,0)])

        while len(queue)>0:
            node, depth = queue.popleft()

            if depth < len(levels):
                levels[depth].append(node.val)
            else:
                levels.append([node.val])
            
            if node.left != None:
                queue.append((node.left,depth+1))

            if node.right != None:
                queue.append((node.right,depth+1))

        ans = []
        for level in levels:
            ans.append(level[-1])

        return ans
