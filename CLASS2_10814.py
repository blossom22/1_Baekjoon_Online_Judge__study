# Baekjoon_CLASS2_10814: 좌표 정렬하기

import sys
n = int(sys.stdin.readline())
data = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    data[i].append(i)
data.sort(key=lambda v:(int(v[0]), v[2]))
for i in range(n):
    print(int(data[i][0]), data[i][1])