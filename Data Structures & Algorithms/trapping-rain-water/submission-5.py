class Solution:
    def trap(self, height: List[int]) -> int:
       
        if len(height)==0:
            return 0

        ans = 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]

        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax= max(height[l], leftMax)
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r],rightMax)
                ans += rightMax - height[r]
        return ans
    