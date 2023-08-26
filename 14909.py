# Baekjoon_BRONZE3_14909: 양수 개수 세기

import sys
n = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(len(n)):
    if n[i]>0:
        cnt+=1
print(cnt)