# Baekjoon_BRONZE4_28281: 선물    

import sys
n,x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
price = []
for i in range(n-1):
    price.append(a[i]*x + a[i+1]*x)
print(min(price))