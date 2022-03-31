import requests

url = "https://superheroapi.com/api/2619421814940190/search/"
params = [{'name': 'Captain America'}, {'name': 'Hulk'}, {'name': 'Thanos'}]

for hero in params:
    heroes = requests.get(url + hero['name'])
    hero['intelligence'] = int(heroes.json()['results'][0]['powerstats']['intelligence'])

hero_name = sorted(params, key=lambda hero: -hero['intelligence'])[0]['name']
print(f'Самый умный супергерой: {hero_name}')
