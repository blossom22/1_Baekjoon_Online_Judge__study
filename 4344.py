# Baekjoon_Bronze1_4344: 평균은 넘겠지

import sys
c = int(sys.stdin.readline())
for i in range(c):
    s = list(map(int, sys.stdin.readline().split()))
    avg = sum(s[1:])/s[0]
    above = 0
    for j in s[1:]:
        if j>avg:
            above += 1
    print(f"{above/s[0]*100:.3f}"+"%")