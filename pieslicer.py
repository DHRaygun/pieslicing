#
# Created by Jack Cairy
# First draft finished February 2022
# Contact at tech.jackc@gmail.com
# READ THE README.MD FILE FOR FULL INFORMATION
#

# from datetime import datetime
import random
from PIL import Image
from PIL import ImageDraw

file_name = input(r'Please enter complete file path to desired image: ')
file_output_path = input(r'Please enter where you would like image to output (ex. C:\Users\Jeff\Downloads\): ')
new_file_name = input(r'Please enter desired name of new file without extension (ex. jeff_image): ')
# insta_user = input('Please enter your Instagram username: ')
# insta_password = input('Please enter your Instagram password: ')
# user_cap = input('Please enter desired caption: ')

shape_cord_1 = random.randint(5, 250)
shape_cord_2 = random.randint(5, 250)
shape_cord_3 = random.randint(150, 400)
shape_cord_4 = random.randint(150, 400)
shape = ((shape_cord_1, shape_cord_2), (shape_cord_3, shape_cord_4))

start_ang = random.randint(3, 50)
end_ang = random.randint(50, 270)

rand_color_1 = random.randint(0, 255)
rand_color_2 = random.randint(0, 255)
rand_color_3 = random.randint(0, 255)
rand_outline_1 = random.randint(0, 255)
rand_outline_2 = random.randint(0, 255)
rand_outline_3 = random.randint(0, 255)

im = Image.open(file_name)

file_ext = im.format

im_r = im.resize((400, 400))
draw = ImageDraw.Draw(im_r)
draw.pieslice(shape, start=start_ang, end=end_ang, fill=(rand_color_1, rand_color_2, rand_color_3), outline=(rand_outline_1, rand_outline_2, rand_outline_3))
complete_output = file_output_path+new_file_name+'.'+file_ext
im_r.save(complete_output)

# Gets manual caption (in case of working Instagram posting feature)
# cap_manual = str(datetime), user_cap
