# Q3-2. 部分和問題
# https://algo-method.com/tasks/337

N, M = map(int, input().split())
W = list(map(int, input().split()))

# 0枚と0のカードも考える
dp = [[False] * (M+1) for i in range(N+1)]

# 0枚と0のカードで0は作れるのでTrueにする
dp[0][0] = True

# jをiの状態にカードを足して作れるかどうか。
for i in range(N):
    for j in range(M+1):
        # 到達できない数字
        if not dp[i][j]:
            continue

        dp[i+1][j] = True

        # M以下になるようにもう1枚足せるか
        if j+W[i] <= M:
            dp[i+1][j+W[i]] = True

if dp[-1][-1]:
    print('Yes')
else:
    print('No')
