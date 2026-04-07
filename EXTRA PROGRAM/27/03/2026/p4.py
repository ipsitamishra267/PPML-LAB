#Convert Series to categorical and display category codes
import pandas as pd
s = pd.Series(['apple','banana','apple','orange'])
cat_s = s.astype('category')
print(cat_s.cat.codes)