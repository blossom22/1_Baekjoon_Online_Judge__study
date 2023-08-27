# Baekjoon_BRONZE3_15036: Just A Minim  

import sys
dic = {0:2, 1:1, 2:0.5, 4:0.25, 8:0.125, 16:0.0625}
n = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
hap = 0
for i in ls:
    hap+=dic[i]
print(hap)