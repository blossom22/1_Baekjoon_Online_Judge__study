# Baekjoon_BRONZE2_1568: 새

import sys
n = int(sys.stdin.readline())
cnt = 0
a = 1
while True:
    if n>0:
        n -= a
        cnt+=1
        a+=1
        if n<a:
            a=1
    else:
        break
print(cnt)