# Q1-4. 荷物と箱
# https://algo-method.com/tasks/361

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 昇順ソート
A.sort()

ans = 0
bidex = 0
for i in range(N):
    if bidex >= M:
        break
    for j in range(bidex, M):
        bidex += 1
        if B[j] >= A[i]:
            ans += 1
            break
print(ans)
