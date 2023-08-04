# Baekjoon_BRONZE3_2010: 플러그 

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
com = 0
for i in range(n):
    if i != n-1:
        com += (a[i]-1)
    else:
        com += a[i]
        print(com)
        break

# 또는 이렇게도 가능하다
import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
com = sum(a) - n + 1
print(com)