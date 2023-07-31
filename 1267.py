# Baekjoon_BRONZE3_1267: 핸드폰 요금

n = int(input())
data = list(map(int, input().split()))

def Young(data):
    ify = 0
    for i in range(n):
        ify += (data[i]//30)*10+10
    return ify
def Min(data):
    ifm = 0
    for i in range(n):
        ifm += (data[i]//60)*15+15
    return ifm

if Young(data)>Min(data):
    print('M', Min(data))
elif Young(data)<Min(data):
    print('Y', Young(data))
else:
    print('Y','M',Min(data))