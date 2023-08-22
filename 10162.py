# Baekjoon_BRONZE3_10162: 전자레인지  

import sys
a = 0
b = 0
c = 0
t = int(sys.stdin.readline())
while t>0:
    if t//300 > 0:
        t -= 300
        a += 1
    elif t//60 > 0:
        t -= 60
        b += 1
    elif t//10 > 0:
        t -= 10
        c += 1
    else:
        print(-1)
        break
else:
    print(a,b,c)
