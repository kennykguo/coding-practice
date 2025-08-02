class Twitter:

    def __init__(self):
        self.user_to_tweet_id = {} # each one stores a min heap?
        self.time = 0 # current time
        self.id_to_followers = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if  userId not in self.user_to_tweet_id:
            self.user_to_tweet_id[userId] = []
        heapq.heappush(self.user_to_tweet_id[userId], (-1 * self.time, tweetId))
        print(self.user_to_tweet_id)

    def getNewsFeed(self, userId: int) -> List[int]:
        # get own heap, and followers heaps
        # want to return most recent tweetIDs
        res = []
        all_to_check = []
        all_to_check.append(userId)
        if userId in self.id_to_followers:
            all_to_check.extend(self.id_to_followers[userId])
        
        print("all to check", all_to_check)
        min_heap = []

        for user_id in all_to_check:
            if user_id not in self.user_to_tweet_id:
                continue
            for val in self.user_to_tweet_id[user_id]:
                min_heap.append(val)
        heapq.heapify(min_heap)
        print(min_heap)

        i = 10
        while min_heap and i > 0:
            val = heapq.heappop(min_heap)
            print(val)
            res.append(val[1])
            i -= 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.id_to_followers:
            self.id_to_followers[followerId] = []
        if followeeId not in self.id_to_followers[followerId]:
            self.id_to_followers[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.id_to_followers:
            return
        if followeeId in self.id_to_followers[followerId]:
            self.id_to_followers[followerId].remove(followeeId)
