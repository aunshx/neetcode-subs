from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.heap = []
        self.count = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.heap, (self.count, userId, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.following[userId] | {userId}
        heap = self.heap[:]
        res = []
        while heap and len(res) < 10:
            _, uid, tid = heappop(heap)
            if uid in people:
                res.append(tid)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
