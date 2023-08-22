# Baekjoon_BRONZE3_10178: 할로윈의 사탕 

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    print('You get {} piece(s) and your dad gets {} piece(s).'.format(a[i][0]//a[i][1], a[i][0]%a[i][1]))
