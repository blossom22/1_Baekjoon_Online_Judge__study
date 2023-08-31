# Baekjoon_BRONZE3_3034: 앵그리 창영  

import sys,math
n,w,h = map(int, sys.stdin.readline().split())
k = math.sqrt(w**2+h**2)
for i in range(n):
    a = int(sys.stdin.readline())
    if a<=k:
        print('DA')
    else:
        print('NE')