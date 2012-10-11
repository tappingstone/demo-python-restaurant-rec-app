__author__ = 'cqin'

'''
   This is meant to be used to populate a Tapping Stone's Dev's demo account with some mock data to be used with the main application found in
   com/tappingstone/app/tappingStoneDemo.py

   Should you choose not to import the mock data, be aware that the main application will throw errors due to it making calls onto items that are imported
   using this script. Please modify the main application and this script accordingly if you wish to test using your own dataset.

   All calls are done using async. Changing these calls to be non-asyncronous will result in a really slow runtime. It is best to leave this
   file as is in regards to the server calls.
'''

if __name__ == '__main__':
    import re
    import stoneapi

    #Initalize Stone Client
    appKey = ''
    apiUrl = 'https://stoneapi.com'
    apiVer = 'v1'
    threadCount = 100

    #Create client for usage
    client = stoneapi.Client(appkey=appKey, threads=threadCount, apiurl=apiUrl, apiversion=apiVer)

    file = open('mock_data.txt', 'r')
    lines = file.readlines()

    userNames = {}
    foodPlaces = {}

    #For each line, add to dictionary to get total unique "user names"
    for line in lines:
        userNames[line.split()[1]] = ''
        splitLine = line.split()
        # Create unique item map
        for i in range(2, len(splitLine)):
            # Strip out the alpha characters since they are not related to the actual item name
            strippedId = re.sub(r"\D", "", splitLine[i])
            foodPlaces[strippedId] = ''
    file.close()

    try:
        print 'Creating users...'
        #create the users
        for key in userNames.keys():
            print key
            client.acreate_user(uid=str(key), userName=str(key))
            print 'User:' + key + ' created'

        print 'Now creating items...'
        #create the "items"
        for key in foodPlaces.keys():
            print key
            client.acreate_item(iid=str(key), itypes=(1,))
            print 'Item' + key + 'created'

        #Add user view data
        for key in userNames.keys():
            for line in lines:
                if line.split()[1] == key:
                    lineSplit = line.split()
                    for i in range(2, len(lineSplit)):
                        #Only take valid "items", 0 is an entry point and -1 is an invalid end point
                        if line.split()[i] != '0' and line.split()[i] != '-1':
                            #Strip out the letters so that the "items" will match
                            strippedItem = re.sub(r"\D", "", line.split()[i])
                            client.auser_view_item(uid=key, iid=str(strippedItem))
                            print 'User:' + key + ' ' + 'viewed item:' + ' ' + strippedItem

    except (stoneapi.UserNotCreatedError, stoneapi.UserNotFoundError, stoneapi.ItemNotCreatedError):
        print 'Error creating user!'

    client.close()
    print 'Done'