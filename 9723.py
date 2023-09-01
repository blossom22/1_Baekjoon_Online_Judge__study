# Baekjoon_BRONZE3_9723: Right Triangle 

import sys
t = int(sys.stdin.readline())
for i in range(t):
    ls = list(map(int, sys.stdin.readline().split()))
    ls.sort()
    if ls[2]**2==ls[0]**2+ls[1]**2:
        print('Case #{}: YES'.format(i+1))
    else:
        print('Case #{}: NO'.format(i+1))