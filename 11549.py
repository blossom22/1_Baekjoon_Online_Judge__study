# Baekjoon_BRONZE4_11549: Identifying tea  

t = int(input())
a = list(map(int, input().split()))
c = 0
for i in range(5):
    if a[i] == t:
        c+=1
print(c)