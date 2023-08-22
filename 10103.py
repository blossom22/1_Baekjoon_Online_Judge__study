# Baekjoon_BRONZE3_10103: 주사위 게임

n = int(input())
a = 100
b = 100
for i in range(n):
    n,m = map(int, input().split())
    if n>m:
        b -= n
    elif n<m:
        a -= m
print(a,b,sep='\n')