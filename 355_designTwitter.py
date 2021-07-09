class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.following = {}
        # user - (tweet_id, timestamp)
        self.user_tweets = {}
        self.position = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.following:
            self.following[userId] = set()
            self.user_tweets[userId] = set()
        self.user_tweets[userId].add((tweetId, self.position))
        self.position += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        """
        possible_tweets = []
        if userId in self.user_tweets:
            for tweet in self.user_tweets[userId]:
                possible_tweets.append(tweet)
            for following_user in self.following[userId]:
                if following_user in self.user_tweets:
                    for tweet in self.user_tweets[following_user]:
                        possible_tweets.append(tweet)
            possible_tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet[0] for tweet in possible_tweets[:10]]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.following:
            self.following[followerId] = set()
            self.user_tweets[followerId] = set()
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)