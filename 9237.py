# Baekjoon_Silver5_11931: 수 정렬하기 4

import sys
n = int(sys.stdin.readline())
m = list(int(sys.stdin.readline().strip('\n')) for _ in range(n))
for i in sorted(m, reverse=True):
    print(i)