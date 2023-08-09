# Baekjoon_BRONZE4_11945: 뜨거운 붕어빵

n,m = map(int, input().split())
data = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m-1,-1,-1):
        print(data[i][j],end='')
    print()