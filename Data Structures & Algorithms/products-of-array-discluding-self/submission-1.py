class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums)):

            ans.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))

        return ans

