# Q3-7. ボールと 2 つの箱
# https://algo-method.com/tasks/353

N = int(input())
W = list(map(int, input().split()))

M = sum(W)

dp = [[False] * (M+1) for i in range(N+1)]
dp[0][0] = True

for i in range(N):
    for j in range(M):
        if not dp[i][j]:
            continue

        dp[i+1][j+W[i]] = True
        dp[i+1][abs(j-W[i])] = True

ans = 0
while not dp[N][ans]:
    ans += 1
print(ans)
