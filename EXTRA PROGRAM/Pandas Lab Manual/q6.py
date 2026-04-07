#delete column
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Grade': ['A','B','C','D']
}
df = pd.DataFrame(data)
df = df.drop('Grade', axis=1)
print(df)