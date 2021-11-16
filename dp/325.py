# Q2-2. 表と数字 (2)
# https://algo-method.com/tasks/325

N = int(input())
A = list(map(int, input().split()))

ans = [[0] * N for i in range(N)]
for i in range(N):
    ans[0][i] = A[i]

for i in range(N-1):
    for j in range(N):
        # 真下
        ans[i+1][j] += ans[i][j]

        # 左下
        if j != 0:
            ans[i+1][j-1] += ans[i][j]

        # 右下
        if j != N-1:
            ans[i+1][j+1] += ans[i][j]

    for j in range(N):
        ans[i][j] %= 100

for i in range(N):
    ans[-1][i] %= 100

print(ans[-1][-1])
