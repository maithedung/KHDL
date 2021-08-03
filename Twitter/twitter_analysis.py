import GetOldTweets3 as got
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
# ssl._create_unverified_context()
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get_tweets():

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
        'corona virus').setSince("2019-01-01").setUntil("2020-01-01").setMaxTweets(10)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets


get_tweets()
