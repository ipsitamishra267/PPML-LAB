#group by
import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Bob'],
    'Marks': [85, 90, 95, 75, 80]
})
grouped = df.groupby('Name')['Marks'].mean()
print(grouped)