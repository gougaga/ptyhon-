from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
#正常启动谷歌浏览
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 关闭浏览器
# browser.close()
# browser.quit()
# print(browser.page_source)
print(type(browser.page_source))   # response.text
# 设置浏览器界面大小
# browser.set_window_size(480, 800)
# 浏览器最大化
browser.maximize_window()
# 浏览器最小化
# browser.minimize_window()
# 浏览器设置窗口大小
# browser.set_window_size(480, 800) 宽480 高800
# 浏览器后退
# browser.back()
#浏览器前进
# browser.forward()

# headless无界面浏览器模式

chrome_options = webdriver.ChromeOptions()
# # 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless') # 增加无界面选项
# chrome_options.add_argument('--disable-gpu') # 谷歌禁用GPU加速 如果不加这个选项，有时定位会出现问题

#
# # 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
mainUrl = "http://www.baidu.com/"
browser.get(mainUrl)
print(browser.page_source)
browser.quit()
#找到搜索框，搜索python
browser.find_element_by_id('kw').send_keys(u'python')
browser.find_element_by_xpath('//input[@id="kw"]').send_keys('河南艺术职业学研')
# # 点击搜索
browser.find_element_by_id('su').click()
# time.sleep(1)
# #清空搜索框内容
# browser.find_element_by_id('kw').clear()
# browser.find_element_by_id('kw').send_keys(u'mysql')
# # 点击搜索
# browser.find_element_by_id('su').click()
# #也可定位搜索按钮，通过 enter（回车）代替 click()
# browser.find_element_by_id("su").send_keys(Keys.ENTER)
# res = browser.page_source
# # print(res)
# a = browser.find_element_by_xpath('//input[@id="su"]')
# href = a.get_attribute('value')
# b = browser.find_element_by_xpath('//title').text
# time.sleep(3)
#
# print(href)
# print(b)
# browser.close()