# Baekjoon_BRONZE3_2721: 삼각수의 합   

import sys
t = int(sys.stdin.readline())
a = [int(input()) for _ in range(t)]

def ttt(n):
    temp = 0
    for i in range(1,n+1):
        temp += i
    return temp

def www(n):
    hap = 0
    for i in range(1,n+1):
        hap = hap + (i*ttt(i+1))
    return hap

for i in range(t):
    print(www(a[i]))