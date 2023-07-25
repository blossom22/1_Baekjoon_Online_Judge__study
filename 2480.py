# Baekjoon_BRONZE4_2480: 주사위 세개

a = list(map(int, input().split()))
b = list(set(a))
if len(b) == 1:
    print(a[0]*1000 + 10000)
elif len(b) == 3:
    print(max(a)*100)
else:
    for i in a:
        if a.count(i) == 2:
            print(i*100 + 1000)
            break