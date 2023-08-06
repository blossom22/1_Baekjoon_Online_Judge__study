# Baekjoon_BRONZE3_2445: 지능형 기차

import sys
a = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
temp = [a[i][1]-a[i][0] for i in range(4)]
data = [sum(temp[:i]) for i in range(1,5)]
print(max(data))