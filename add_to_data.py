from bs4 import BeautifulSoup
import pandas as pd
import json

df = pd.read_excel("data_with_name.xlsx")
share_prices = {}

def deal_with_name(i,name):
    try:
        with open(f"final_html/{name}.html",encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error occurred while reading file for {name}: {str(e)}")
        return
    
    try:
        soup = BeautifulSoup(content, 'html.parser')
        last_price_element = soup.find(class_="last-price")
        # last_price_element = content.find_element(By.CLASS_NAME, "last-price")
        last_price_text = last_price_element.text
        share_prices[name] = last_price_text
        df.loc[i, 'share_price'] = last_price_text
        print(f"Share price for {name}: {last_price_text}")
    except Exception as e:
        print(f"Error occurred while getting share price for {name}: {str(e)}")

for i in range(len(df)):
    name = df.loc[i, 'name']
    deal_with_name(i,name)

df.to_excel("data_with_price.xlsx", index=False)
