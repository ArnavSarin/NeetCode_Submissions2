class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        ans = []

        def backtrack(arr,total,idx):
            nonlocal ans

            if total > target:
                return

            if total == target:
                ans.append([i for i in arr])
            
            seen = set()
            for i in range(idx, len(candidates)):
                if candidates[i] not in seen:
                    arr.append(candidates[i])
                    backtrack(arr,total+candidates[i], i+1)
                    arr.remove(candidates[i])
                    seen.add(candidates[i])

        backtrack([],0,0)
        return ans