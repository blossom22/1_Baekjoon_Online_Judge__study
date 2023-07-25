# Baekjoon_BRONZE4_2845: 파티가 끝나고 난 뒤

import sys
a,p = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))
tot = a*p
[print(b[i]-tot, end=' ') for i in range(5)]