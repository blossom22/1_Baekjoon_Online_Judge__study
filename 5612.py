# Baekjoon_BRONZE3_5612: 터널의 입구와 출구    

import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = [m]
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    m = m+a-b
    s.append(m)

if min(s)<0:
    print(0)
else:
    print(max(s))