# Baekjoon_BRONZE3_5292: Counting Swann’s Coins  

import sys
a = int(sys.stdin.readline())
for i in range(1,a+1):
    if i%3==0 and i%5==0:
        print('DeadMan')
    elif i%5==0:
        print('Man')
    elif i%3==0:
        print('Dead')
    else:
        print(i,end=' ')