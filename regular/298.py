# https://algo-method.com/tasks/298
# 正規表現 1-2

# 正規表現を取り扱うためのライブラリ
import re

# 調べたい文字列
S = input()
# 調べる正規表現
reg = 'metho.+od'

# マッチした位置が格納される (存在しなければ null)
search = re.search(reg, S)
if search:
    # "Yes" と表示される
    print("Yes")
else:
    print("No")
