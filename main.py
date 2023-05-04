import requests
import json

heroes_list = ['Hulk', 'Captain America', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain America,': 0, 'Thanos': 0}
url = ''https://www.superheroapi.com/api.php/______________/search/'

for hero in heroes_list:
    hero_dict = json.loads(requests.get(url + hero).content)
    intelligence_dict[hero] = int(hero_dict['results'][0]['powerstats']['intelligence'])
    print(intelligence_dict)