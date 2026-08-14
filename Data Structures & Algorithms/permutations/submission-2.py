class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(arr, remaining):
            nonlocal ans

            if len(arr)==len(nums):
                ans.append([i for i in arr])

            for i in range(0,len(remaining)):
                arr.append(remaining[i])
                temp = remaining[:i] + remaining[i+1:]
                backtrack(arr,temp)
                arr.remove(remaining[i])

            return

        backtrack([],nums)
        return ans
