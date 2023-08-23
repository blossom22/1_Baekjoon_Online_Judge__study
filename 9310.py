# Baekjoon_BRONZE3_9310: Arithmetic and Geometric Sums  

import sys
while True:
    n = int(sys.stdin.readline())
    if n!=0:
        a,b,c = map(int, sys.stdin.readline().split())
        if a+c==b*2:
            print(n*(2*a+(n-1)*(b-a))//2)
        else:
            r = b//a
            print(a*(r**n-1)//(r-1))
    else:
        break