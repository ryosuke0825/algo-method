# Q2-1. 表と数字 (1)
# https://algo-method.com/tasks/324

A = list(map(int, input().split()))

ans = [[0] * 4 for i in range(4)]
for i in range(4):
    ans[0][i] = A[i]

for i in range(3):
    for j in range(4):
        # 真下
        ans[i+1][j] += ans[i][j]

        # 左下
        if j != 0:
            ans[i+1][j-1] += ans[i][j]

        # 右下
        if j != 3:
            ans[i+1][j+1] += ans[i][j]
print(ans[-1][-1])
