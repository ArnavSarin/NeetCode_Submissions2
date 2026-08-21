"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node == None:
            return None

        queue = deque([node])
        hm = defaultdict(Node)
        start = hm[node] = Node(node.val)
        seen = {start}

        while len(queue)>0:
            current = queue.popleft()

            new_neighbors = []
            for i in current.neighbors:
                if i not in seen: 
                    temp = hm[i] = Node(i.val)
                    new_neighbors.append(temp)
                    queue.append(i)
                    seen.add(i)
                else:
                    new_neighbors.append(hm[i])
                    

            hm[current].neighbors = new_neighbors

        return start

        
            

            


                


        