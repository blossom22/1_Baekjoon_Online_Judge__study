# Baekjoon_BRONZE4_10156: 과자

import sys
k,n,m = map(int, sys.stdin.readline().split())
[print(k*n-m) if k*n>m else print(0)]