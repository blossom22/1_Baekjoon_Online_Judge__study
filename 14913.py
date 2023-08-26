# Baekjoon_BRONZE3_14913: 등차수열에서 항 번호 찾기

import sys
a,d,k = map(int, sys.stdin.readline().split())
n = (k-a)/d+1
if int(n)==n and n>0:
    print(int(n))
else:
    print('X')

