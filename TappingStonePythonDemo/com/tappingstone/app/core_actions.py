import stoneapi

__author__ = 'cqin'
'''
    This is a class contains functions that are not user behavior related actions. This is the class that returns the actual Client
    that allows the behavior_actions.py to make calls to the TappingStone server and is a required class for both the main application and behavior_actions.py

    Please make sure that you enter in your own valid application key below into appKey='{yourApplicationKeyGoesHere}'. Failure to do so will result in a server
    error whenever you try to make calls to TappingStone.
'''

class ServerActions:
    client = None

    def __init__(self):
        #Initalize Stone Client
        appKey = '5x4h1i4p33k3m5h552i615s521c313h'
        apiUrl = 'https://stoneapi.com'
        apiVer = 'v1'
        threadCount = 100

        #Create client for usage
        self.client = stoneapi.Client(appkey=appKey, threads=threadCount, apiurl=apiUrl, apiversion=apiVer)

    # Returns the Stone Client for usage
    def getStoneClient(self):
        return self.client

    # Closes the Stone Client connection
    def closeStoneClient(self, client):
        client.close()

    # Get client information
    def getUserInfo(self, client, uid, async):
        if async is True:
            clientInfo = client.aget_user(uid=uid)
            return clientInfo
        else:
            clientInfo = client.get_user(uid=uid)
            return clientInfo


    # Method to create a user
    def createUser(self, client, uid, async):
        if async is True:
            client.acreate_user(uid=uid)
        else:
            client.create_user(uid=uid)

    # Method to create an item
    def createItem(self, client, async, itemId):
        """
        * Method to create an item
        * Returns a response object that can be passed into parseResponse()
        """
        if async is True:
            response = client.acreate_item(iid=itemId, itypes=(1,))
        else:
            response = client.create_item(iid=itemId)

        return response

    # Method to access items
    def getItemInfo(self, client, async, itemId):
        """
        * Method to get information about a particular item
        * Returns a response object that can be passed into parseResponse()
        """
        if async is True:
            response = client.aget_item(iid=itemId)
        else:
            response = client.get_item(iid=itemId)

        return response

    # Method to unpack the response object
    # TODO seperate into different response unpacks
    def parseResponse(self, client, response, uid):
        """
        * This is a generic response parser to parse the responses returned by the server
        """
        try:
            parsedResponse = client.aresp(response)
            return parsedResponse
        except(stoneapi.UserNotFoundError):
            print 'User was not found'
            # Create a new user if user ID is not found
            self.createUser(client, uid=uid, async=True)
        except(stoneapi.ItemNotCreatedError):
            print 'There is no such item.'
        except(stoneapi.ItemNotFoundError):
            print 'There is no such item.'
