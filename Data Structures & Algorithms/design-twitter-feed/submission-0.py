import heapq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter -= 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([self.counter, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following.get(userId, set()) | {userId}
        
        for user in users:
            feed = self.tweets.get(user, [])
            if feed:
                idx = len(feed) - 1
                counter, tweetId = feed[idx]
                heapq.heappush(heap, (counter, tweetId, user, idx))
        res = []
        while heap and len(res) < 10:
            counter, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:
                idx -= 1
                counter, tweetId = self.tweets[user][idx]
                heapq.heappush(heap, (counter, tweetId, user, idx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId) 
        
