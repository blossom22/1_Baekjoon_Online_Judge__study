# Baekjoon_BRONZE3_2523: 별 찍기 - 13

n = int(input())
for i in range(1,n+1):
    print('*'*i)
for j in range(n-1,0,-1):
    print('*'*j)