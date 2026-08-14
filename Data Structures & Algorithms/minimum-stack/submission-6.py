class MinStack:

    def __init__(self):
        self.stack = []
        self.minArray = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minArray, val)
        
    def pop(self) -> None:
        popped = self.stack.pop()
        print(popped)
        if self.minArray[0] == popped:
            print("GOT HERE")
            print(self.minArray[0])
            heapq.heappop(self.minArray)
        else:
            self.minArray.remove(popped)
            heapq.heapify(self.minArray)
            
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minArray[0]

        
