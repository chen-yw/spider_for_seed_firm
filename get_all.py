from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import json
import time

df = pd.read_excel("data_with_name.xlsx")

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

share_prices = {}

def get_valuation_share_price(name):
    driver.get(f"https://europe.republic.com/login?r=%2Fbusinesses%2F{name}%2Fsections%2Fmarket")
    time.sleep(1)
    with open("final.html","w",encoding='utf-8') as f:
        f.write(driver.page_source)
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
    
    with open(f"{name}.html", "w",encoding='utf-8') as f:
        f.write(driver.page_source)
    # time.sleep(50)

def get_valuation_share_price_without_log_in(i,name):
    print(i,name)
    driver.get(f"https://europe.republic.com/businesses/{name}/sections/market")
    time.sleep(0.5)
    
    try:
        last_price_element = driver.find_element(By.CLASS_NAME, "last-price")
        last_price_text = last_price_element.text
        share_prices[name] = last_price_text
        print(f"Share price for {name}: {last_price_text}")
    except Exception as e:
        print(f"Error occurred while getting share price for {name}: {str(e)}")
        
    
    with open(f"final_html/{name}.html","w",encoding='utf-8') as f:
        f.write(driver.page_source)
    
    
get_valuation_share_price("revolut")
# get_valuation_share_price_without_log_in(1,"revolut")
# for i in range(1, len(df)):
#     name = df.loc[i, 'name']
#     print(i,name)
#     get_valuation_share_price_without_log_in(name)

# 548
# 从125行开始，用多线程快速执行
with ThreadPoolExecutor(max_workers=1) as executor:  # 根据需要调整max_workers的数量
    futures = [executor.submit(get_valuation_share_price_without_log_in,i, df.loc[i, 'name']) for i in range(548,len(df),1)]

# 等待所有任务完成
for future in futures:
    future.result()

print("所有任务已完成")

# with open("price.json",'w',encoding='utf-8') as f:
#     json.dump(share_prices,f,ensure_ascii = False,indent = 4)



