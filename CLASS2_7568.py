# Baekjoon_CLASS2_Silver5_7568: 덩치

import sys
n = int(sys.stdin.readline())
info = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in info:
    place = 1   # 초기에 등수를 1등으로 가정
    for j in info:
        if j[0]>i[0] and j[1]>i[1]:     # 나보다 더 덩치가 큰 놈이 있으면, 등수를 1단계 낮춰(즉, place + 1)
            place += 1
    print(place, end=' ')