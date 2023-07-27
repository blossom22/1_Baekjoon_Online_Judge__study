# Baekjoon_BRONZE4_5575: 타임 카드 

a = [list(map(int, input().split())) for _ in range(3)]
b = [(a[i][3]*3600 + a[i][4]*60 + a[i][5])-(a[i][0]*3600 + a[i][1]*60 + a[i][2]) for i in range(3)]
[print(b[i]//3600, (b[i]%3600)//60, (b[i]%3600)%60) for i in range(3)]

