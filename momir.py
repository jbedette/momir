import json
import get_images
import create_card_image
import random


def momir_get_creature(cmc, creatures):
    creature = (random.sample(creatures[cmc],1))[0]
    print(json.dumps(creature,indent=4))
    # print(f"{creature["image_uris"]}")
    creature['img'] = get_images.download_cropped_image(creature['image_uris']['art_crop'], creature['name'], delay=0.10)
    return creature

if __name__ == '__main__':
    with open('./data/momir.json', 'r', encoding='utf-8') as file:
        momir = json.load(file)
    
    # print(momir['0'])

    # test_targs = ['1','2','3','4']
    test_targs = ['2']
    for targ in test_targs:
        creature = momir_get_creature(targ,momir)
        creature = create_card_image.create_card_image(creature)






