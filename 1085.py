# Baekjoon_BRONZE3_1085: 직사각형에서 탈출 

x,y,w,h = map(int, input().split())
data = [h-y, w-x, y, x]
print(min(data))