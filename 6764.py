# Baekjoon_BRONZE4_6764: Sounds fishy!

a = [int(input()) for _ in range(4)]

def rise(a):
    cnt = 0
    for i in range(0,3):
        if a[i]<a[i+1]:
            cnt += 1
            pass
        else:
            break
    if cnt == 3:
        return 'Fish Rising'

def dive(a):
    cnt = 0
    for i in range(0,3):
        if a[i]>a[i+1]:
            cnt += 1
            pass
        else:
            break
    if cnt == 3:
        return 'Fish Diving'

def cons(a):
    if len(list(set(a))) == 1:
        return 'Fish At Constant Depth'

answer = [rise(a) ,dive(a), cons(a)]

for i in range(3):
    if any(answer) == True:
        if answer[i] != None:
            print(answer[i])
    else:
        print('No Fish')
        break