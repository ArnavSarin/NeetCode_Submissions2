class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        print(nums)
        def backtrack(arr, idx):
            nonlocal ans

            ans.append([i for i in arr])

            seen = set()
            for i in range(idx,len(nums)):
                if nums[i] not in seen:
                    arr.append(nums[i])
                    backtrack(arr,i+1)
                    arr.remove(nums[i])
                    seen.add(nums[i])

            return


        backtrack([],0)
        return ans