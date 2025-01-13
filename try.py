from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome()
driver.get("https://europe.republic.com/businesses/revolut/sections/about")


page_source = driver.page_source
print(page_source)

with open(f"heml_file_tmp.html", "w",encoding='utf-8') as f:
    f.write(page_source)

# 关闭浏览器
driver.quit()
