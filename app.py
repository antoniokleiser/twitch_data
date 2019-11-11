import json
from twitch import TwitchClient

with open('config.json', 'r') as file:
    config = json.load(file)

id_cliente = config['DEFAULT']['CLIENTE']
id_secreto = config['DEFAULT']['SECRETO']

client = TwitchClient(client_id=id_cliente, oauth_token=id_secreto)
games = client.games.get_top(10,0)
print(games)
