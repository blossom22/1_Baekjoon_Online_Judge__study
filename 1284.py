# Baekjoon_BRONZE3_1284: 집 주소 

import sys
while True:
    n = int(sys.stdin.readline())
    m = str(n)
    a = 0
    if n != 0:
        for i in m:
            if i == '1':
                a+=2
            elif i == '0':
                a+=4
            else:
                a+=3
        a+=(len(m)+1)
        print(a)
    else:
        break