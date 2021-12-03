# 問題 5
# https://algo-method.com/tasks/278

A, B, K = map(int, input().split())

if (B+A) % (K+1) != 0:
    print(-1)
else:
    x = K * (A+B)//(K+1)-A
    if x < 0:
        print(-1)
    else:
        print(x)
