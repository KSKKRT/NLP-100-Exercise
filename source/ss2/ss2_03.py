import pandas as pd

col1 = pd.read_csv('./code/ss2/col1.txt')
col2 = pd.read_csv('./code/ss2/col2.txt')
concatinate = pd.concat([col1, col2], axis=1)
concatinate.to_csv('concat1_2.txt', sep='\t', index=False)
print(concatinate.head())

# paste command -> concatinate files
# option -> -d:--delimeters
"""
paste ./code/ss2/col1.txt ./code/ss2/col2.txt | head -n 5
"""