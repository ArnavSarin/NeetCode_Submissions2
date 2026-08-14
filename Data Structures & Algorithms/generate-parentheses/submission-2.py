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

            # if value == "":
            #     backtrack("()",remaining-1)

            # else:

            #     value = value + "()"
            #     backtrack(value,remaining-1)
            #     value = value[:-2]

            #     if value + "()" != "()" + value:
            #         value = "()" + value 
            #         backtrack(value,remaining-1)
            #         value = value[2:]

            #     value = "(" + value + ")"
            #     backtrack(value,remaining-1)
            #     value = value[1:-1]

        backtrack("", n)
        return [i for i in ans]