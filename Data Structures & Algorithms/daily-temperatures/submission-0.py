class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i in range(0,len(temperatures)):

            while stack and temperatures[i]>temperatures[stack[-1]]:
                val = stack.pop()
                ans[val] = i-val

            stack.append(i)

        while stack:
            val = stack.pop()
            ans[val] = 0

        return ans