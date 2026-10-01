class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        ans = 0
        n = len(heights)

        for i in range(0,n+1):
            while stack and (i==n or heights[stack[-1]]>=heights[i]):
                j = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                ans = max(ans,width*j)
            stack.append(i)

        
        return ans
        
       


