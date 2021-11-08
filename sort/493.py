# Q1-7. 順位表の並び替え
# https://algo-method.com/tasks/493

N = int(input())
names = ['']*N
points = [[0] * 4 for i in range(N)]
for i in range(N):
    arr = input().split()
    names[i] = arr[0]
    points[i][0] = i
    points[i][1] = int(arr[1])
    points[i][2] = int(arr[2])
    points[i][3] = points[i][1]+points[i][2]

points.sort(key=lambda x: x[3])
points.sort(key=lambda x: x[1], reverse=True)

for i in range(N):
    print('{} {} {}'.format(names[points[i][0]], points[i][1], points[i][2]))
