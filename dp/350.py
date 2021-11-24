# Q3-5. 部分和問題 (応用 1)
# https://algo-method.com/tasks/350

N, M = map(int, input().split())
W = list(map(int, input().split()))

dp = [[1000] * (M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1000:
            continue

        dp[i+1][j] = min(dp[i+1][j], dp[i][j])

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = min(dp[i+1][j+W[i]], dp[i][j]+1)

if dp[-1][-1] == 1000:
    print(-1)
else:
    print(dp[-1][-1])
