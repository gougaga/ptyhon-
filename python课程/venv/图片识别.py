import pytesseract
from PIL import Image
# 打开图片mode可以忽略，如果要给 mode="r"
# 将图像文件转化为实例
img = Image.open('2.png')
# 识别英文
# 得到图像中的英文进行输出
info = pytesseract.image_to_string(img,lang="eng",config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
print(info)