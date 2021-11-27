# 正規表現 4-2 アジアンなんとか
# https://algo-method.com/tasks/436

# 正規表現を取り扱うためのライブラリ
import re

# 調べたい文字列
S = input()

# 置換する（肯定の先読み）
print(re.sub('asian(?=(.* ){5})', 'global', S))
