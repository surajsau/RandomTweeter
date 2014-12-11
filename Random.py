from random import randrange
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

num1 = str(randrange(-250000, 250000))
num2 = str(randrange(0, 500000))

operator = randrange(0, 4)

if operator == 0:
    operator = '+'
elif operator == 1:
    operator = '-'
elif operator == 2:
    operator = '*'
elif operator == 3:
    operator = '/'

result = str(eval(num1 + operator + num2))

tweet = 'Did you know that : ' + num1 + ' ' + operator + ' ' + num2 + ' = ' + result + ' #random #calculation'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status(tweet)

