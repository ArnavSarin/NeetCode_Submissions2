class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posted = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posted[userId].append((-self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        followeeIds = []
        if userId in self.users:
            followeeIds = self.users[userId]
        
        tweets = [i for i in self.posted[userId]]

        for f in followeeIds:
            tweets += self.posted[f]
        
        heapq.heapify(tweets)

        newsfeed = []
        for i in range(10):
            if tweets:
                post = heapq.heappop(tweets)
                newsfeed.append(post[1])

        return newsfeed 
         
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
