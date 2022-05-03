from os import access
import tweepy
import time

consumer_key = 'your API key'
consumer_secret = 'your API secret'
access_token = 'your access token'
access_token_secret = 'your access token secret'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# update new tweet

# api.update_status("Hello from MrBonchen")
# print("Status Updated!")


FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


# Print all tweets in json format

# tweets = api.mentions_timeline()
# print(tweets)


# find the first tweet with #random and store its id in the text file

# for tweet in tweets:
#     if '#random' in tweet.text:
#         store_last_seen(FILE_NAME, tweet.id)
#         break


# reply to the tweets with #random since the tweet with id from the text file

# def reply():
#     tweets = api.mentions_timeline(
#         read_last_seen(FILE_NAME), tweet_mode='extended')
#     for tweet in reversed(tweets):
#         if '#random' in tweet.full_text.lower():
#             print("Replied To ID" + ' - ' + tweet.full_text)
#             api.update_status("@" + tweet.user.screen_name +
#                               " Random reply for #random tweets!", tweet.id)
#             store_last_seen(FILE_NAME, tweet.id)
# while True:
#     reply()
#     time.sleep(2)


# print the bot account information in json format
user = api.me()
# print(user)


# for follower in tweepy.Cursor(api.followers).items():
# print all followers ' name
#    print(follower.name)

# follow back a follower based on their name
# if follower.name == 'elon musk':
#     follower.follow()


# search for 'programming' and like, retweet 500 of the tweets found. Take a break for 10 seconds after each tweet
search = 'Programming'
num_tweets = 500

for tweet in tweepy.Cursor(api.search, search).items(num_tweets):
    try:
        tweet.favorite()
        print('Tweet Liked')
        tweet.retweet()
        print('Retweeted')
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
