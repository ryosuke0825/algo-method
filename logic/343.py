# 問題 7
# https://algo-method.com/tasks/343

A, K = map(int, input().split())

if A % K == 0:
    print(A)
else:
    print(A+(K-A % K))
