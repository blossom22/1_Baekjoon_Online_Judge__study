# Baekjoon_Silver4_1269: 대칭 차집합

import sys
a,b = map(int, sys.stdin.readline().split())
n = set(map(int, sys.stdin.readline().split()))
m = set(map(int, sys.stdin.readline().split()))
k = n.symmetric_difference(m)
print(len(k))