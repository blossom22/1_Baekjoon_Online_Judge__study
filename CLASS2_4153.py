# Baekjoon_CLASS2_4153: 직각삼각형 

import sys
while True:
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    if all(a) == False:
        break
    else:
        if a[0]**2 + a[1]**2 == a[2]**2:
            print('right')
        else:
            print('wrong')