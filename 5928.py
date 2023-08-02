# Baekjoon_BRONZE4_5928: Contest Timing     

d,h,m = map(int, input().split())
if d < 11 or (d==11 and h<11) or (d==11 and h==11 and m<11):
    print(-1)
elif d==11:
    print((h*60+m) - (11*60+11))
else:
    print(((d-11)*24*60) + (h*60+m) - (11*60+11))
