# Baekjoon_Silver5_10815: 숫자 카드

import sys
n = int(sys.stdin.readline())
nl = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))
ml = sorted(ms)
dic = {}

np, mp = 0,0    # nl에서 작동할 포인터와 ml에서 작동할 포인터를 세팅해준다.
while np<=len(nl)-1 and mp<=len(ml)-1:
    if nl[np]==ml[mp]:
        dic[ml[mp]] = 1
        np+=1
        mp+=1
    elif nl[np]>ml[mp]:
        mp+=1
    else:
        np+=1
for i in ms:
    print(dic.get(i,0), end=' ')