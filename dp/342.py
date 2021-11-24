# Q3-4. ナップサック問題
# https://algo-method.com/tasks/342

N, M = map(int, input().split())
W = list(map(int, input().split()))
V = list(map(int, input().split()))

dp = [[-1] * (M+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == -1:
            continue

        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        if j+W[i] <= M:
            dp[i+1][j+W[i]] = max(dp[i+1][j+W[i]], dp[i][j]+V[i])

print(max(dp[-1]))
