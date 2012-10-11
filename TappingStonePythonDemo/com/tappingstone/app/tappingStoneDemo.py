import re
import random
from core_actions import ServerActions
from behavior_actions import UserActions

__author__ = 'cqin'

'''
   Main class to be run, depends on behavior_actions.py and core_actions.py
   Must already have stoneapi installed
   Written under Python 2.7.3
   Tested in Python 2.7.3
'''

if __name__ == '__main__':
    print 'Starting Tapping Stone Demo Python App...'

    #Define restaurant maps
    restMap = {}

    file = open('sampleRestaurantList.txt', 'rb')
    lines = file.readlines()
    for line in lines:
        splitLine = re.split('\t', line)
        restMap[str(int(splitLine[0]))] = re.sub(r'\r\n', '', splitLine[1])

    server = ServerActions()
    stoneClient = server.getStoneClient()

    userActions = UserActions()
    userId = userActions.getUserId()

    #Check the userID here, if user doesn't exist, create them.
    response = server.getUserInfo(stoneClient, userId, True)
    server.parseResponse(stoneClient, response, userId)

    menuLoop = True
    while(menuLoop):
        print 'Please choose an option below:'
        print '1. Get userID info'
        print '2. View restaurants'
        print '3. Get recommended restaurants'
        print '4. Quit'
        userChoice = raw_input()

        if userChoice == str(1):
            print 'View user ID info selected'
            response = server.getUserInfo(stoneClient, userId, True)
            server.parseResponse(stoneClient, response, userId)
            print '\n'
        elif userChoice == str(2):
            print 'Now listing 10 RANDOM restaurants:\n'
            keys = restMap.keys()
            for i in range(0, 10):
                randomRest = random.choice(restMap.keys())
                print randomRest + '.' + ' ' + restMap[randomRest]
            print '\n'
            anotherMenuLoop = True
            while(anotherMenuLoop):
                userSelection = raw_input('Please choose a restaurant you\'d like to view:')
                print restMap[userSelection] + 'selected. Please choose an option below:'
                userActions.userView(stoneClient, userId, str(userSelection))
                print '1. Like this restaurant.'
                print '2. Dislike this restaurant.'
                print '3. Rate this restaurant.'
                restaurantChoice = raw_input()
                if restaurantChoice == str(1):
                    response = userActions.userLikeItem(stoneClient, userId, str(userSelection), True)
                    print server.parseResponse(stoneClient, response, userId)
                elif restaurantChoice == str(2):
                    userActions.userDislikeItem(stoneClient, userId, str(userSelection), True)
                elif restaurantChoice == str(3):
                    rating = raw_input('Please enter a rating from 1-5:')
                    userActions.userRateItem(stoneClient, userId, str(userSelection), str(rating), True)
                anotherMenuLoop = False
                print '\n'
        elif userChoice == str(3):
            print 'Please enter the number of recommendations you would like:'
            n = raw_input()
            print 'Now retrieving ' + n + ' recommendations...\n'
            response = userActions.getRecommend(stoneClient, userId, n, True)
            responseMap = server.parseResponse(stoneClient, response, userId)
            print responseMap
            #Get the response Dictionary's IID value only
            list = responseMap['iids']
            for i in list:
                print restMap[i]
            print '\n'
        elif userChoice == str(4):
            print 'Thank you for trying out the Tapping Stone Demo Python App!'
            menuLoop = False

    exit(0)


