import pandas as pd

from ss2_00 import df

print(len(df['Name'].unique()))

"""
cut -f 1 ./code/ss2/popular-names.txt | sort | uniq | wc -l
"""