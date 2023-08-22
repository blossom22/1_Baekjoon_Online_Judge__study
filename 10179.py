# Baekjoon_BRONZE3_10179: 쿠폰   

import sys
t = int(sys.stdin.readline())
answer = []
for i in range(t):
    p = float(sys.stdin.readline())
    answer.append('${}'.format('{:.2f}'.format(p*0.8)))
print(*answer,sep='\n')