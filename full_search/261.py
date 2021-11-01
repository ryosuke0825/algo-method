# 全探索
# ペアの全探索 5
# https://algo-method.com/tasks/261

N = int(input())
S = input()

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            ans += 1
print(ans)
