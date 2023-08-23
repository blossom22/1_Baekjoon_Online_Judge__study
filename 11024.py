# Baekjoon_BRONZE3_11024: 더하기 4

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    print(sum(n))   