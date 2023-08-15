# Baekjoon_BRONZE4_28295: 체육은 코딩과목 입니다     

a = 1
for i in range(10):
    n = int(input())
    a = (a+n)%4
if a==1:
    print('N')
elif a==2:
    print('E')
elif a==3:
    print('S')
else:
    print('W')