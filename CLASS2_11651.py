# Baekjoon_CLASS2_11651: 좌표 정렬하기2

import sys
n = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda v: (v[1], v[0]))
for i in range(n):
    print(*m[i])