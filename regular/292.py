# 正規表現 1-1
# https://algo-method.com/tasks/292

import re

S = input()
reg = '.*algo.*'

search = re.search(reg, S)
if search:
    print('Yes')
else:
    print('No')
