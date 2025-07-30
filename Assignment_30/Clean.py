import pandas as pd

df = pd.read_csv('bank-full.csv')

df.columns = df.columns.str.strip('" ')

df = df.applymap(lambda x: x.strip('" ') if isinstance(x, str) else x)

df.to_csv('bank-full-clean.csv', index=False)

print(" remove the in (" ")csv ")
