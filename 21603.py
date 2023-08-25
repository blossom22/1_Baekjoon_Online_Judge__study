# Baekjoon_BRONZE3_21603: K 2K 게임 

import sys
n,k = map(int, sys.stdin.readline().split())
cnt = 0
t = []
for i in range(1,n+1):
    if str(i)[-1]!=str(k)[-1] and str(i)[-1]!=str(2*k)[-1]:
        t.append(i)
        cnt+=1
print(cnt)
print(*t)
