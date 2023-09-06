# Baekjoon_BRONZE1_4796: 캠핑       

import sys 
cnt = 1
while True:
    l,p,v = map(int, sys.stdin.readline().split())
    answer = 0
    if l==0 and p==0 and v==0:
        break
    else:
        a = 0
        if v%p >= l:
            a = l
        else:
            a = v%p
        answer = answer + (v//p)*l + a
        print('Case {}:'.format(cnt),answer)
        cnt+=1