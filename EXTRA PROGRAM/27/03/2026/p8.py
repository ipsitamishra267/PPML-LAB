#Write a pandas program to create a DataFrame from a dictionary and then transpose it,ensuring that data types remain consistent.
import pandas as pd

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}

df = pd.DataFrame(data)

print(df)
print(df.dtypes)

df_t = df.T

print(df_t)
print(df_t.dtypes)