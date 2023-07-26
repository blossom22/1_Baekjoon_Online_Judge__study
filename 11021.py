# Baekjoon_BRONZE5_11021: A+B - 7

import sys
t = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
for i in range(t):
    print('Case #{0}: {1}'.format(i+1, sum(a[i])))