class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            idx = abs(nums[i])
            if nums[idx] * -1 == abs(nums[idx]):
                return abs(nums[i])

            nums[idx] = nums[idx]*-1
        
        return -1