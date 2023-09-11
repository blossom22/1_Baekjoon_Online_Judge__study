# Baekjoon_BRONZE2_2908: 상수   

import sys
a,b = map(str, sys.stdin.readline().split())
a = int(a[::-1])
b = int(b[::-1])
print(max(a,b))