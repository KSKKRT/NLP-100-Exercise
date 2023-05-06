#sed(Stream EDitor) command
#option -> -e:add script command
#script command: s/a/b/g
#gの有無でパターンにマッチした全ての文を変換するか決められる．

"""
sed -e 's/\t/ /g' ./code/ss2/popular-names.txt | head -n 5
"""