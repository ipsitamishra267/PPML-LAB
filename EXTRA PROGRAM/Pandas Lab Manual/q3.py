#load csv and show info.
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
print(df.describe())