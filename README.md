# Sentiment_Analysis_using_Twitter
A tool for analysing the sentiments of public on a topic using their tweets about the topic
Twitter is a social network where people post short, 140-character, status messages called tweets,because tweets are sent out continuously, Twitter is a great way to figure out how people feel about current events. In this post, we'll create a tool that enables us to find out how people feel about two great Indian Leaders. To do this, we'll need to:
Stream tweets from the Twitter API.
Filter out the tweets that aren't relevant.
Process the tweets to figure out what emotions they express about each candidate.
Store the tweets for additional analysis.
# The Twitter Streaming API
We setup a program to get tweets in real-time — let's called this the streamer.
In order to make it easy to work with real-time tweets, Twitter provides the Twitter Streaming API. There are quite a few rules about how to stream tweets from Twitter, but the main ones are:
Create a persistent connection to the Twitter API, and read each connection incrementally.
Process tweets quickly, and don't let your program get backed up.
Handle errors and other issues properly.
The most popular is tweepy, which allows you to connect to the streaming API and handle errors properly.
# Setting up Tweepy
To setup tweepy for start streaming data. The first thing we'll need to do is visit the Twitter Developer Center and create a developer account. This account will enable us to create credentials that let us authenticate with the Twitter Streaming API.
After creating the account, we can go to the Application Console and create a new Twitter application. This will let us get credentials specific to the application, which will let us connect to the API.


