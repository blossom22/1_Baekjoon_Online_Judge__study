# Baekjoon_BRONZE3_2588: 곱셈

a = int(input())
b = int(input())

i = a*int(str(b)[-1])
j = a*int(str(b)[-2])
k = a*int(str(b)[0])
print(i, j, k, i+j*10+k*100, sep='\n')
