class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def backtrack(arr, total, idx):
            nonlocal ans 
            if total > target:
                return
            
            if total == target:
                ans.append([i for i in arr])

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(arr,total + nums[i], i)
                arr.remove(nums[i])
                
        backtrack([], 0, 0)
        return ans 

        


