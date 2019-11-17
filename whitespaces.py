from PIL import Image, ImageChops
import PIL
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
# import os utilities
import os

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter
def trim(im):
  # for each image in the current directory
  
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    



for (image, i) in zip(os.listdir(os.getcwd()), range(len(os.listdir(os.getcwd())))):
    im = Image.open(image)
    print(im)
    im = trim(im)
    if im:
        im.save("/Users/shivamralli/Desktop/Competitions/KCP/data/Want to find/Images/unnatural_death_images/cleaned/cleaned_data"+str(i)+".png")