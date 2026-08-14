class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(arr, idx):
            nonlocal ans 
            if idx > len(nums):
                return

            ans.append([i for i in arr])

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i+1)
                arr.remove(nums[i])
        
        backtrack([],0)
        return ans