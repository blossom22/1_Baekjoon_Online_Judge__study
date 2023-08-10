# Baekjoon_BRONZE4_13752: 히스토그램 

n = int(input())
data = []
for i in range(n):
    a = int(input())
    data.append('='*a)
print(*data,sep='\n')