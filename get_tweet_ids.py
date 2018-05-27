from twitterscraper import query_tweets
from frequent_words import *
from all_emojis import *


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
emoji_file = open('./hindi_data.label', 'w')
data_file = open('./hindi_data_new.ids', 'w')
threshold = 150
saved_tweets_id = {}
count = 0
word_set = code_mixed_words
total_iterations = len(word_set)*len(emojis)
iterations = 0
for emoji in emojis:
	for query_word in word_set:
		query = ' '.join([query_word, emoji])
		iterations += 1
		for tweet in query_tweets(query, threshold)[:threshold]:
			if tweet.id not in saved_tweets_id:
				print(tweet.id, file=data_file)
				print(emojis[emoji], file=emoji_file)
				saved_tweets_id[tweet.id] = 1
				count += 1
		print('{} tweet ids saved. => {:.2f} % completed'.format(count, (iterations/total_iterations)*100.0))
emoji_file.close()
data_file.close()
			