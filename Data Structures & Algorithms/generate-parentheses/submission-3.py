class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = set()

        def backtrack(value, remaining):
            nonlocal ans 

            if remaining == 0:
                ans.add(value[:])
                return

            for i in range(len(value) + 1):
                new_value = value[:i] + "()" + value[i:]
                backtrack(new_value, remaining - 1)

        backtrack("", n)
        return list(ans)