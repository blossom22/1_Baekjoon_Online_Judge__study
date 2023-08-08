# Baekjoon_BRONZE3_28417: 스케이트보드

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
data = []
for i in range(n):
    b = sorted(a[i][2:])
    data.append(max(a[i][:2]) + b[-2] + b[-1])
print(max(data))