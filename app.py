import json
from twitch import TwitchClient
import csv
import pandas as pd
import datetime
import matplotlib.pyplot as plt 
import numpy as np 

#open config file
with open('config.json', 'r') as file:
    config = json.load(file)
#create variables with config file info
id_cliente = config['DEFAULT']['CLIENTE']
id_secreto = config['DEFAULT']['SECRETO']

client = TwitchClient(client_id=id_cliente, oauth_token=id_secreto)
games = client.games.get_top(10, 0)
'''
print(games[0]['game']['name'])
print(games[0]['viewers'])
print(games[0]['channels'])
'''
data_twitch = [] #empty
#loop for to scrape all the info
for i in games:
    name = i['game']['name']
    viewers = i['viewers']
    channels = i['channels']
    timestamp = datetime.datetime.now()
    #append all the info
    data_twitch.append([name, viewers, channels, timestamp])

#create dataframe
dataset = pd.DataFrame(data_twitch)
#changen column names
dataset.columns = ['GAME', 'VIEWERS', 'CHANNELS', 'TIMESTMAP']
#export the data
dataset.to_csv('twitch_data.csv', index = False) 

#print data
plt.figure(figsize=(15,15))
plt.bar(range(len(dataset['GAME'])), dataset['VIEWERS'])
plt.xlabel('games')
plt.ylabel('viewers')
ax = plt.subplot()
ax.set_xticks(range(len(dataset['GAME'])))
ax.set_xticklabels(dataset['GAME'], rotation = 15)
plt.legend(['Twitch'])
plt.show()