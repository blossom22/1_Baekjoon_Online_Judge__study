# Baekjoon_BRONZE2_2750: 수 정렬하기

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
a.sort()
for i in range(n):
    print(a[i])