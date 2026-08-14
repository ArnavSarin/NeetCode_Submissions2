class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(arr, idx):
            nonlocal ans

            if idx==len(s):
                ans.append([i for i in arr])
                return

            for i in range(idx,len(s)):
                if s[idx:i+1] == s[idx:i+1][::-1]:
                    arr.append(s[idx:i+1])
                    backtrack(arr,i+1)
                    arr.remove(s[idx:i+1])

        backtrack([],0)
        return ans