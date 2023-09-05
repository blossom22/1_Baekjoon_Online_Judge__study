# Baekjoon_BRONZE3_15633: Fan Death

import sys
n = int(sys.stdin.readline())
hap = 0
for i in range(1,n+1):
    if n%i==0:
        hap+=i
print(hap*5-24)