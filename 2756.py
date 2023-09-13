# Baekjoon_BRONZE2_2756: 다트   

import sys
t = int(sys.stdin.readline())
for i in range(t):
    a = list(map(float,sys.stdin.readline().split()))
    score = []
    for j in range(0,12,2):
        temp = a[j]**2+a[j+1]**2
        if temp<=9:
            score.append(100)
        elif 9<temp<=36:
            score.append(80)
        elif 36<temp<=81:
            score.append(60)
        elif 81<temp<=144:
            score.append(40)
        elif 144<temp<=225:
            score.append(20)
        else:
            score.append(0)
    n = sum(score[:3])
    m = sum(score[3:])
    if n>m:
        print('SCORE: {} to {}, PLAYER 1 WINS.'.format(n,m))
    elif n<m:
        print('SCORE: {} to {}, PLAYER 2 WINS.'.format(n,m))
    else:
        print('SCORE: {} to {}, TIE.'.format(n,m))