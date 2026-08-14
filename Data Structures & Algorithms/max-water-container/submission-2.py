class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptrA, ptrB = 0, len(heights)-1
        maxArea = 0
        while ptrA < ptrB:
            if heights[ptrA] < heights[ptrB]:
                maxArea = max(maxArea,(ptrB-ptrA) * heights[ptrA])
                ptrA += 1
            else:
                maxArea = max(maxArea,(ptrB-ptrA) * heights[ptrB])
                ptrB -=1
        
        return maxArea