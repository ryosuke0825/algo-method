# Q1-3. 階段ののぼり方
# https://algo-method.com/tasks/304

N = int(input())

if N == 1:
    print(1)
    exit(0)

# 0段目は1パターン、1段目は1パターン
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

# N段目へ行くパターンは、N-1段目へ行くパターン＋N-2段目へ行くパターン
for i in range(2, N+1):
    dp[i] = dp[i-1]+(dp[i-2])
print(dp[-1])
