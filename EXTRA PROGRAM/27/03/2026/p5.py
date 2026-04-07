import pandas as pd
s = pd.Series(['apple','banana','apple','orange'])
p = pd.Series(['lion','cat','dog','tiger','monkey','dog','cat'])
cat_s = s.astype('category')
print(cat_s)
animal = p.astype('category')
print(animal)
print(cat_s.cat.codes)
print(animal.cat.codes)