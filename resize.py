import os
from PIL import Image

# folder of the images
folder_path = './images'
#folder to save the new images
folder_path_images_new_resolution = './images-with-new-resolution'

# Add the new resolution
new_width = 1280
new_height = 800

for filename in os.listdir(folder_path):
        #Images extention
    if filename.endswith('.png') or filename.endswith('.jpg'):
        # Open image
        img = Image.open(os.path.join(folder_path, filename))
        # Change resolution
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        # Save image with the new resolution
        img.save(os.path.join(folder_path_images_new_resolution, filename))
