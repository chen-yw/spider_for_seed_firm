import pandas as pd
import time

df = pd.read_excel("data.xlsx")
df['name'] = df['url']
print(df)

for i in range(0, len(df)):
    name = df.loc[i, 'name']
    firm_name = name.split('/')[4]
    # print(name)
    df.loc[i, 'name'] = firm_name

df.to_excel('data_with_name.xlsx', index=False)

