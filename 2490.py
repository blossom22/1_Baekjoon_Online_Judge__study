# Baekjoon_BRONZE3_2490: 윷놀이

a = [list(map(str, input().split())) for _ in range(3)]
for i in range(3):
    if a[i].count('0')==1:
        print('A')
    elif a[i].count('0')==2:
        print('B')
    elif a[i].count('0')==3:
        print('C')
    elif a[i].count('0')==4:
        print('D')
    else:
        print('E')

