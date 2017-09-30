from twitterscraper import query_tweets
import re
from frequent_words import *

def clean_tweet(tweet_string):
	tweet_string = tweet_string.replace('\n',' ').strip()
	return ' '.join(re.sub("(@[A-Z_a-z0-9]+)|([https:/]*[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*))"," ",tweet_string).split())
	#@[_A-Za-z0-9]+
	# capture usernames
	#[https://]*[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)
	# capture ursl and emails

data_file = open('./telugu_data.text', 'w')
saved_tweets_id = {}
saved_tweets_string = {}
count = 0
word_set = telugu_words
total_iterations = len(word_set)
iterations = 0
for query in word_set:
	iterations += 1
	for tweet in query_tweets(query, 200)[:200]:
		tweet_text = clean_tweet(tweet.text)
		if tweet.id not in saved_tweets_id and (len(tweet_text)>70 and tweet_text[:70] not in saved_tweets_string):
			print(tweet_text, file=data_file)
			saved_tweets_id[tweet.id] = 1
			saved_tweets_string[tweet_text[:70]] = 1
			count += 1
	print('{} tweets saved. => {:.2f} % completed'.format(count, (iterations/total_iterations)*100.0))
data_file.close()
			