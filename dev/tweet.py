import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

'''
Instantiate the api through environment variable access
'''
def twitterauth():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)

def tweet_collect(api, queries, no_tweets):
    columns = ["Date Created", "Number of Likes", "Source or Device", "Content"]
    all_tweets = []

    for query in queries:
        try:
            tweets = api.search_tweets(q=query, lang="en", count=no_tweets, tweet_mode='extended')
            tweet_attributes = [[tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]
            all_tweets.extend(tweet_attributes)
        except BaseException as e:
            print("null on",str(e))

    df = pd.DataFrame(all_tweets, columns=columns)
    return df
    
def main():
    api = twitterauth()
    queries = [
        "'Pfizer''COVID''vaccine'-filter:retweets AND -filter:replies AND -filter:links", 
        "'Moderna''COVID''vaccine'-filter:retweets AND -filter:replies AND -filter:links"
    ]

    tweets_df = tweet_collect(api, queries, 10)
    tweets_df.to_csv('tweetdata.csv', index=False)

if __name__ == "__main__":
    main()