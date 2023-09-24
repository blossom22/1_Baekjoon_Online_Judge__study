# Baekjoon_BRONZE2_2028: 자기복제수

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    a = len(str(n))
    if int(str(n**2)[-a:]) == n:
        print('YES')
    else:
        print('NO')

