from typing import List

class Twitter:

    def __init__(self):
        self.followee = {}
        self.tweets = []
      
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followee.keys():
            self.followee[userId] = [userId]
        self.tweets.append([userId, tweetId])         
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        num = 0
        for tweet in reversed(self.tweets):
            if num >= 10:
                break
            if (tweet[0] in self.followee.get(userId, [userId])):
                feed.append(tweet[1])
                num += 1
        return feed
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followee:
            self.followee[followerId] = [followerId]
        if followeeId not in self.followee[followerId]:
            self.followee[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followee and followeeId in self.followee[followerId] and followeeId != followerId:
            self.followee[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)