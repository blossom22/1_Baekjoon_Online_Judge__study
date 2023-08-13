# Baekjoon_BRONZE3_18883: N M 찍기

import sys
n,m = map(int, sys.stdin.readline().split())
data = [[0]*m for _ in range(n)]
k = 0
for i in range(n):
    for j in range(m):
        k+=1 
        data[i][j] = k
for i in range(n):
    print(*data[i])
