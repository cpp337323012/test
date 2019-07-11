# encoding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'E:\webdriver\chromedriver.exe')
url = 'http://xyq.163.com/2011/zhuanyi/search.html'
driver.get(url)
driver.implicitly_wait(3)
driver.maximize_window()

current_region = driver.find_element_by_id('region')

# 选择value值为江苏1区的选项
Select(current_region).select_by_value("江苏1区")
time.sleep(1)


# 选择Value值为雨花台的选项
current_server = driver.find_element_by_id('server')
Select(current_server).select_by_value("雨花台")
time.sleep(1)

# 点击查询
current_search = driver.find_element_by_id('search_server').click()
time.sleep(1)
# 查询结果获取

server_search = driver.find_elements_by_class_name('rs-td')
'''
选择服务器对象通过by_class_name定位当前所有的服务器，循环定位到的列表加入新的列表中打印出来
'''
servername = []
for i in server_search:
   name =  i.find_element_by_tag_name('b').text
   servername.append(name)

print(servername)

# 判断是否有预期
if u'水泊梁山' in servername:
    print(u'可以回家了')
else:
    print(u'不行还要再等等')

driver.quit()

