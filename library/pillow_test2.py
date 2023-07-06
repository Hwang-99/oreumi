from PIL import Image, ImageFilter
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img = Image.open(current_dir +'/dochi.jpg', mode = 'r')#이미지 열어서 객체에 저장하기
img.show()#이미지뷰어로 열어보기
print(img.size)

cropped_img = img.crop((10, 10, 200, 200))
cropped_img.save(current_dir + 'cropped_test.jpg')
cropped_img.show()

blur_test = img.filter(ImageFilter.BLUR) # 이미지를 흐리게 필터링 BLUR
blur_test.save(current_dir + 'blur_test.jpg')
blur_test.show()

contour_test = img.filter(ImageFilter.CONTOUR)
contour_test.save(current_dir + 'contour_test.jpg')
contour_test.show()