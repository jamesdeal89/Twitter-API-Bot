# practice exploring the Twitter API via a basic bot (@opinionbotCS)
import tweepy
import textblob
import time

# authentication for Twitter API
CONSUMER_KEY = 'ed03MoV3IRwE083w1Kqx1RxZ0'
CONSUMER_SECRET = 'zQ1GME6Z4bTdyHC5hpmNdt6WyJ1AAhUCQOYtOd4A6cFWJBdncB'
ACCESS_KEY = '1489504157539377156-nBt7okNSLWmJtDNN4BUaBu75DV6Fki'
ACCESS_SECRET = 'Ws4kEpwjM6YdJH31qwmn8r7ROz1fnN8VtlM9d47ZpmRyH'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



def checkData():
    #opens the log of previously replied tweet IDs to make sure there's no doubled up replies
    fileData = open("logged.txt","r+")
    # gets the raw data of all the tweets @ the bot
    # includes lots and lots of complex data we don't need
    mentions = api.mentions_timeline()
    # converts the data in the first mention into a dictionary
    mentions[0].__dict__
    # iterates through every tweet @ the bot
    for tweet in mentions:
        # checks to make sure we don't reply to tweets we've already replied to
        if str(tweet.id) in fileData.read():
            pass
        else:
            # prints the tweet ID and pure extracted tweet text
            print(tweet.id, tweet.text)
            # checks for a specific hastag in the tweet.
            if '#thebatman' in tweet.text.lower():
                # creates a TextBlob version of the tweet for sentiment analysis
                sentimentTweet = textblob.TextBlob(tweet.text)
                # checks if the tweet has positive sentiment
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " hyped!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    # adds replied tweet ID to file
                    fileData.write(str(tweet.id)+"%d\r\n")
                # checks if the tweet has negative sentiment
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " you're wrong; The Batman is going to be great", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    fileData.write(str(tweet.id)+"%d\r\n")
            if 'mr.davies' in tweet.text.lower():
                sentimentTweet = textblob.TextBlob(tweet.text)
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " I know that guy!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    fileData.write(str(tweet.id)+"%d\r\n")
                    # adds replied tweet ID to file
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " Don't talk about him like that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    fileData.write(str(tweet.id)+"%d\r\n")
                    # adds replied tweet ID to file
            if 'twitter api' in tweet.text.lower():
                # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                print("tweeting")
                api.update_status(status = "@" + tweet.user.screen_name + " I use that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                fileData.write(str(tweet.id)+"%d\r\n")
                # adds replied tweet ID to file
            if 'you' in tweet.text.lower() or ' opinionbotcs' in tweet.text.lower():
                sentimentTweet = textblob.TextBlob(tweet.text)
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " Thank you for your feedback!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    fileData.write(str(tweet.id)+"%d\r\n")
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " That's just rude!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    fileData.write(str(tweet.id)+"%d\r\n")
    fileData.close()


while True:
    checkData()
    time.sleep(15)


"""
testing and making notes on textblob sentiment analysis
the text to be analysed must be put into the textblob data structure using TextBlob(text)
using .tags we can see the words in a 2d array of token and sentiment tag. 
.sentences will break a textblob into sentence tokens
.words will break it into word tokens
using sentence.sentiment.polarity will output a value from -1 to 1 of the sentiment.
"""

