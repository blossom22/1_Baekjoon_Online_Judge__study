# Baekjoon_BRONZE3_5565: 영수증   

import sys
n = int(sys.stdin.readline())
hap = sum([int(sys.stdin.readline()) for _ in range(9)])
print(n-hap)