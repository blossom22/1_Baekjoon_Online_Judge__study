# Baekjoon_BRONZE4_27918: 탁구 경기    

import sys
n = int(sys.stdin.readline())
d = 0
p = 0
cnt = 0
for i in range(n):
    a = input()
    if a=='D':
        d+=1
        cnt+=1
    else:
        p+=1
        cnt+=1
    if abs(d-p)==2:
        print(d,':',p,sep='')
        break
    if cnt==n:
        print(d,':',p,sep='')