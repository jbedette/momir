import json

def extract_creatures():
    keys = [
        'name',
        'cmc',
        'mana_cost',
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

    with open('./data/oracle-cards.json', 'r', encoding='utf-8') as file:
        oracle = json.load(file)

    for card in oracle:
        if  "Creature" in card['type_line'] and "Aura" not in card['type_line']:
            temp = {}
            for key in keys:
                if key in card:
                    temp[key] = card[key]
            if 'image_uris' in card:
                temp['image_uris'] = card['image_uris']
            creatures.append(temp)

    with open('./data/creatures.json', 'w', encoding='utf-8') as creature_json:
        json.dump(creatures, creature_json, indent=4)

    print("Data written to creatures.json")


def momir_creatures_by_cmc():
    keys = [
        'name',
        'cmc',
        'mana_cost',
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

    creatures = {i: [] for i in range(17)}

    with open('./data/oracle-cards.json', 'r', encoding='utf-8') as file:
        oracle = json.load(file)

    for card in oracle:
        if  "Creature" in card['type_line'] and "Aura" not in card['type_line'] and "Token" not in card['type_line']:
            temp = {}
            for key in keys:
                if key in card:
                    temp[key] = card[key]
            if 'image_uris' in card:
                temp['image_uris'] = card['image_uris']
            creatures[int(temp['cmc'])].append(temp)
    with open('./data/momir.json', 'w', encoding='utf-8') as creature_json:
        json.dump(creatures, creature_json, indent=4)

    print("Data written to momir.json")

if __name__ == '__main__':
    momir_creatures_by_cmc()