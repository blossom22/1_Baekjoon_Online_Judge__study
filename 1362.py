# Baekjoon_BRONZE2_1362: 펫

i = 0
import sys
while True:
    i+=1
    mark = 0
    o,w = map(int, sys.stdin.readline().split())
    if o==0 and w==0:
        break

    while True:
        c,d = map(str, sys.stdin.readline().split())
        if c=='#' and d=='0':
            break 
        d = int(d)
        if c=='F':
            w += d
        else:
            w -= d
        if w<=0:
            mark = 1
    if mark==1:
        print('%d RIP'%i)
    else:
        if w > o/2 and w < o*2:
            print('%d :-)'%i)
        else:
            print('%d :-('%i)