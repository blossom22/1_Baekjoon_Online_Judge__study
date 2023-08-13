# Baekjoon_BRONZE3_5361: 전투 드로이드 가격 

t = int(input())
price = []
for i in range(t):
    a,b,c,d,e = map(int, input().split())
    k = '{:.2f}'.format(a*350.34 + b*230.90 + c*190.55 + d*125.30 + e*180.90)
    price.append('${}'.format(k))
print(*price, sep='\n')

