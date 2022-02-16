# practice exploring the Twitter API via a basic bot (@opinionbotCS)
from audioop import avg
import tweepy
import textblob
import time
import GPTgenerator
import random

# authentication for Twitter API
CONSUMER_KEY = 'ed03MoV3IRwE083w1Kqx1RxZ0'
CONSUMER_SECRET = 'zQ1GME6Z4bTdyHC5hpmNdt6WyJ1AAhUCQOYtOd4A6cFWJBdncB'
ACCESS_KEY = '1489504157539377156-nBt7okNSLWmJtDNN4BUaBu75DV6Fki'
ACCESS_SECRET = 'Ws4kEpwjM6YdJH31qwmn8r7ROz1fnN8VtlM9d47ZpmRyH'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


loggedID= []
timeCount = 43201
prompts = ["iPhones", "Apple", "Facebook", "Twitter", "Artifical Intelligence", "Google", "Memes", "Python", "Programming", "Batman", "Conspiracy Theories", "Computer Science", "The future", "Life", "Elon Musk", "Books", "Marvel"]

def inWords(x):
    if x < 0.05 and x > -0.05:
        return "Mostly Neutral"
    elif x <= -0.05 and x > -0.1:
        return "Leaning Negative"
    elif x >= 0.05 and x < 0.1:
        return "Leaning Positive"
    elif x <= -0.1 and x > -0.12:
        return "Mostly Negative"
    elif x >= 0.1 and x < 0.12:
        return "Mostly Positive"
    elif x <= -0.12:
        return "Overwhelmingly Negative"
    elif x >= 0.12:
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
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " hyped!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    # adds replied tweet ID to file
                    loggedID.append(tweet.id)
                # checks if the tweet has negative sentiment
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " you're wrong; The Batman is going to be great", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    loggedID.append(tweet.id)
        elif 'mr.davies' in tweet.text.lower():
            sentimentTweet = textblob.TextBlob(tweet.text)
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " I know that guy!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    loggedID.append(tweet.id)
                    # adds replied tweet ID to file
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " Don't talk about him like that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    loggedID.append(tweet.id)
                    # adds replied tweet ID to file
        elif 'twitter api' in tweet.text.lower():
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                # makes a tweet @ing the user. the 'tweet.id' makes it go into a response to a specific thread
                print("tweeting")
                try:
                    api.update_status(status = "@" + tweet.user.screen_name + " I use that!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                except:
                    print("API error when responding")
                loggedID.append(tweet.id)
                # adds replied tweet ID to file
        """ commented out because sometimes conflicts with chat function
        elif 'you' in tweet.text.lower() or ' opinionbotcs' in tweet.text.lower():
            sentimentTweet = textblob.TextBlob(tweet.text)
            if tweet.id in loggedID:
                print("skipping "+ str(tweet.id))
            else:
                if sentimentTweet.sentiment.polarity >= 0:
                    print("tweeting")
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " Thank you for your feedback!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    loggedID.append(tweet.id)
                elif sentimentTweet.sentiment.polarity < 0:
                    print("tweeting")
                    try:
                        api.update_status(status = "@" + tweet.user.screen_name + " That's just rude!", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    except:
                        print("API error when responding")
                    loggedID.append(tweet.id)"""
        if 'analyse' in tweet.text.lower():
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
                try:
                    api.update_status(status = "@" + tweet.user.screen_name + " The sentiment polarity of " + hashtag + " is: " + wordRating + "(" + str(rndPolarity) + ")" + " based on " + str(counter) + " samples", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                except:
                    print("API error when responding")
                # adds replied tweet ID to file
                loggedID.append(tweet.id)
        elif 'testing' in tweet.text.lower():
            if str(tweet.id) in str(loggedID):
                print("skipping " + str(tweet.id))
            else:
                # this is for checking and testing the TextBlob sentiment values with test data
                dataText = textblob.TextBlob(tweet.text)
                Polarity = round(dataText.sentiment.polarity, ndigits=3)
                wordRating = inWords(Polarity)
                try:
                    api.update_status(status = "@" + tweet.user.screen_name + " Your test tweet's polarity value is: " + str(Polarity) + "(" + wordRating + ")", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                except:
                    print("API error when responding")
                loggedID.append(tweet.id)
        elif 'chat' in tweet.text.lower():
            if str(tweet.id) in str(loggedID):
                print("skipping" + str(tweet.id))
            else:
                # cuts out the "@opinionbotcs" part of the tweet as it messes with the AI
                location = tweet.text.find("chat") + 4
                prompt = tweet.text[location:]
                # Uses an implemnetation module I made of the GPT Neo AI and passes in the tweet as the AI prompt
                response = GPTgenerator.generate(prompt, 140)
                response = GPTgenerator.generate(prompt, 140)
                # Responds with the text from the AI
                try:
                    api.update_status(status = "@" + tweet.user.screen_name + response, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                    print("tweeting")
                except:
                    print("API error when responding")
                loggedID.append(tweet.id)


while True:
    checkData()
    time.sleep(15)
    timeCount += 15
    # makes an AI generated tweet if it's been more than 12 hours since the last one
    if timeCount > 43200:
        # selects a random AI prompt from a list of many topics
        prompt = random.choice(prompts)
        dailyTweet = GPTgenerator.generate(prompt, 140)
        try: 
            api.update_status(status = dailyTweet)
            print("Tweeting daily tweet")
        except:
            print("API error when tweeting")
        timeCount = 0


"""
making notes on textblob sentiment analysis
the text to be analysed must be put into the textblob data structure using TextBlob(text)
using .tags we can see the words in a 2d array of token and sentiment tag. 
.sentences will break a textblob into sentence tokens
.words will break it into word tokens
using sentence.sentiment.polarity will output a value from -1 to 1 of the sentiment.
"""

