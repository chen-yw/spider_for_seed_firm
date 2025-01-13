from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import random
import time

website_df = pd.read_csv("website.csv")
website_list = website_df["website"].tolist()

def get_html(url,number = 0):
    print(number,url)
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(1+random.randint(0,2))  # 等待1到3秒，来防止被检测
        page_source = driver.page_source
        with open(f"raw_html/file_{number}.html", "w",encoding='utf-8') as f:
            f.write(page_source)
        f.close()    
    except Exception as e:
        print(f"Error occurred while accessing {url}: {str(e)}")
    finally:
        driver.quit()

for i in range(58,len(website_list)):
    get_html(website_list[i],i+1)
    time.sleep(0.5)
    
    
