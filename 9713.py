# Baekjoon_BRONZE3_9713: Sum of Odd Sequence  

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    hap = 0
    for j in range(1,n+1):
        if j%2==1:
            hap+=j
    print(hap)