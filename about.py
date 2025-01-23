# 用来爬取about内容的脚本文件
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import pandas as pd
import json
import time

df = pd.read_excel("data_with_name.xlsx")
name_list = df['name'].tolist()

driver = webdriver.Chrome()

df_info = pd.DataFrame(columns=["website","pitch closing date","raised","pre-money valuation","equity offered","investors","link-website"])

def get_valuation_share_price(name):
    # 其实这个函数目前是用来登录的
    driver.get(f"https://europe.republic.com/login?r=%2Fbusinesses%2F{name}%2Fsections%2Fabout")
    time.sleep(1)
    user_input = driver.find_element(By.ID,"session_email")
    password_input = driver.find_element(By.ID,"session_password")
    username = "yiweichen211@gmail.com"
    password = "Hms123456@"
    user_input.send_keys(username)
    password_input.send_keys(password)
    print("user name and password")
    wait = WebDriverWait(driver, 10)
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    login_btn.click()
    print("login success")

def get_information_in_about_section(name):
    print(name)
    driver.get(f"https://europe.republic.com/businesses/{name}/sections/about")
    time.sleep(0.3)
    with open(f"about_html/{name}_about.html","w",encoding='utf-8') as f:
        f.write(driver.page_source)
    
def get_basic_about_information_from_html(name):
    with open(f"about_html/{name}_about.html", "r", encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="ListGroup-rowContent")
    for element in elements:
        divs = element.find_all("div")
        if len(divs) == 6:
            row_data = {}
            count = 1
            for div in divs:
                if count == 1:
                    row_data["website"] = f"https://europe.republic.com/businesses/{name}/sections/about"
                    row_data["pitch closing date"] = div.get_text().strip()
                elif count == 2:
                    row_data["raised"] = div.get_text().strip()
                elif count == 3:
                    row_data["pre-money valuation"] = div.get_text().strip()
                elif count == 4:
                    row_data["equity offered"] = div.get_text().strip()
                elif count == 5:
                    row_data["investors"] = div.get_text().strip()
                elif count == 6:
                    a_tag = div.find("a")
                    if a_tag and a_tag.get("href"):
                        row_data["link-website"] = "https://europe.republic.com" + str(a_tag.get("href"))
                        
                count += 1
            df_info.loc[len(df_info)] = row_data
            
get_valuation_share_price("revolut") # 基础的登录
    

# name_list = ["aurovine","audiopi","y1-sport"] # 调试用的list

for name in name_list:
    get_information_in_about_section(name)
    get_basic_about_information_from_html(name)
    print(len(df_info))
    
print(df_info)
df_info.to_excel("basic_about_info.xlsx", index=False)

# get_information_in_about_section("revolut")
# get_basic_about_information_from_html("revolut")

# get_information_in_about_section("stamp-free-limited")
# get_basic_about_information_from_html("stamp-free-limited")

# print(df_info)
