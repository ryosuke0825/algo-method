# 問題 3
# https://algo-method.com/tasks/277

A, K = map(int, input().split())

if A % (K+1) == 0:
    print((A//(K+1))*K)
else:
    print(-1)
