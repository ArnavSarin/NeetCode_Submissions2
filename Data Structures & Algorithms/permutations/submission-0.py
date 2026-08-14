class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(arr):
            nonlocal ans

            if len(arr) == len(nums):
                ans.append([i for i in arr])

            for i in range(0,len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.remove(nums[i])

            return

        
        backtrack([])
        return ans