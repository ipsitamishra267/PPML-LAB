#select rows and columns
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)
print(df['Name'])
print(df[['Name', 'City']])
print(df.iloc[1])
print(df.iloc[1:3])
print(df.loc[1:3, ['Name', 'City']])