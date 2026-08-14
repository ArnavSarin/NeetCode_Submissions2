class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.hm[key]
        print("GOT HERE START")
        print(timestamps)

        left, right, ans = 0, len(timestamps)-1, 0

        if len(timestamps) == 0 or timestamp < timestamps[0][0]:
            return ""

        while left <= right:
            mid = (left+right)//2

            if timestamps[mid][0] == timestamp:
                print("GOT HERE 0")
                return timestamps[mid][1]
            elif timestamp > timestamps[mid][0]:
                left = mid+1
                print("GOT HERE 1")
                ans = max(mid,ans)
                print(ans)
                print(mid)
            else:
                print("GOT HERE 2")
                right = mid-1

        return timestamps[ans][1]

        
