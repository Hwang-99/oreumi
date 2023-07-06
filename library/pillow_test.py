from PIL import Image
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img = Image.open(current_dir +'/dochi.jpg', mode = 'r')#이미지 열어서 객체에 저장하기

img.show()

