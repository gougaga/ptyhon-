# 导包
import pytesseract
from PIL import Image
# 读取图片 得到图片实例
img = Image.open('c.png')
# 使用pytesseract库提取文本信息
# long='chi_sim'简体中文, long='chi_tra'繁体中文
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)