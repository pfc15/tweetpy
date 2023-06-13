import tweepy
import pandas as pd
import csv
import variaveis.py



auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret,
   access_token, access_token_secret
)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
    # print(tweet.text)

tabela = pd.read_excel('jogadores.xlsx')

teste = tabela[tabela["jogador"] == "TitaN"]['twitter'].values
print(teste)
teste = teste[0][1:]
print(type(teste))
print(teste)
teste = api.get_user(screen_name='titannlol1')
tweets = []
timeline = api.user_timeline(user_id=teste.id)
for e in timeline:
    print(e.text)
print(len(timeline))
ultimo = timeline[-1]
while len(timeline)!=0:
    timeline = api.user_timeline(user_id=teste.id, max_id=ultimo)
    for e in timeline:
        print(e.text)
    print(len(timeline))
    tweets += timeline
with open('tweet_titan', w) as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow()
