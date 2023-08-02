# Baekjoon_BRONZE4_10480: Oddities  

n = int(input())
data = [int(input()) for _ in range(n)]
for i in range(n):
    if data[i]%2==0:
        print('{} is even'.format(data[i]))
    else:
        print('{} is odd'.format(data[i]))