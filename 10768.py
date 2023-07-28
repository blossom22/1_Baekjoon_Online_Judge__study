# Baekjoon_BRONZE4_10768: 특별한 날 

n = int(input())
m = int(input())
if n>=2 and m>18:
    print('After')
elif n<=2 and m<18:
    print('Before')
else: 
    print('Special')