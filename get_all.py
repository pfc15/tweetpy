import tweepy
from tweepy import Cursor
import pandas as pd
from pandas_ods_reader import read_ods
import csv
import json
import variaveis.py




auth = tweepy.OAuth1UserHandler(
   api_key, api_key_secret
)
api = tweepy.API(auth)


# pegando a tabela
df_cblol = read_ods("stats.ods", "teste")
df_lec = read_ods("stats.ods", "CBLOL")
tweets = []
for arroba in df_cblol['twitter']:
    print(arroba)
    user = api.get_user(screen_name=arroba)
    cont=0
    for status in Cursor(api.user_timeline, id=arroba).items():
        print(arroba)
        print(cont)
        print(status.text)
        print('-='*20)
        tweets.append(status._json)
        print(type(status._json))
        if '2022' in status._json['created_at']:
            break
        
        cont +=1

    
print(type(tweets[0]))
keys = list(tweets[0].keys()) + ['quoted_status_id', 'quoted_status', 'quoted_status_id_str', 'possibly_sensitive','extended_entities', 'retweeted_status']
with open('faltou.csv', "w") as csvfile:
    dictwriter = csv.DictWriter(csvfile, keys)
    dictwriter.writeheader()
    for t in tweets:
        dictwriter.writerow(t)
