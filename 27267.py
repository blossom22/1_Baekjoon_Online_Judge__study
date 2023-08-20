# Baekjoon_BRONZE4_27267: Сравнение комнат      

a,b,c,d = map(int, input().split())
m = a*b
p = c*d
print('M') if m>p else print('P') if m<p else print('E')