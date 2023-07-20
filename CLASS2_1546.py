# Baekjoon_CLASS2_1546: 평균 

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(sum([a[i]/max(a)*100 for i in range(n)])/n)