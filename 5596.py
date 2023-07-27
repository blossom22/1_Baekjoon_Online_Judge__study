# Baekjoon_BRONZE4_5596: 시험 점수 

import sys
a = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
print(max(sum(a[0]), sum(a[1])))