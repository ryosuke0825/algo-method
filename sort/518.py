# Q2-7. ヒープソートの準備
# https://algo-method.com/tasks/518

N = int(input())
A = list(map(int, input().split()))

x = N//2-1
while x >= 0:
    k = x
    while True:
        if 2*k+1 >= N:
            break

        # A[k],A[2k+1]A[2k+1],A[2k+2]を比較する
        tmp = max(A[k], A[2*k+1])
        if 2*k+2 < N:
            tmp = max(tmp, A[2*k+2])

        # 頂点kを選択した場合
        if tmp == A[k]:
            break

        # 頂点2k+1を選択した場合
        elif tmp == A[2*k+1]:
            A[k], A[2*k+1] = A[2*k+1], A[k]
            k = 2*k+1

        elif tmp == A[2*k+2]:
            A[k], A[2*k+2] = A[2*k+2], A[k]
            k = 2*k+2
    x -= 1
print(*A)
