import json
import get_images
import create_card_image
import random
import print


def momir_get_creature(cmc, creatures):
    creature = (random.sample(creatures[cmc],1))[0]
    creature['img'] = get_images.download_cropped_image(creature['image_uris']['art_crop'], creature['name'], delay=0.10)
    return creature

# def get_creature(name,momir,debug):
#     for cmcs in momir:
#         for creatures in cmcs:
#             for creature in creatures:
#                 print(creature)
#             # if(creature['name'] == name):
#             #     creature['img'] = get_images.download_cropped_image(creature['image_uris']['art_crop'], creature['name'], delay=0.10)
#             #     if(debug == True):
#             #         with open('./data/debug.json', 'w', encoding='utf-8') as creature_json:
#             #             json.dump(creature, creature_json, indent=4)
#             #     return creature

def gui_momir(cmc):
    with open('./data/momir.json', 'r', encoding='utf-8') as file:
        momir = json.load(file)
    
    creature = momir_get_creature(str(cmc),momir)
    file_name = create_card_image.create_card_image(creature, output_dest="./images/")
    # print.print_file(file_name)
    return file_name

if __name__ == '__main__':
    with open('./data/momir.json', 'r', encoding='utf-8') as file:
        momir = json.load(file)
    

    # test_targs = ['1','2','3','4']
    test_targs = ['10','10','10','10','10']
    # test_targs = ['15']
    for targ in test_targs:
        creature = momir_get_creature(targ,momir)
        creature = create_card_image.create_card_image(creature, output_dest="./images/")
        # creature.show()

    # creature = get_creature("Reaper King",momir,True)
    # creature = create_card_image.create_card_image(creature)
    # creature.show()






