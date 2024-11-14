import json

with open('./data/oracle-cards.json', 'r', encoding='utf-8') as file:
    oracle = json.load(file)

keys = [
    'name',
    'cmc',
    'type_line',
    'oracle_text',
    'power',
    'toughness',
    'colors',
    'color_identity',
    'legalities',
    'reserved',
    'set',
    'set_name',
    'digital',
    'rarity',
    'flavor_text',
    'artist',
    'border_color'
]

creatures = []

for card in oracle:
    if  "Creature" in card['type_line'] and "Aura" not in card['type_line']:
        temp = []
        for key in keys:
            if key in card:
                temp.append(card[key])
        if 'image_uris' in card:
            temp.append(card['image_uris'])
        creatures.append(temp)


with open('./data/creatures.json', 'w', encoding='utf-8') as creature_json:
    json.dump(creatures, creature_json, indent=4)

print("Data written to creatures.json")