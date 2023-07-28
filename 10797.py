# Baekjoon_BRONZE4_10797: 10부제 

a = int(input())
car = list(map(int, input().split()))
s = 0
for i in range(5):
    if car[i] == a:
        s+=1
print(s)