# Baekjoon_BRONZE3_14720: 우유 축제 

import sys
n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0
milk = 0
for i in range(n):
    if data[i]==(milk%3):
        cnt+=1
        milk+=1
print(cnt)