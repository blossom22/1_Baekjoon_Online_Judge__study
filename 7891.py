# Baekjoon_CLASS0_7891: Can you add this?

import sys
t = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
b = [print(sum(a[i])) for i in range(t)]