"""
355. Design Twitter
Medium
Design a simplified version of Twitter where users can post tweets,
 follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
 Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
 Each item in the news feed must be posted by users who the user followed or by the user themself.
  Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId)
The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId)
The user with ID followerId started unfollowing the user with ID followeeId.
"""

from collections import defaultdict, deque
import heapq


class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(deque)
        self.following = defaultdict(set)
        self.feed_size = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

        if len(self.user_tweets[userId]) > self.feed_size:
            self.user_tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> list:
        tweets = list(self.user_tweets[userId])

        for followeeId in self.following[userId]:
            tweets.extend(self.user_tweets[followeeId])

        top_tweets = heapq.nlargest(self.feed_size, tweets, key=lambda x: x[0])

        return [tweet[1] for tweet in top_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

# Example usage:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# news_feed = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
