class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += "\\" + str(len(i)) + "\\" + i
        print(encoded)
        return encoded



    def decode(self, s: str) -> List[str]:
        iterator = 1
        decoded = []
        while iterator < len(s):
            end_bracket = (s[iterator:]).index("\\")
            number = int(s[iterator:iterator + end_bracket])
            starting = iterator + end_bracket + 1
            ending = iterator + end_bracket + 1 + number
            decoded.append(s[starting:ending])
            iterator += end_bracket + 2 + number
        return decoded

