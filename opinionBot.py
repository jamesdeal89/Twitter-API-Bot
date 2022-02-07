# practice exploring the Twitter API via a basic bot (@opinionbotCS)
import tweepy
import time

# authentication for Twitter API
CONSUMER_KEY = 'ed03MoV3IRwE083w1Kqx1RxZ0'
CONSUMER_SECRET = 'zQ1GME6Z4bTdyHC5hpmNdt6WyJ1AAhUCQOYtOd4A6cFWJBdncB'
ACCESS_KEY = '1489504157539377156-nBt7okNSLWmJtDNN4BUaBu75DV6Fki'
ACCESS_SECRET = 'Ws4kEpwjM6YdJH31qwmn8r7ROz1fnN8VtlM9d47ZpmRyH'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

checkedIDs = []

def checkData():
    # gets the raw data of all the tweets @ the bot
    # includes lots and lots of complex data we don't need
    mentions = api.mentions_timeline()
    # converts the data in the first mention into a dictionary
    mentions[0].__dict__
    # iterates through every tweet @ the bot
    for tweet in mentions:
        # checks to make sure we don't reply to tweets we've already replied to
        if tweet.id in checkedIDs:
            pass
        else:
            # prints the tweet ID and pure extracted tweet text
            print(tweet.id, tweet.text)
            # checks for a specific hastag in the tweet.
            if '#thebatman' in tweet.text.lower():
                # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                print("tweeting")
                api.update_status(status = "@" + tweet.user.screen_name + " hyped!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                # adds replied tweet ID to list
                checkedIDs.append(tweet.id)
            if 'mr.davies' in tweet.text.lower():
                # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                print("tweeting")
                api.update_status(status = "@" + tweet.user.screen_name + " cringe.", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                checkedIDs.append(tweet.id)
                # adds replied tweet ID to list
            if 'twitter api' in tweet.text.lower():
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " I use that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    checkedIDs.append(tweet.id)
                    # adds replied tweet ID to list

while True:
    checkData()
    time.sleep(15)


