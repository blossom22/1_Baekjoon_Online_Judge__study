# Baekjoon_BRONZE4_28490: Area     

n = int(input())
maximus = 0
for i in range(n):
    h,w = map(int, input().split())
    if h*w>=maximus:
        maximus = h*w
print(maximus)