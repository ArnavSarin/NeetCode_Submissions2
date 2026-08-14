class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptrA, ptrB = 0, len(heights)-1

        maxArea = 0
        while ptrA < ptrB:
            print("GOT HERE")
            print(ptrA)
            print(ptrB)
            if heights[ptrA] < heights[ptrB]:
                print("GOT HERE 0")
                maxArea = max(maxArea,(ptrB-ptrA) * heights[ptrA])
                ptrA += 1
            else:
                print("GOT HERE 1")
                maxArea = max(maxArea,(ptrB-ptrA) * heights[ptrB])
                ptrB -=1
        
        return maxArea