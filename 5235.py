# Baekjoon_BRONZE3_5235: Even Sum More Than Odd Sum  

import sys
t = int(sys.stdin.readline())
for i in range(t):
    a = list(map(int, sys.stdin.readline().split()))
    even = 0
    odd = 0
    for j in range(1,a[0]+1):
        if a[j]%2==0:
            even+=a[j]
        else:
            odd+=a[j]
    if even>odd:
        print('EVEN')
    elif even<odd:
        print('ODD')
    else:
        print('TIE')