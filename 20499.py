# Baekjoon_BRONZE4_20499: Darius님 한타 안 함?

a = list(map(int, input().split('/')))
if a[0]+a[2]<a[1] or a[1]==0:
    print('hasu')
else:
    print('gosu')