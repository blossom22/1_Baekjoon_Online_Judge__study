# Baekjoon_BRONZE3_29684: Which Team Should Receive the Sponsor Prize? 

import sys
while True:
    n = int(sys.stdin.readline())
    if n!=0:
        a = list(map(int, sys.stdin.readline().split()))
        temp = []
        for i in range(n):
            temp.append(abs(a[i]-2023))
        print(temp.index(min(temp))+1)
    else:
        break