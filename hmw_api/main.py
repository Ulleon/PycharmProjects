import requests


def get_superhero_intelligence(superhero_name):
    all_heroes_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes = requests.get(all_heroes_url).json()
    for item in all_heroes:
        if item['name'].lower() == superhero_name.lower():
            return item['powerstats']['intelligence']


superheroes = ['hulk', 'captain america', 'thanos']
intelligences = []

for superhero in superheroes:
    intelligence = get_superhero_intelligence(superhero)
    intelligences.append(intelligence)

max_intelligence = max(intelligences)
most_intelligent_superhero = superheroes[intelligences.index(max_intelligence)]

print(f"Самый умный супергерой: {most_intelligent_superhero}")
