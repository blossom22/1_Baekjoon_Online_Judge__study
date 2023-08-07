# Baekjoon_BRONZE3_2720: 세탁소 사장 동혁  

import sys
t = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(t)]
b = [[0]*4 for _ in range(t)]
for i in range(t):
    b[i][0] = a[i]//25
    b[i][1] = (a[i]%25)//10
    b[i][2] = ((a[i]%25)%10)//5
    b[i][3] = ((a[i]%25)%10)%5
for i in range(t):
    print(*b[i])