class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(math.sqrt((x-0)**2 + (y-0)**2), [x,y]) for x,y in points]

        heapq.heapify(distances)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(distances)[1])
        
        return ans

            