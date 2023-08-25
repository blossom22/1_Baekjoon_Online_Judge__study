# Baekjoon_BRONZE3_10865: 친구 친구

import sys
n,m = map(int, sys.stdin.readline().split())
dic = {i:0 for i in range(1,n+1)}
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    dic[a] += 1
    dic[b] += 1
print(*list(dic.values()),sep='\n')
