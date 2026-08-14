class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(0,len(position)):
            arr.append((position[i],speed[i]))
        
        arr = sorted(arr, key=lambda x:x[0], reverse=True)
        stack = []

        print(arr)

        for p, s in arr:
            stack.append((target-p)/s)

            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            

        



        return 0
