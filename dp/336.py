# Q3-1. 部分和問題 (導入編)
# https://algo-method.com/tasks/336

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * M for i in range(N)]
dp[0][0] = 1

for h in range(N-1):
    for w in range(M):
        if dp[h][w] == 1:
            dp[h+1][w] = 1
            if w+A[h] < M:
                dp[h+1][w+A[h]] = 1

print(sum(dp[-1]))
