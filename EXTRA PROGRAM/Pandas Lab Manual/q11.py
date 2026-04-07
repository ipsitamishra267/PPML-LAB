#Merge dataframe
import pandas as pd
df1 = pd.DataFrame({'ID':[1,2]})
df2 = pd.DataFrame({'ID':[1,2],'Marks':[80,90]})
print(pd.merge(df1,df2,on='ID'))