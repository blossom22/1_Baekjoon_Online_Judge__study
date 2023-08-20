# Baekjoon_BRONZE4_27262: Лифт       

n,k,a,b = map(int, input().split())
elev = (k-1)*b + (n-1)*b 
stair = (n-1)*a
print(elev, stair)