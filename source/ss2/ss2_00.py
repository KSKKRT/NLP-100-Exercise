"""
popular-names.txtは,アメリカで生まれた赤ちゃんの「名前」「性別」「人数」「年」をタブ区切り形式で格納したファイルである.
"""
import pandas as pd

df = pd.read_table('code/ss2/popular-names.txt', header=None, sep='\t', names=['Name', 'Gender', 'Number', 'Year'])

if __name__ == '__main__':
    print(len(df))

# wc means word count 
# option -> -m:--chars, -l:--lines, -w:--words
"""linux command
wc -l popular-names.txt
"""
# -> 2780