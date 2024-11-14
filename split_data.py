import json

with open('oracle-cards.json', 'r', encoding='utf-8') as file:
    oracle = json.load(file)

creatures = []

for card in oracle:
    if card['type_line'] == "Creature":
        creatures.append(card)

with open('creatures.json', 'w', encoding='utf-8') as creature_json:
    json.dump(creatures, creature_json, indent=4)

print("Data written to creatures.json")
