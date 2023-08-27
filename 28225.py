# Baekjoon_BRONZE3_28225: Flower Festival 

import sys
n,f = map(int, sys.stdin.readline().split())
now = []
for i in range(n):
    x,v = map(int, sys.stdin.readline().split())
    now.append((f-x)/v)
print(now.index(min(now))+1)