# Baekjoon_BRONZE4_8710: Koszykarz        

k, w, m = map(int, input().split())
temp = int((w-k)/m)
if temp == (w-k)/m:
    print(temp)
else:
    print(temp+1)