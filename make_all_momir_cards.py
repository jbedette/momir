import json
import get_images
import create_card_image

def momir_get_creature(cmc, creatures):
    for creature in creatures[cmc]:
        if 'image_uris' in creature:
            creature['img'] = get_images.download_cropped_image(creature['image_uris']['art_crop'], creature['name'], delay=0.10)
            creature = create_card_image.create_card_image(creature, output_dest="./momir_images/")


if __name__ == '__main__':
    with open('./data/momir.json', 'r', encoding='utf-8') as file:
        momir = json.load(file)
    
    targs = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
    for targ in targs:
        momir_get_creature(targ,momir)






