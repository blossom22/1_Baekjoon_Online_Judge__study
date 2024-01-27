# Baekjoon_Bronze3_13871: Farm robot

from collections import deque
import sys
n,c,s = map(int, sys.stdin.readline().split())
nlist = deque(range(1,n+1))
command = list(map(int, sys.stdin.readline().split()))
res = 0
if s==1:
    res = 1
for i in range(c):
    if command[i]==1:
        nlist.rotate(-1)
        if nlist[0]==s:
            res += 1
    elif command[i]==-1:
        nlist.rotate(1)
        if nlist[0]==s:
            res += 1
print(res)