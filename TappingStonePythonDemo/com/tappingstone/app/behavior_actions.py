import stoneapi

__author__ = 'cqin'

'''
   This class is meant to contain all the user related functionality such as rating, viewing, adding friends, disliking, unfriending, etc
'''

class UserActions:
    default_user = None

    def __init__(self):
        print 'Welcome to the Tapping Stone Python SDK Demo App'
        userId = raw_input('Please enter your user ID:')
        self.default_user = userId

    def getUserId(self):
        return self.default_user

    def userView(self, client, userId, itemId):
        try:
            client.auser_view_item(uid=userId, iid=str(itemId))
        except(stoneapi.ItemNotFoundError):
            print 'Error trying to view item, item does not exist!'

    # Method to get N recommendations for given user, call can be done async or non-async
    def getRecommend(self, client, uid, numRecs, async):
        if async is True:
            response = client.aget_recommendations(uid=uid, n=numRecs)
        else:
            response = client.get_recommendations(uid=uid, n=numRecs)
        return response

    # Method for adding a friend to a user's account
    def addFriend(self, client, friendId, async):
        print ''
        # TODO

    # Method for when a user rates an item
    def userRateItem(self, client, userId, itemId, rating, async):
        if async is True:
            response = client.auser_rate_item(userId, itemId, rating)
        else:
            response = client.user_rate_item(userId, itemId, rating)

        print 'You rated ' + str(itemId) + ' a ' + str(rating)
        return response

    def userLikeItem(self, client, userId, itemId, async):
        if async is True:
            response = client.auser_like_item(userId, itemId)
        else:
            response = client.user_like_item(userId, itemId)

        print 'You liked ' + str(itemId)
        return response

    def userDislikeItem(self, client, userId, itemId, async):
        if async is True:
            response = client.auser_dislike_item(userId, itemId)
        else:
            response = client.user_dislike_item(userId, itemId)

        print 'You disliked ' + str(itemId)
        return response

