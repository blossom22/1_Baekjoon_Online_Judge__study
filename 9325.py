# Baekjoon_BRONZE3_9325: 얼마?

import sys
t = int(sys.stdin.readline())
car = []
for i in range(t):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    op = []
    for j in range(n):
        q,p = map(int, sys.stdin.readline().split())
        op.append(q*p)
    car.append(s+sum(op))
print(*car,sep='\n')