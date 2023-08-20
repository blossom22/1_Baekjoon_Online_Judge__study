# Baekjoon_BRONZE4_13985: Equality   

e = list(map(str, input().split()))
if int(e[0])+int(e[2]) == int(e[-1]):
    print('YES')
else:
    print('NO')