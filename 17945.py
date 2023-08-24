# Baekjoon_BRONZE3_17945: 통학의 신

import sys,math
a,b = map(int, sys.stdin.readline().split())
x = []
x.append((-2*a+math.sqrt((2*a)**2-4*b))/2)
x.append((-2*a-math.sqrt((2*a)**2-4*b))/2)

for i in range(len(set(x))):
    print(int(sorted(x)[i]),end=' ')
