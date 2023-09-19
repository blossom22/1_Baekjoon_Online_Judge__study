# Baekjoon_BRONZE4_25304: 영수증 

import sys
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
pr = 0
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    pr += a*b
print('Yes') if pr==x else print('No')