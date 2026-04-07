#Write a Pandas program to split a dataset to group by two columns and count by each row.
import pandas as pd

data = {
    'School Code': ['S1', 'S1', 'S2', 'S2', 'S1'],
    'Class': ['10', '10', '9', '9', '9'],
    'Student Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Karan']
}

df = pd.DataFrame(data)

grouped = df.groupby(['School Code', 'Class']).size().reset_index(name='Count')

print(grouped)