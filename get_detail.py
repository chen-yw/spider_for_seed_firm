# 用来爬取sheet3最细节的信息
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
import re

# driver = webdriver.Chrome()
df = pd.read_excel("basic_about_info.xlsx")

def remove_consecutive_empty_lines(text):
    # 使用正则表达式替换连续的空行
    cleaned_text = re.sub(r'\n\s*\n', '\n', text)
    return cleaned_text

def log_in(name):
    # 其实这个函数目前是用来登录的
    driver.get(f"https://europe.republic.com/login?r=%2F{name}%2Fsections%2Fteam")
    time.sleep(0.1)
    user_input = driver.find_element(By.ID,"session_email")
    password_input = driver.find_element(By.ID,"session_password")
    username = "yiweichen211@gmail.com"
    password = "Hms123456@"
    user_input.send_keys(username)
    password_input.send_keys(password)
    # print("user name and password")
    wait = WebDriverWait(driver, 10)
    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))
    login_btn.click()
    # print("login success")


def get_details(url):
    name = url.split("/")[-1]
    url = url + "/sections/team"
    print(name)
    print(url)
    try:
        # log_in(name) # 后来发现每一个都需要登录才保险
        driver.get(url)
        time.sleep(0.3)
        with open(f"final_detail_html/{name}.html","w",encoding='utf-8') as f:
            f.write(driver.page_source)
    except Exception as e:
        print(f"Error occurred while getting details for {name}: {str(e)}")
        

def get_team_member_info(url): 
    name = url.split("/")[-1]
    with open(f"final_detail_html/{name}.html","r",encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="entrepreneur_container")
    all_context = ""
    for element in elements:
        all_context += element.get_text().strip()
    # print(remove_consecutive_empty_lines(all_context))
    return remove_consecutive_empty_lines(all_context)
    
def get_investment_bar(url):
    name = url.split("/")[-1]
    with open(f"final_detail_html/{name}.html","r",encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="investment_total_bar_container")
    for element in elements:
        sub_div = element.find("div",class_="investment_total_percentage")
        print(sub_div.get_text().strip()) # 这个就已经是百分比了
        sub_div = element.find("div",class_="investment_total_target")
        print(sub_div.get_text().split("\n")[1]) # 这个的第一行应该是筹集资金的目标
        sub_div = element.find("div",class_="CampaignProgress-text")
        print(sub_div.get_text().split("\n")[1]) # 这个的第一行应该是实际筹集资金的金额
        print(sub_div.get_text().split("\n")[3]) # 这个的第二行应该是投资人数


def get_other_detail(url):
    name = url.split("/")[-1]
    with open(f"final_detail_html/{name}.html","r",encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="campaign_page_panel")
    element = elements[0]
    sub_div = element.find("tr",class_="tax-relief")
    if sub_div:
        sub_sub_div = sub_div.find("td")
        print(sub_sub_div.get_text().strip())
    sub_div = element.find("tr",class_="share-price")
    if sub_div:
        sub_sub_div = sub_div.find("td")
        print(sub_sub_div.get_text().strip())
    sub_div = element.find("td",class_="co-investor")
    print(sub_div.get_text().strip())
    
def get_highlights_and_key_features(url):
    name = url.split("/")[-1]
    with open(f"final_detail_html/{name}.html","r",encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="campaign_highlights_bullet_points")
    all_context = ""
    for element in elements:
        all_context += element.get_text().strip()
    print(remove_consecutive_empty_lines(all_context),"\n")
    all_context = ""
    elements = soup.find_all(class_="campaign_highlights_list")
    for element in elements:
        all_context += element.get_text().strip()
    print(remove_consecutive_empty_lines(all_context),"\n")
    
link_websites = df['link-website'].to_list()
    
def add_all_info_to_the_df(index):
    # 这个函数用来把所有的信息都加到df里面，传入的参数是对应的列表的行
    url = df.loc[index,"link-website"]
    name = url.split("/")[-1]
    print(url)
    df.loc[index,"team"] = get_team_member_info(url)
    with open(f"final_detail_html/{name}.html","r",encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(class_="campaign_page_panel")
    if len(elements) != 0:
        element = elements[0]
        sub_div = element.find("tr",class_="share-price")
        if sub_div:
            sub_sub_div = sub_div.find("td")
            if sub_sub_div:
                df.loc[index,"share-price"] = sub_sub_div.get_text().strip()
        sub_div = element.find("tr",class_="tax-relief")
        if sub_div:
            sub_sub_div = sub_div.find("td")
            if sub_sub_div:
                df.loc[index,"tax-relief"] = sub_sub_div.get_text().strip()
        sub_div = element.find("td",class_="co-investor")
        if sub_div:
            df.loc[index,"co-investor"] = sub_div.get_text().strip()
    
    elements = soup.find_all(class_="investment_total_bar_container")
    for element in elements:
        sub_div = element.find("div",class_="investment_total_percentage")
        # print(sub_div.get_text().strip()) # 这个就已经是百分比了
        if sub_div:
            try:
                df.loc[index,"Subscribed Percentage"] = sub_div.get_text().strip()
            except:
                pass
        sub_div = element.find("div",class_="investment_total_target")
        # print(sub_div.get_text().split("\n")[1]) # 这个的第一行应该是筹集资金的目标
        if sub_div:
            try:
                df.loc[index,"Target"] = sub_div.get_text().split("\n")[1]
            except:
                pass
        sub_div = element.find("div",class_="CampaignProgress-text")
        # print(sub_div.get_text().split("\n")[1]) # 这个的第一行应该是实际筹集资金的金额
        if sub_div:
            try:
                df.loc[index,"Subscribed"] = sub_div.get_text().split("\n")[1]
            except:
                pass
        # print(sub_div.get_text().split("\n")[3]) # 这个的第二行应该是投资人数
        if sub_div:
            try:
                df.loc[index,"Investor Number"] = sub_div.get_text().split("\n")[3]
            except:
                pass
    elements = soup.find_all(class_="campaign_highlights_bullet_points")
    all_context = ""
    for element in elements:
        all_context += element.get_text().strip()
    df.loc[index,"business highlights"] = remove_consecutive_empty_lines(all_context)
    all_context = ""
    elements = soup.find_all(class_="campaign_highlights_list")
    for element in elements:
        all_context += element.get_text().strip()
    df.loc[index,"key features"] = remove_consecutive_empty_lines(all_context)
        
for i in range(len(df)):
    add_all_info_to_the_df(i)

print(df)
df.to_excel("final_version_data.xlsx",index=False)
    
