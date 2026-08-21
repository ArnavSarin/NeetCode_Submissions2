"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        startTimes, endTimes = [], []
        for i in intervals:
            startTimes.append(i.start)
            endTimes.append(i.end)

        heapq.heapify(startTimes)
        heapq.heapify(endTimes)

        rooms, maxRooms = 0, 0

        while len(startTimes) > 0 and len(endTimes) > 0:

            if startTimes[0] < endTimes[0]:
                heapq.heappop(startTimes)
                rooms += 1
            else:
                heapq.heappop(endTimes)
                rooms -= 1

            maxRooms = max(maxRooms, rooms)
        
        return maxRooms


        
        
