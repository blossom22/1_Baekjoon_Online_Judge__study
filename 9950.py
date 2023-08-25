# Baekjoon_BRONZE3_9950: Rectangles     

import sys
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if any([a,b,c]) != False:
        if a==0:
            a=c//b
            print(a,b,c)
        elif b==0:
            b=c//a
            print(a,b,c)
        elif c==0:
            c=a*b
            print(a,b,c)
    else:
        break