# 問題 4
# https://algo-method.com/tasks/279

A, B, K = map(int, input().split())

if B-A < 0 or (B-A) % (K+1) != 0:
    print(-1)
else:
    y = (B-A) // (K+1)
    print(K*y+A)
