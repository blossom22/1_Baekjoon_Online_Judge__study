# Baekjoon_BRONZE2_1964: 오각형, 오각형, 오각형…

import sys
n = int(sys.stdin.readline())
dot = 5
for i in range(1,n):
    dot = dot+(3*i+4)
print(dot%45678)