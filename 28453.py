# Baekjoon_BRONZE4_28453: Previous Level    

n = int(input())
m = list(map(int, input().split()))
for i in range(n):
    if m[i]==300:
        print(1, end=' ')
    elif 275<=m[i]:
        print(2, end=' ')
    elif 250<=m[i]:
        print(3, end=' ')
    else:
        print(4, end=' ')

