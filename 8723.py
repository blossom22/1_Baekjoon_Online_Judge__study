# Baekjoon_BRONZE4_8723: Patyki   

sam = sorted(list(map(int, input().split())))
if sam[0]**2+sam[1]**2 == sam[2]**2:
    print(1)
elif sam[0]==sam[1]==sam[2]:
    print(2)
else:
    print(0)