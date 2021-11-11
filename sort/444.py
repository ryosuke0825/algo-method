# Q2-6. マージソート
# https://algo-method.com/tasks/444

from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int, input().split()))


def merge_sort(a):

    # 要素数が 11 以下の場合は何も行わない。
    n = len(a)
    if n <= 1:
        return a

    # 配列を左右に分割してソートを行う。 X = N/2 とおく。
    x = n//2

    # A[0],A[1],⋯,A[X] をこの順に配列 LL に格納する。
    l = a[:x]
    # A[X+1],A[X+2],⋯,A[N−1] をこの順に配列 RR に格納する。
    r = a[x:]

    # L,Rを再帰的にソートする。R を逆順に並び替え、LL の最後尾に結合する。
    l = deque(merge_sort(l)+merge_sort(r)[::-1])

    # 空配列Bを用意。
    b = []

    # Lが空になるまで以下を繰り返し行う。
    while l:
        # efirst<=elastならば、efirstの値をBの末尾に追加し、elastを削除する
        if l[0] <= l[-1]:
            b.append(l[0])
            l.popleft()
        else:
            b.append(l[-1])
            l.pop()
    return b


print(*merge_sort(A))
