# Baekjoon_BRONZE4_8760: Schronisko  

z = int(input())
a = [list(map(int, input().split())) for _ in range(z)]
[print(a[i][0]*a[i][1]//2) for i in range(z)]