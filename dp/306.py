# Q1-5. マスの移動 (2)
# https://algo-method.com/tasks/306

N, M = map(int, input().split())
A = list(map(int, input().split()))

INF = 10**8
dp = [INF]*N
dp[0] = 0
for i in range(1, N):
    dp[i] = min(dp[i], dp[i-1]+A[i], dp[i-2]+A[i]*2)
    for j in range(1, M+1):
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+A[i]*j)
print(dp[-1])
