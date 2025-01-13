from bs4 import BeautifulSoup
import json

def html2json(num):
    print(num)
    # 读取本地HTML文件
    try:
        with open(f"raw_html/file_{num}.html", "r", encoding="utf-8") as file:
            html_content = file.read()
    except Exception as e:
        print(f"Error occurred while reading file_{num}.html: {str(e)}")
        return
    
    # 先创建一个json对象来存储信息
    json_obj = {}
    
    # 是用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html_content, "lxml")
    tr_elements = soup.find_all("tr")
    
    location_info = soup.find_all("tr", class_="location")
    json_obj["location"] = ""
    for location in location_info:
        td_elements = location.find_all("td")
        for td in td_elements:
            json_obj["location"] += td.get_text()
    json_obj["location"] = json_obj["location"].replace("\n"," ")

    website_links = soup.find_all("a", class_="website",title = True)
    json_obj["website"] = ""
    for link in website_links:
        json_obj["website"] += link.get_text()
    json_obj["website"] = json_obj["website"].replace("\n"," ")

    sectors_info = soup.find_all("tr", class_="sectors")
    json_obj["sectors"] = ""
    for sector in sectors_info:
        sector_detail = sector.find_all("span")
        for detail in sector_detail:
            json_obj["sectors"] += detail.get_text()
    json_obj["sectors"] = json_obj["sectors"].replace("\n"," ")    
    
    incorporation_date_trs = [tr for tr in tr_elements if "Incorporation date" in tr.get_text()]
    json_obj["incorporation date"] = ""
    for tr in incorporation_date_trs:
        date_info = tr.find_all("td")
        for info in date_info:
            json_obj["incorporation date"] += info.get_text()
    json_obj["incorporation date"] = json_obj["incorporation date"].replace("\n"," ")
    
    valuation_trs = [tr for tr in tr_elements if "Indicative valuation" in tr.get_text()]
    json_obj["indicative valuation"] = ""
    for tr in valuation_trs:
        valuation_info = tr.find_all("td")
        for info in valuation_info:
            json_obj["indicative valuation"] += info.get_text()
    json_obj["indicative valuation"] = json_obj["indicative valuation"].replace("\n"," ")
    
    change_trs = [tr for tr in tr_elements if "Change (%)" in tr.get_text()]
    json_obj["change (%)"] = ""
    for tr in change_trs:
        change_info = tr.find_all("span")
        for info in change_info:
            json_obj["change (%)"] += info.get_text()
    json_obj["change (%)"] = json_obj["change (%)"].replace("\n"," ")
    
    total_raised_trs = [tr for tr in tr_elements if "Total raised" in tr.get_text()]
    json_obj["total raised"] = ""
    for tr in total_raised_trs:
        total_raised_info = tr.find_all("td")
        for info in total_raised_info:
            json_obj["total raised"] += info.get_text()
    json_obj["total raised"] = json_obj["total raised"].replace("\n"," ")
            
    total_indvestors_trs = [tr for tr in tr_elements if "Total investors" in tr.get_text()]
    json_obj["total investors"] = ""
    for tr in total_indvestors_trs:
        total_investors_info = tr.find_all("td")
        for info in total_investors_info:
            json_obj["total investors"] += info.get_text()
    json_obj["total investors"] = json_obj["total investors"].replace("\n"," ")   
    
    eligibility_status_trs = [tr for tr in tr_elements if "Eligibility status" in tr.get_text()]
    json_obj["Eligibility status"] = ""
    for tr in eligibility_status_trs:
        eligibility_status_info = tr.find_all("td")
        for info in eligibility_status_info:
            lines = info.get_text().split("\n")
            for line in lines:
                stripped_line = line.strip()
                if stripped_line:
                    json_obj["Eligibility status"] += stripped_line
                    break
    json_obj["Eligibility status"] = json_obj["Eligibility status"].replace("\n"," ")
    
    available_shares_trs = [tr for tr in tr_elements if "Available shares" in tr.get_text()]
    json_obj["available shares"] = ""
    for tr in available_shares_trs:
        available_shares_trs_info = tr.find_all("td")
        for info in available_shares_trs_info:
            json_obj["available shares"] += info.get_text()
    json_obj["available shares"] = json_obj["available shares"].replace("\n"," ")
    
    features_info = soup.find_all("span", class_="key-features")
    json_obj["key-features"] = ""
    for feature in features_info:
        json_obj["key-features"] += feature.get_text()
    json_obj["key-features"] = json_obj["key-features"].replace("\n"," ")
    
    with open(f"json_file/json_{num}.json", "w",encoding='utf-8') as f:
        json.dump(json_obj, f,indent=4, ensure_ascii=False)


for i in range(756):
    html2json(i+1)





