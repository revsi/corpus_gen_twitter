from twitterscraper import query_tweets
import re
from frequent_words import *
from all_emojis import *
def clean_tweet(tweet_string):
	tweet_string = tweet_string.replace('\n',' ').strip()
	return ' '.join(re.sub("(@[A-Z_a-z0-9]+)|([https:/]*[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}([-a-zA-Z0-9@:%_\+.~#?&//=]*))"," ",tweet_string).split())
	#@[_A-Za-z0-9]+
	# capture usernames
	#[https://]*[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)
	# capture ursl and emails

# emojis = {'❤':0,
# 			'😍':1,
# 			'😂':2,
# 			'💕':3,
# 			'🔥':4,
# 			'😊':5,
# 			'😎':6,
# 			'✨':7,
# 			'💙':8,
# 			'😘':9,
# 			'📷':10,
# 			'☀':12,
# 			'💜':13,
# 			'😉':14,
# 			'💯':15,
# 			'😁':16,
# 			'🎄':17,
# 			'📸':18,
# 			'😜':19,}


query = ''
# emoji_file = open('./hindi_data.label', 'w')
data_file = open('./hindi_data.txt', 'w')
saved_tweets_id = {}
saved_tweets_string = {}
count = 0
word_set = hindi_words
total_iterations = len(word_set)*len(emojis)
iterations = 0
for emoji in emojis:
	for query_words in word_set:
		query = ' '.join([query_words, emoji])
		iterations += 1
		for tweet in query_tweets(query, 500)[:500]:
			tweet_text = clean_tweet(tweet.text)
			if tweet.id not in saved_tweets_id and (len(tweet_text)>50 and tweet_text[:50] not in saved_tweets_string):
				print(tweet_text, file=data_file)
				# print(emojis[emoji], file=emoji_file)
				saved_tweets_id[tweet.id] = 1
				saved_tweets_string[tweet_text[:50]] = 1
				count += 1
		print('{} tweets saved. => {:.2f} % completed'.format(count, (iterations/total_iterations)*100.0))
# emoji_file.close()
data_file.close()
			