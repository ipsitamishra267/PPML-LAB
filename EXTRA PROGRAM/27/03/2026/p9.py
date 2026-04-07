#Write a Pandas program to split the following dataframe into groups based on school code. also check the type of groupby object.
import pandas as pd

data = {
    'Index': [1, 2, 3, 4, 5],
    'School Code': ['s001', 's002', 's003', 's002', 's003'],
    'Student Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Karan'],
    'Age': [14, 15, 14, 15, 16],
    'Height': [5.1, 5.3, 5.0, 5.2, 5.4],
    'Weight': [45, 48, 42, 46, 50],
    'Date of Birth': ['2009-05-10', '2008-08-21', '2009-03-15', '2008-11-30', '2007-07-19'],
    'Address': ['Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'Bangalore']
}

df = pd.DataFrame(data)

df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])

grouped = df.groupby('School Code')

for name, group in grouped:
    print(f"\nGroup: {name}")
    print(group)

print("\nType of groupby object:")
print(type(grouped))