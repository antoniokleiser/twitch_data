import datetime
from twitch import TwitchClient
import json

class Data:
    def datos(self):
        #open config file
        with open('config.json', 'r') as file:
            config = json.load(file)
        #create variables with config file info
        id_cliente = config['DEFAULT']['CLIENTE']
        id_secreto = config['DEFAULT']['SECRETO']
        client = TwitchClient(client_id=id_cliente, oauth_token=id_secreto)
        games = client.games.get_top(100, 0)
        data_twitch = [] #empty
        #loop for to scrape all the info
        for i in games:
            name = i['game']['name']
            viewers = i['viewers']
            channels = i['channels']
            timestamp = datetime.datetime.now()
            #append all the info
            data_twitch.append([name, viewers, channels, timestamp])

e = Data()