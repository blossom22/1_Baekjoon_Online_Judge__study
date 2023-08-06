# Baekjoon_BRONZE3_2476: 주사위 게임

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
price = []
for i in range(n):
    if len(set(a[i])) == 1:
        price.append(10000+a[i][0]*1000)
    elif len(set(a[i])) == 3:
        price.append(max(a[i])*100)
    else:
        for j in range(3):
            if a[i].count(a[i][j]) == 2:
                price.append(1000+a[i][j]*100)
print(max(price))