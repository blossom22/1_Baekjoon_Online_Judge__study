# Baekjoon_BRONZE2_4447: 좋은놈 나쁜놈

n = int(input())
for i in range(n):
    a = {'g':0, 'b':0}
    temp = input()
    name = list(temp)
    for i in name:
        if i=='g' or i=='G':
            a['g']+=1
        elif i=='b' or i=='B':
            a['b']+=1
    if a['g']>a['b']:
        print('%s is GOOD' %temp)
    elif a['g']<a['b']:
        print('%s is A BADDY' %temp)
    else:
        print('%s is NEUTRAL' %temp)