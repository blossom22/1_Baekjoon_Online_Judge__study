# Baekjoon_BRONZE4_18398: HOMWRK  

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(n):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b, a*b)