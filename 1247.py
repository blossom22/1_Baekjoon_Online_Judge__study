# Baekjoon_BRONZE3_1247: 부호 

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
m = int(sys.stdin.readline())
b = [int(sys.stdin.readline()) for _ in range(m)]
k = int(sys.stdin.readline())
c = [int(sys.stdin.readline()) for _ in range(k)]

data = [a,b,c]
for i in range(3):
    if sum(data[i])>0:
        print('+')
    elif sum(data[i])<0:
        print('-')
    else:
        print(0)