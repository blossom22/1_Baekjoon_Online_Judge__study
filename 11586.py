# Baekjoon_BRONZE3_11586: 지영 공주님의 마법 거울

n = int(input())
matrix = [list(input()) for _ in range(n)]
k = int(input())

if k==1:
    for i in range(n):
        print(*matrix[i],sep='')
elif k==2:
    for i in range(n):
        print(*matrix[i][::-1],sep='')
else:
    for i in range(n):
        print(*matrix[n-1-i],sep='')