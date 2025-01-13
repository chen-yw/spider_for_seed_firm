from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化浏览器
driver = webdriver.Chrome()

# 打开目标网站
# driver.get("https://europe.republic.com/businesses/revolut/sections/market")
driver.get("https://europe.republic.com/businesses/republic/sections/market")

# 等待页面加载并通过验证
time.sleep(10)  # 根据需要调整等待时间

# 获取页面标题并打印
page_title = driver.title
# print("Page Title:", page_title)

# 获取页面的完整HTML内容并打印
page_source = driver.page_source
# print("Page Source:", page_source)

with open("file.html", "w",encoding='utf-8') as f:
    f.write(page_source)
    
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    pass

# 关闭浏览器
driver.quit()