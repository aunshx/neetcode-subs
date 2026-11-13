from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.following[userId] | {userId}
        res = []
        heap = []
        for uid in people:
            for tweet in self.tweets[uid][-10:]:
                heappush(heap, tweet)
        while heap and len(res) < 10:
            res.append(heappop(heap)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
