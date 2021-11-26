# https://algo-method.com/tasks/397
# 正規表現 4-1 アルルの呪文

# 正規表現を取り扱うためのライブラリ
import re

# 調べたい文字列
S = input()

# 置換する（肯定の先読み）
print(re.sub('ru(?=r)', 'ra', S))
