class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0,0
        # hm = defaultdict()
        length = 0
        curr = ""
        while i<len(s) and j<len(s):
            if s[j] not in curr:
                curr += s[j]
                # hm[s[j]] = j
                j+=1 
            else:
                i += 1
                j = i + 1
                curr = s[i]
                # i = hm[s[j]]+1
                # j = i+1
                # curr = ""
                # print(i)
                # print(j)
            # print("GOT HERE")
            # print(curr)
            length = max(length, len(curr))

        return length
                
        


