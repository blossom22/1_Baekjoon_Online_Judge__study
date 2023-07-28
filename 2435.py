# Baekjoon_BRONZE1_2435: 기상청 인턴 신현수

import sys
n,k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
hap = [sum(data[i:i+k]) for i in range(n-k+1)]
print(max(hap))