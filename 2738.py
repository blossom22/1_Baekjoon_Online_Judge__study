# Baekjoon_CLASS0_2738: 행렬 덧셈

import sys
n,m = map(int, sys.stdin.readline().split())
a = [[0]*m for i in range(n)]
b = [[0]*m for i in range(n)]
c = [[0]*m for i in range(n)]
for i in range(n):
    a[i] = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    b[i] = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(m):
        c[i][j] = a[i][j] + b[i][j]
    print(*c[i], end='\n')