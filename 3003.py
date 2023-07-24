# Baekjoon_CLASS0_3003: 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys
a = list(map(int, sys.stdin.readline().split()))
b = [1,1,2,2,2,8]
c = [print(b[i]-a[i], end=' ') for i in range(6)]
