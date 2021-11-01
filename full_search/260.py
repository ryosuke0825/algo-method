# 全探索
# ペアの全探索 4
# https://algo-method.com/tasks/260

N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)

ans = 'No'
for i in range(N):
    for j in range(i+1, N):
        if S[i] == S[j]:
            ans = 'Yes'
            break
print(ans)
