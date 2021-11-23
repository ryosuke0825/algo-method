# Q3-3. ナップサック問題 (導入編)
# https://algo-method.com/tasks/341

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[-1] * M for i in range(N)]
dp[0][0] = 0

for i in range(N-1):
    for j in range(M):
        # 到達できないマス
        if dp[i][j] == -1:
            continue

        # 1マス下
        dp[i+1][j] = max(dp[i+1][j], dp[i][j], 0)

        # 1マス下のAiマス右
        if j+A[i] < M:
            dp[i+1][j+A[i]] = max(max(dp[i][j], 0)+B[i], dp[i+1][j+A[i]])
print(dp[-1][-1])
