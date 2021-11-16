# Q2-3. 3 つの仕事
# https://algo-method.com/tasks/41

N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

ans = [[0] * 3 for i in range(N)]
for i in range(3):
    ans[0][i] = A[0][i]

for i in range(1, N):
    ans[i][0] = A[i][0]+max(ans[i-1][1], ans[i-1][2])
    ans[i][1] = A[i][1]+max(ans[i-1][0], ans[i-1][2])
    ans[i][2] = A[i][2]+max(ans[i-1][0], ans[i-1][1])
print(max(ans[-1]))
