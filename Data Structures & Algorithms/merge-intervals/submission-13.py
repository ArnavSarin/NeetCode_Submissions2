class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedIntervals = sorted(intervals, key=lambda x:x[0], reverse=False)
        print(sortedIntervals)

        ans = []

        for i in sortedIntervals:
            length = len(ans)
            
            if length == 0 or i[0] > ans[length-1][1]:
                # print("GOT HERE A")
                ans.append(i)     
            else:
                j = length-1
                tempInterval = i
                # print("GOT HERE 1")
                # print(j)
                # print(tempInterval)
                
                while j!=0 and tempInterval[0] <= ans[j][1]:
                    #STATEMENT 1: EITHER EATS UP INTERVAL
                    #STATEMENT 2: GOES BEFORE INTERVAL
                
                    # if tempInterval[1] < ans[j][0] and tempInterval[0] > ans[j-1][1]:
                    #     print("GOT HERE 2")
                    #     ans.insert(j,tempInterval)
                    #     break

                    if not (tempInterval[1] < ans[j][0]):
                        # print("GOT HERE 4")
                        tempInterval = [
                            min(tempInterval[0],ans[j][0]), 
                            max(tempInterval[1],ans[j][1])]
                        # print(tempInterval)
                        # print(j)
                        ans.pop()

                    j-=1 

                if j != 0:
                    ans.append(tempInterval)

                if j == 0:
                    # print("GOT HERE")
                    if tempInterval[1] < ans[j][0]:
                        ans.insert(0,tempInterval)
                    elif tempInterval[0] > ans[j][1]:
                        ans.insert(1,tempInterval)
                    else:
                        ans[0] = [
                            min(tempInterval[0],ans[0][0]), 
                            max(tempInterval[1],ans[0][1])]
            # print(ans)

        return ans