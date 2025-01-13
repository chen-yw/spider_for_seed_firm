from bs4 import BeautifulSoup

# 读取本地HTML文件
with open("raw_html/file_1.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, "lxml")
tr_elements = soup.find_all("tr")

# 找到class为'location'的<tr>元素并获取其中的文字内容
location_info = soup.find_all("tr", class_="location")
for location in location_info:
    td_elements = location.find_all("td")
    for td in td_elements:
        print(td.get_text())

# 找到class为'website'并且具有title的<a>元素
website_links = soup.find_all("a", class_="website",title = True)
for link in website_links:
    print(link.get_text())
    
# 找到class为'sectors'的<tr>元素并获取其中的文字内容
sectors_info = soup.find_all("tr", class_="sectors")
for sector in sectors_info:
    sector_detail = sector.find_all("span")
    for detail in sector_detail:
        print(detail.get_text())
    
# 找到文本信息包含'Incorporation date'的<tr>元素
incorporation_date_trs = [tr for tr in tr_elements if "Incorporation date" in tr.get_text()]
for tr in incorporation_date_trs:
    date_info = tr.find_all("td")
    for info in date_info:
        print(info.get_text())

# 找到文本信息包含Indicative valuation的tr元素
valuation_trs = [tr for tr in tr_elements if "Indicative valuation" in tr.get_text()]
for tr in valuation_trs:
    valuation_info = tr.find_all("td")
    for info in valuation_info:
        print(info.get_text())

# 找到文本信息包含'Change (%)'的<tr>元素
change_trs = [tr for tr in tr_elements if "Change (%)" in tr.get_text()]
for tr in change_trs:
    change_info = tr.find_all("span")
    for info in change_info:
        print(info.get_text())
        
# Valuation share price还没有搞定
print("Valuation share price还没有搞定")

# Total raised
total_raised_trs = [tr for tr in tr_elements if "Total raised" in tr.get_text()]
for tr in total_raised_trs:
    total_raised_info = tr.find_all("td")
    for info in total_raised_info:
        print(info.get_text())

# Total investors
total_indvestors_trs = [tr for tr in tr_elements if "Total investors" in tr.get_text()]
for tr in total_indvestors_trs:
    total_investors_info = tr.find_all("td")
    for info in total_investors_info:
        print(info.get_text())
        
# Eligibility status
eligibility_status_trs = [tr for tr in tr_elements if "Eligibility status" in tr.get_text()]
for tr in eligibility_status_trs:
    eligibility_status_info = tr.find_all("td")
    for info in eligibility_status_info:
        lines = info.get_text().split("\n")
        for line in lines:
            stripped_line = line.strip()
            if stripped_line:
                print(stripped_line)
                break

# Available shares
available_shares_trs = [tr for tr in tr_elements if "Available shares" in tr.get_text()]
for tr in available_shares_trs:
    available_shares_trs_info = tr.find_all("td")
    for info in available_shares_trs_info:
        print(info.get_text())
        
# key-features
features_info = soup.find_all("span", class_="key-features")
for feature in features_info:
    print(feature.get_text())





