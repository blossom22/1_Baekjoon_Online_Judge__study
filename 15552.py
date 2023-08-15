# Baekjoon_BRONZE4_15552: 빠른 A+B

import sys
t = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
[print(sum(a[i])) for i in range(t)]