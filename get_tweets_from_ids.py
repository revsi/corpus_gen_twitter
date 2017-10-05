import twython                  

consumerKey_1='kcNt0fserbldYypDpB30XM6Ce'
consumerSecret_1='klCiCzuJlRlvDQrUagiuSw1HaUgF1NYhqZk8SYsEUtvcBZ5iry'
token_1='3012016202-W6xdRhbXaU1jXU7X2OI7NRIzciKzFI3HBO0312p'
tokenSecret_1='PqZbSBS9ZoVvIvGPbwqtRJS9Y3hOs7z2NGFLJg8c5dAMt'

consumerKey_2='8er3QRpLi3NNDpIqMDPdpCQap'
consumerSecret_2='bEZ7IeluaB1AyztFdYjiCvxO6VFrOu2xt8gTarcldqzFteFWki'
token_2='3012016202-jgL5I2epFueI0iX1nknmndWHyHuZxNyr5qg017G'
tokenSecret_2='EXvNd1024BwLWellLzOchZhOCf55HoE2txg0QvXr3FWcH'

consumerKey_3='xgRxSH2oS55V96dlfmyke14Ex'
consumerSecret_3='BHT6R608D8fZlNEhmzVVxaPPy5iS9LKUsaTZXfwNp6N6AQGmjX'
token_3='3012016202-Bcs4IGJYSMvBAShm7x6q9tOZfPfVgdoVpGQ6uel'
tokenSecret_3='QaXI4oRn1HncW1GwOtQTenRDHEvey1nZWonmfEiofCGUp'

consumerKey_4='B4vdZ8exUKFINOelJ4Gc36qUt'
consumerSecret_4='1PGDmmI0oVyWBXmUKh5ngoXVNSSkZ2OYaJK9YtrU8PnzbUNTdW'
token_4='3012016202-BOy4hvNpfxkkTjSVsQANyCAiDgGblDkTGk7CgmC'
tokenSecret_4='BlqIGbk44EtTfemyPteitH6sPrURq5EtS8G8SIMxFts1m'

def get_twython(c):
	if c==0:
		return twython.Twython(consumerKey_1, consumerSecret_1, token_1, tokenSecret_1)
	elif c==1:
		return twython.Twython(consumerKey_2, consumerSecret_2, token_2, tokenSecret_2)
	elif c==2:
		return twython.Twython(consumerKey_3, consumerSecret_3, token_3, tokenSecret_3)
	else:
		return twython.Twython(consumerKey_4, consumerSecret_4, token_4, tokenSecret_4)


id_file = open('hindi_data.ids', 'r')

data_file = open('hindi_data.txt', 'w')

c = 0
twitter = get_twython(c)
for i in id_file:
	try:
		tweet = twitter.show_status(id=int(i))
	except Exception as e:
		if e.error_code == 404 or e.error_code == 403:
			continue
		c = (c+1)%4
		twitter = get_twython(c)
		tweet = twitter.show_status(id=int(i))
	tweet = tweet['text']
	print(tweet.replace('\n', ' '), file=data_file)
id_file.close()
data_file.close()


