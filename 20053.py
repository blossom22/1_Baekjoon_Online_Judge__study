# Baekjoon_BRONZE3_20053: 최소, 최대 2 

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    print(min(a),max(a))