# Baekjoon_BRONZE3_5523: 경기 결과  

import sys
n = int(sys.stdin.readline())
sa = 0
sb = 0
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    if a>b:
        sa+=1
    elif a<b:
        sb+=1
print(sa, sb)