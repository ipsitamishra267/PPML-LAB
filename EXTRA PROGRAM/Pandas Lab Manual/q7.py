#Handle missing values
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, 40],
    'City': ['New York', 'Los Angeles', None, 'Houston']
})
df.fillna({'Age': df['Age'].mean(), 'City': 'Unknown'}, inplace=True)
print(df)