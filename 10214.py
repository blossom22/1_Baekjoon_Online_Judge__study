# Baekjoon_BRONZE3_10214: Baseball

import sys
t = int(sys.stdin.readline())
for i in range(t):
    y = 0
    k = 0
    for j in range(9):
        a,b = map(int, sys.stdin.readline().split())
        y+=a
        k+=b
    if y>k:
        print('Yonsei')
    elif y<k:
        print('Korea')
    else:
        print('Draw')
    