# 导包
import pytesseract
from PIL import Image
# 打开图片得到图片实例
img = Image.open('../4.png')
# 对于数字chi_sim或者是默认英文都可以得到结果，但是
text = pytesseract.image_to_string(img)
print(text)