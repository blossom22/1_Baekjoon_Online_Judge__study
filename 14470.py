# Baekjoon_BRONZE4_14470: 전자레인지 

a = [int(input()) for _ in range(5)]
if a[0]<0:
    time = -a[0]*a[2] + a[3] + a[1]*a[4]
else:
    time = (a[1]-a[0])*a[4]
print(time)