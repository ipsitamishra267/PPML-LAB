#concatenate
import pandas as pd

df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Marks': [85, 90]
})

df2 = pd.DataFrame({
    'Name': ['Charlie', 'David'],
    'Marks': [75, 80]
})

concatenated_df = pd.concat([df1, df2], ignore_index=True)

print(concatenated_df)