# Baekjoon_Silver5_1427: 소트인사이드

import sys
n = list(map(str, sys.stdin.readline().strip('\n')))
m = list(map(int, n))
m.sort(reverse=True)
for i in range(len(n)):
    print(m[i], end='')