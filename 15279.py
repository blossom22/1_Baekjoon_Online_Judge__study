# Baekjoon_BRONZE3_15279: Heart Rate  

import sys
n = int(sys.stdin.readline())
answer = []
for i in range(n):
    a = []
    b,p = map(float, sys.stdin.readline().split())
    bpm = 60*b/p
    temp = 60/p
    abpm_min = '{:.4f}'.format(bpm-temp)
    abpm_max = '{:.4f}'.format(bpm+temp)
    bpm_float = '{:.4f}'.format(bpm)
    a.extend([abpm_min, bpm_float, abpm_max])
    answer.append(a)
for i in range(n):
    print(*answer[i])