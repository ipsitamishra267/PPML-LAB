#Convert Series from string to numeric with error handling
import pandas as pd

s = pd.Series(['10','20','abc','30'])
numeric_s = pd.to_numeric(s,errors='coerce')
print(numeric_s)
