# Name: Johnson Dinh
# Time: 30:00
# Language: Python3
import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Maps global time to tweet. We use a negative decrementing integer 
        # so Python's min-heap inherently acts as a max-heap for timestamps.
        self.time = 0
        
        # Maps userId -> list of [timestamp, tweetId]
        self.tweetMap = defaultdict(list)
        
        # Maps followerId -> set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with the current global timestamp
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1 # Decrement to simulate max-heap ordering

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        
        # Users implicitly follow themselves to see their own tweets
        self.followMap[userId].add(userId)
        
        # 1. Initialize the heap with the SINGLE most recent tweet from everyone we follow
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Get the index of the last tweet this user posted
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                
                # Push [timestamp, tweetId, followeeId, index_of_previous_tweet]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])
                
        # 2. Extract the top 10 most recent tweets
        while heap and len(res) < 10:
            time, tweetId, followeeId, next_index = heapq.heappop(heap)
            res.append(tweetId)
            
            # 3. If the user whose tweet we just popped has more tweets, 
            # push their next most recent tweet into the heap!
            if next_index >= 0:
                next_time, next_tweetId = self.tweetMap[followeeId][next_index]
                heapq.heappush(heap, [next_time, next_tweetId, followeeId, next_index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)