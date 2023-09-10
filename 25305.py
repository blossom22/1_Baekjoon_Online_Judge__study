# Baekjoon_BRONZE2_25305: 커트라인

import sys
N,k = map(int, sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))
for _ in range(k-1):
    x.remove(max(x))
print(max(x))
