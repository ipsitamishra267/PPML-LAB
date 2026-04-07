#filtering
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Marks': [85, np.nan, 90, 75]
})
df['Marks'].fillna(df['Marks'].mean(), inplace=True)
filtered_df = df[df['Marks'] > 50]

print(filtered_df)