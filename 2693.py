# Baekjoon_BRONZE1_2693: N번째 큰 수

import sys
t = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
for i in range(t):
    for j in range(2):
        data[i].remove(max(data[i]))
    print(max(data[i]))