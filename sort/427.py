# Q2-9. バケットソート
# https://algo-method.com/tasks/447

N = int(input())
A = list(map(int, input().split()))
X = N+1
# 長さXの配列numを用意し、各要素を0で初期化する。
num = [0]*X

# i=0,1,⋯,N−1 について、num[A[i]]の値を1増やす。
for i in range(N):
    num[A[i]] += 1

# 1、i=0のとき、acc[i]=num[i]
acc = [0]*X
acc[0] = num[0]

# i=0,1,⋯,X−1 について、次のようにacc[i]を更新する。
# 2、i!=0のとき、acc[i]=acc[i-1]+num[i]
for i in range(1, X):
    acc[i] = acc[i-1]+num[i]

# 長さがNの配列Bを用意する。
B = [0]*N

# i=0,1,⋯,N−1 について、次のようにBを更新する。
# acc[A[i]]の値を1減らす。
# B[acc[A[i]]]にA[i]の値を代入する。
for i in range(N):
    acc[A[i]] -= 1
    B[acc[A[i]]] = A[i]
print(*B)
