# 正規表現 4-3 algometric
# https://algo-method.com/tasks/435

import re

S = input()
reg = 'algo(?!(rithm|method))[a-z]{5,}'

search = re.search(reg, S)
if search:
    print('Yes')
else:
    print('No')
