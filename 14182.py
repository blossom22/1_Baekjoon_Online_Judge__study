# Baekjoon_BRONZE3_14182: Tax 

import sys
while True:
    a = int(sys.stdin.readline())
    if a != 0:
        if a<1000000:
            print(a)
        elif 1000000<a<=5000000:
            print(int(a*0.9))
        else:
            print(int(a*0.8))
    else:
        break