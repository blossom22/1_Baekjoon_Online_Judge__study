# Baekjoon_CLASS2_2751: 수 정렬하기 2

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]
a.sort()
print(*a,sep='\n')