# Baekjoon_BRONZE4_22015: 金平糖 (Konpeito) 

a,b,c = map(int, input().split())
k = max(a,b,c)
print(k-a+k-b+k-c)