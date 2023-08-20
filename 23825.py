# Baekjoon_BRONZE4_23825: SASA 모형을 만들어보자 

import sys
n,m = map(int, sys.stdin.readline().split())
a = n//2 
b = m//2
print(a) if a<=b else print(b)