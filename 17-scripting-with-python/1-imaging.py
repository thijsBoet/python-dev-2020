from PIL import Image, ImageFilter
# Image         => https://pillow.readthedocs.io/en/stable/reference/Image.html
# ImageFilter   => https://pillow.readthedocs.io/en/stable/reference/ImageFilter.html

# creates image object in memory
img = Image.open('./img/pikachu.jpg')

print(img.format)
print(img.size)
print(img.mode)

# use dir to get all possible methods on img
print(dir(img))

img = Image.open('./img/pikachu.jpg')
# Pillow has a filter function
filtered_img = img.filter(ImageFilter.BLUR)
# convert image to B&W images
filtered_img = img.convert('L')
# rotate images a certain amount of degrees
filtered_img.rotate(90)
# resize using a tuple
filtered_img.resize((300, 300))
# save them to a specific name and format
filtered_img.save('blurred-rotated-grey-pikachu.png', 'png')
filtered_img.show()

astro = Image.open('./img/astro.jpg')
print(astro.size)
# new_img = astro.resize((300, 300))
astro.thumbnail((400,400))
# tumbnail method keeps aspect ratio
print(astro.size)
astro.save('thumbnail.jpg')
astro.show()

import sys, os
from PIL import Image

def convert_to_png(image_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(image_folder):
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}{clean_name}.png', 'png')

convert_to_png('img', 'png')