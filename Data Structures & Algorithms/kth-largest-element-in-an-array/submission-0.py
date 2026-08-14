class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp =[-i for i in nums]
        heapq.heapify(temp)

        for i in range(k):
            value = heapq.heappop(temp)

        return -value