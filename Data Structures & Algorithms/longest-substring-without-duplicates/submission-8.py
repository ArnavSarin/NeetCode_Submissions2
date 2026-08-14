class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0,0
        length = 0
        curr = ""
        while i<len(s) and j<len(s):
            if s[j] not in curr:
                curr += s[j]
                j+=1 
            else:
                i += 1
                j = i + 1
                curr = s[i]
            length = max(length, len(curr))

        return length
                
        


