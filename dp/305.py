# Q1-4. タイルの敷き詰め
# https://algo-method.com/tasks/305

N = int(input())

if N == 1:
    print(1)
    exit(0)
elif N == 2:
    print(2)
    exit(0)

dp = [0]*N
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, N):
    dp[i] = dp[i-1]+(dp[i-2])+(dp[i-3])
print(dp[-1])
