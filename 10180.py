# Baekjoon_BRONZE3_10180: Ship Selection    

import sys
t = int(sys.stdin.readline())
num = []
for i in range(t):
    n,d = map(int, sys.stdin.readline().split())
    cnt = 0
    for j in range(n):
        v,f,c = map(int, sys.stdin.readline().split())
        if v*f/c >= d:
            cnt+=1 
    num.append(cnt)
print(*num,sep='\n')