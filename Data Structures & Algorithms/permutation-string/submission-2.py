class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        ans = ''.join(sorted(s1))
        length = len(s1)
        i = 0

        print(ans)
        
        while i+length<=len(s2):
            temp = ''.join(sorted(s2[i:i+length]))
            print(temp)
            if temp == ans:
                return True
            i+=1

        return False
        