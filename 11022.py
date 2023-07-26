# Baekjoon_BRONZE5_11022: A+B - 8

import sys
t = int(input())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
for i in range(t):
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, a[i][0], a[i][1], sum(a[i])))
