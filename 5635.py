# Baekjoon_Silver5_5635: 생일 

import sys
n = int(sys.stdin.readline())
m = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
m.sort(key=lambda v:(int(v[3]), int(v[2]), int(v[1])))
print(m[-1][0])
print(m[0][0])