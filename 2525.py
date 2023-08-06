# Baekjoon_BRONZE3_2525: 오븐 시계

a,b = map(int, input().split())
c = int(input())

min = a*60+b+c
if min>=1440:
    print(min//60-24, min%60)
else:
    print(min//60, min%60)