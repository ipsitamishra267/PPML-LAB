#Write a Pandas program to merge two DataFrames on a single column id.
import pandas as pd

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'Name': ['Amit', 'Riya', 'Rahul']
})

df2 = pd.DataFrame({
    'id': [1, 2, 3],
    'Marks': [85, 90, 78]
})

merged_df = pd.merge(df1, df2, on='id')

print(merged_df)