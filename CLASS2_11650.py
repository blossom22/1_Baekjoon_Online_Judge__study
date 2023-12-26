# Baekjoon_CLASS2_11650: 좌표 정렬하기

import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data.sort(key=lambda v:(v[0], v[1]))    # x값을 기준으로 오름차순 정렬하되, x값이 동일하면 y값 기준으로 오름차순 정렬
for i in range(n):
    print(*data[i])