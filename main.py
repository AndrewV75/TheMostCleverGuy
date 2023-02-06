''' Кто самый умный супергерой? Есть API по информации о супергероях
https://akabab.github.io/superhero-api/api/ с информацией по всем супергероям.
Нужно определить кто самый умный (intelligence) из трех супергероев-
Hulk, Captain America, Thanos.'''

import requests
from pprint import pprint

superheroes = ['Hulk', 'Captain America', 'Thanos']
url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url=url)
best_heroes = {}

def intelligence(superheroes):
  for hero in response.json():
    if hero['name'] in superheroes:
      values = hero['powerstats']
      intelligence_score = values.get('intelligence')
      best_heroes[hero['name']] = intelligence_score
  return best_heroes

new_heroes = intelligence(superheroes)
# pprint(best_heroes)
# pprint(new_heroes)
print(f'Самый умный: {max(new_heroes, key = new_heroes.get)}')