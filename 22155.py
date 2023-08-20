# Baekjoon_BRONZE4_22155: Простая задача 

n = int(input())
result = []
for i in range(n):
    i,f = map(int, input().split())
    result.append('Yes') if (i<=1 and f<=2) or (i<=2 and f<=1  ) else result.append('No') 
print(*result,sep='\n')