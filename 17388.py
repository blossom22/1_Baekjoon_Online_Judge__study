# Baekjoon_BRONZE4_17388: 와글와글 숭고한 

u = list(map(int, input().split()))
if sum(u)>= 100:
    print('OK')
else:
    if min(u) == u[0]:
        print('Soongsil')
    elif min(u) == u[1]:
        print('Korea')
    else:
        print('Hanyang')