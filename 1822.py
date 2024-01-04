# Baekjoon_Silver4_1822: 차집합

import sys
a,b = map(int, sys.stdin.readline().split())
n = set(map(int, sys.stdin.readline().split()))
m = set(map(int, sys.stdin.readline().split()))
k = n.difference(m)
if k:
    print(len(k))
    print(*sorted(k))
else:
    print(0)
