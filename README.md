Welcome to the TappingStone Restaurant Recommendation Python demo application.

This demo application was written and tested using Python 2.7.3 and it is recommended that you use at least Python version 2.7+.
Should there be any issues running it under any other versions of Python, please contact help@tappingstone.com.

Prior to running any of the scripts please fill in your application key in the following files:
com/tappingstone/app/core_actions.py
com/tappingstone/data/mock_data.py

NOTE: This sample application assumes that you have successfully installed the TappingStone python SDK found  here: https://www.tappingstone.com/docs/example
Failure to have the TappingStone Python SDK installed with result in this application not working.

If you would like to put some mock data into your TappingStone account, please take a look at mock_data.py which can be run on it's own to import a set of data (http://archive.ics.uci.edu/ml/datasets/Entree+Chicago+Recommendation+Data) into your account for demo use. Alternatively you can modify the script to import any of your own data and set your own parsers to format your data to be used by the function calls detailed in the TappingStone API (https://www.tappingstone.com/docs/sdk/python/index.html)

Please note that the main application found in com/tappingstone/app depends on some of the data imported by mock_data.py. Namely, it depends on the "items" that are imported into your TappingStone account. If this data is not imported, then tappingStoneDemo.py as is will throw errors. Should you choose not to import the mock data then please alter the main application (tappingStoneDemo.py) accordingly.

File descriptions:
Folder (data):
    mock_data.txt - Mock data set to be used in this demo application
    sampleuserIDList.txt - List of userId's from data.txt should you wish to get recommendations for that user or to use that user's ID
    restaurants.txt - List of restaurants with their name and IDs associated from the data.txt file
    mock_data.py - Demo script to import data found in text files above or to be used and adapted to your own data set
Folder (app):
    tappingStoneDemo.py - Main application
    core_actions.py - class which defines functions related to server actions such as sending requests, parsing requests, creating users, etc.
    behavior_actions.py - class which contains functions that related to user activity such as viewing an item, adding friends, rating an item, etc.
    sampleRestaurantList.txt - file which is used by the main application to display restaurant names and IDs. This file is REQUIRED if you are testing the demo app using the mock data
                                and the main application as is.

General application notes:
The main application will create a user given the user input if the entered ID does not already exist your TappingStone account.

When viewing restaurants, it will give you 10 random restaurants from the list found in sampleRestaurantList.txt. If you want to keep viewing/rating/liking a particular restaurant, just enter in the restaurant ID during the prompts or edit the main application file to your liking.

This application does not do input checking and assumes that you are entering in valid input (i.e. when choosing number of recommendations, it expects an integer).