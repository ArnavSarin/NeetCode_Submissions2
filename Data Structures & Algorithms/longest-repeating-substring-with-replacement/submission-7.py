class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = defaultdict(int)
        other, max_length, i, j = 0, 1, 0, 1
        largest = s[i]
        hm[s[i]] += 1

        while j<len(s) and i<len(s):
            hm[s[j]] += 1

            print(hm)
            print(largest)

            if hm[s[j]] > hm[largest]:
                print("GOT HERE 0")
                largest = s[j]

            other = sum(hm.values()) - hm[largest]

            if other > k and i < j:
                print("GOT HERE 2")
                hm[s[i]] -= 1
                i+=1
                #NEED TO SUBTRACT OTHER BY ONE 

            max_length = max(max_length,len(s[i:j+1]))
            j+=1

        return max_length




