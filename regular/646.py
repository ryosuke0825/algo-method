# 正規表現 4-4 typical_snake_case
# https://algo-method.com/tasks/646

# 正規表現を取り扱うためのライブラリ
import re

N, Y, M = map(int, input().split())

YYYYMM = ''
if M <= 9:
    YYYYMM = str(Y)+'0'+str(M)
else:
    YYYYMM = str(Y)+str(M)

reg1 = '.*_' + YYYYMM + '\d\d.pdf'
reg2 = re.compile(r'.*_(.+)_.*')

for _ in range(N):
    S = input()
    search = re.search(reg1, S)
    if search:
        result = reg2.search(S)
        print(result.group(1))
