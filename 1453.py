# Baekjoon_BRONZE2_1453: 피시방 알바

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(abs(len(a)-len(set(a))))