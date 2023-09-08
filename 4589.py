# Baekjoon_BRONZE4_4589: Gnome Sequencing   

import sys
n = int(sys.stdin.readline())
result = ['Gnomes:']
for i in range(n):
    a,b,c = map(int, sys.stdin.readline().split())
    if (a<=b<=c) or (a>=b>=c):
        result.append('Ordered')
    else:
        result.append('Unordered')
print(*result,sep='\n')