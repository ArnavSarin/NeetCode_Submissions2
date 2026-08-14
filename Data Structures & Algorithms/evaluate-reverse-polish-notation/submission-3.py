class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value2 - value1)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(int(value2 / value1))
            else:
                stack.append(int(i))
            print(stack)
        
        return stack[0]