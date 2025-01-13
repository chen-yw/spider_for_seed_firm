import json
import pandas as pd
import numpy as np

all_data = []

url_df = pd.read_csv("website.csv")

def json2xlsx(num):
    print(num)
    try:
        with open(f"json_file/json_{num}.json",encoding='utf-8') as f:
            data = json.load(f)
        data['url'] = url_df.loc[num-1,'website']
        all_data.append(data)
        print(data)
    except Exception as e:
        print(f"Error occurred while reading json_{num}.json: {str(e)}")
        return

for i in range(756):
    json2xlsx(i+1)

df = pd.DataFrame(all_data)
df.to_excel("data.xlsx", index=False)
