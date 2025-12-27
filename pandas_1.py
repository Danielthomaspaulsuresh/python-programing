import pandas as pd

df = pd.read_csv("heart.csv")
print(df)

print(df.info())

print(df.duplicated().sum())

print(df.columns)