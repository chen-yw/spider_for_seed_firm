from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置Chrome选项以使用现有的用户数据目录
options = webdriver.ChromeOptions()

# 初始化浏览器
driver = webdriver.Chrome(options=options)

# 打开目标网站
# https://europe.republic.com/login?r=%2Fbusinesses%2Frevolut%2Fsections%2Fmarket
driver.get("https://europe.republic.com/login?r=%2Fbusinesses%2Frevolut%2Fsections%2Fmarket")
# driver.get("https://europe.republic.com/businesses/revolut/sections/market")
# driver.get("https://europe.republic.com/businesses/republic/sections/market")

# 等待页面加载并通过验证
time.sleep(1)  # 根据需要调整等待时间

# 获取页面标题
page_title = driver.title

# 获取页面的完整HTML内容
page_source = driver.page_source

with open("final.html", "w",encoding='utf-8') as f:
    f.write(page_source)
    
time.sleep(10)
# id="session_email"
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

time.sleep(1)

page_source = driver.page_source

with open("final_1.html", "w",encoding='utf-8') as f:
    f.write(page_source)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
    pass

# 关闭浏览器
driver.quit()