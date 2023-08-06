# Baekjoon_BRONZE3_2460: 지능형 기차 2

import sys
a = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
temp = [a[i][1]-a[i][0] for i in range(10)]
data = [sum(temp[:i]) for i in range(1,11)]
print(max(data))