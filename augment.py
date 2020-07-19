from PIL import Image, ImageEnhance
import os

def augment_color(filepath):
    print('\n___________________________________________________________\n')
    print(f'Generating 10 color variants of image at: {filepath}')
    im = Image.open(filepath)
    enh = ImageEnhance.Color(im)

    for f in range(50, 100, 5):
        factor = f / 100
        destination = f'{filepath[:-4]}color{f}.jpg'
        enh.enhance(factor).save(destination)
        print(f'Saved to: {destination}')

    print('\n___________________________________________________________\n')

def augment_contrast(filepath):
    print('\n___________________________________________________________\n')
    print(f'Generating 10 contrast variants of image at: {filepath}')
    im = Image.open(filepath)
    enh = ImageEnhance.Contrast(im)

    for f in range(50, 100, 5):
        factor = f / 100
        destination = f'{filepath[:-4]}contrast{f}.jpg'
        enh.enhance(factor).save(destination)
        print(f'Saved to: {destination}')

    print('\n___________________________________________________________\n')

def augment_brightness(filepath):
    print('\n___________________________________________________________\n')
    print(f'Generating 10 brightness variants of image at: {filepath}')
    im = Image.open(filepath)
    enh = ImageEnhance.Brightness(im)

    for f in range(50, 100, 5):
        factor = f / 100
        destination = f'{filepath[:-4]}brightness{f}.jpg'
        enh.enhance(factor).save(destination)
        print(f'Saved to: {destination}')

    print('\n___________________________________________________________\n')
    
def augment_sharpness(filepath):
    print('\n___________________________________________________________\n')
    print(f'Generating 10 sharpness variants of image at: {filepath}')
    im = Image.open(filepath)
    enh = ImageEnhance.Sharpness(im)

    for f in range(60, 170, 10):
        factor = f / 100
        destination = f'{filepath[:-4]}sharpness{f}.jpg'
        enh.enhance(factor).save(destination)
        print(f'Saved to: {destination}')

    print('\n___________________________________________________________\n')
    
def augment_images(tube_set, tube_class):
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
    print(f'Augmenting {tube_set} images in class {tube_class}')
    target_directory = f'./test_tubes/{tube_set}/T_{tube_class}'

    for filename in os.listdir(target_directory):
        filepath = f'{target_directory}/{filename}'
        augment_color(filepath)
        augment_contrast(filepath)
        augment_brightness(filepath)
        augment_sharpness(filepath)
        
    print('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')
    
    
for tube in range(20, 21):
    print('Starting:\n')
    augment_images('test', tube)
    print('Done!\n')

for tube in range(2, 21):
    print('Starting:\n')
    augment_images('train', tube)
    print('Done!\n')

    
