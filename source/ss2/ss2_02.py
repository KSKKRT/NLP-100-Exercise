from ss2_00 import df

col1 = df['Name']
col2 = df['Gender']
col1.to_csv('col1.txt', index=False)
col2.to_csv('col2.txt', index=False)
print(col1.head())
print(col2.head())

# cut command
# option -> -d:--delimeter, -f:--fields
"""
cut -f 2 './code/ss2/popular-names.txt' | head -n 5
"""