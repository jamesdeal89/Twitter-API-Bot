# practice exploring the Twitter API via a basic bot (@opinionbotCS)
from audioop import avg
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

loggedID= []

def inWords(x):
    if x < 0.2 and x > -0.2:
        return "Mostly Neutral"
    elif x <= -0.2 and x > -0.3:
        return "Leaning Negative"
    elif x >= 0.2 and x < 0.3:
        return "Leaning Positive"
    elif x <= -0.3 and x > -0.5:
        return "Mostly Negative"
    elif x >= 0.3 and x < 0.5:
        return "Mostly Positive"
    elif x <= -0.5:
        return "Overwhelmingly Negative"
    elif x >= 0.5:
        return "Overwhelimgly Positive"

def checkData():
    # gets the raw data of all the tweets @ the bot
    # includes lots and lots of complex data we don't need
    mentions = api.mentions_timeline()
    # converts the data in the first mention into a dictionary
    mentions[0].__dict__
    # iterates through every tweet @ the bot    
    for tweet in mentions:
        # checks to make sure we don't reply to tweets we've already replied to
        # prints the tweet ID and pure extracted tweet text
        print(tweet.id, tweet.text)
        # checks for a specific hastag in the tweet.
        if '#thebatman' in tweet.text.lower():
            # creates a TextBlob version of the tweet for sentiment analysis
            sentimentTweet = textblob.TextBlob(tweet.text)
            # checks if the tweet has positive sentiment
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " hyped!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    # adds replied tweet ID to file
                    loggedID.append(tweet.id)
                # checks if the tweet has negative sentiment
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " you're wrong; The Batman is going to be great", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    loggedID.append(tweet.id)
        elif 'mr.davies' in tweet.text.lower():
            sentimentTweet = textblob.TextBlob(tweet.text)
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " I know that guy!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    loggedID.append(tweet.id)
                    # adds replied tweet ID to file
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    api.update_status(status = "@" + tweet.user.screen_name + " Don't talk about him like that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    loggedID.append(tweet.id)
                    # adds replied tweet ID to file
        elif 'twitter api' in tweet.text.lower():
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                print("tweeting")
                api.update_status(status = "@" + tweet.user.screen_name + " I use that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                loggedID.append(tweet.id)
                # adds replied tweet ID to file
        elif 'you' in tweet.text.lower() or ' opinionbotcs' in tweet.text.lower():
            sentimentTweet = textblob.TextBlob(tweet.text)
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " Thank you for your feedback!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    loggedID.append(tweet.id)
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    api.update_status(status = "@" + tweet.user.screen_name + " That's just rude!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    loggedID.append(tweet.id)
        elif 'analyse' in tweet.text.lower():
            #find hashtag
            print(tweet.id, loggedID) 
            if str(tweet.id) in str(loggedID):
                print("skipping "+ str(tweet.id))
            else:
                location = tweet.text.find("#")
                hashtag = tweet.text[location:]
                print(hashtag)
                #get sample of tweets using tweepy Cursor search the '.items' is the size of the sample. 'lang='en'' makes sure we get tweets which TextBlob can analyse.
                sample = api.search_tweets(q=hashtag, lang = 'en')
                #analyse tweet sentiments
                totalPolarity = 0
                counter = 0
                for dataPoint in sample:
                    counter += 1
                    dataText = textblob.TextBlob(dataPoint.text)
                    totalPolarity += dataText.sentiment.polarity 
                #create average sentiment score
                avgPolarity = totalPolarity / counter
                rndPolarity = round(avgPolarity, ndigits=3)
                # make an easy to understand sentiment scale in words to go alongside it
                wordRating = inWords(rndPolarity)
                #return score to user in a reply
                api.update_status(status = "@" + tweet.user.screen_name + " The sentiment polarity of " + hashtag + " is: " + wordRating + "(" + str(rndPolarity) + ")" + " based on " + str(counter) + " samples", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                # adds replied tweet ID to file
                loggedID.append(tweet.id)
        elif 'testing' in tweet.text.lower():
            # this is for checking and testing the TextBlob sentiment values with test data
            dataText = textblob.TextBlob(tweet.text)
            Polarity = dataText.sentiment.polarity
            wordRating = inWords(Polarity)
            api.update_status(status = "@" + tweet.user.screen_name + " Your test tweet's polarity value is: " + + Polarity + "(" + wordRating + ")", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)



while True:
    checkData()
    time.sleep(15)


"""
making notes on textblob sentiment analysis
the text to be analysed must be put into the textblob data structure using TextBlob(text)
using .tags we can see the words in a 2d array of token and sentiment tag. 
.sentences will break a textblob into sentence tokens
.words will break it into word tokens
using sentence.sentiment.polarity will output a value from -1 to 1 of the sentiment.
"""

