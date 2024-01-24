# Baekjoon_BRONZE4_18691: Pokemon Buddy

import sys, math
t = int(sys.stdin.readline())
for i in range(t):
    g,c,e = map(int,sys.stdin.readline().split())
    need = e-c
    if need<=0:
        print(0)
    else:
        if g==1:
            print(need)
        elif g==2:
            print(need*3)
        elif g==3:
            print(need*5)
