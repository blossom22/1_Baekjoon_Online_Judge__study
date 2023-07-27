# Baekjoon_BRONZE4_10101: 삼각형 외우기    

a = [int(input()) for _ in range(3)]
b = sum(a)
c = list(set(a))
if b==180 and len(c)==1:
    print('Equilateral')
elif b==180 and len(c)==2:
    print('Isosceles')
elif b==180 and len(c)==3:
    print('Scalene')
elif b!=180:
    print('Error')