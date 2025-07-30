import pandas as pd

df_raw = pd.read_csv("bank-full.csv", header=None)

df_split = df_raw[0].str.split(';', expand=True)

df_split.columns = df_split.iloc[0]  
df_split = df_split[1:]              

df_split.reset_index(drop=True, inplace=True)

df_split.to_csv("bank-full-OK.csv", index=False)

print("Cleaned CSV saved as 'bank-full-OK.csv'")
