# Baekjoon_CLASS2_Silver2_1654: 랜선자르기

import sys
k,n = map(int, sys.stdin.readline().split())
line = list(int(sys.stdin.readline()) for _ in range(k))
ans = 0
left = 1
right = max(line)
while left <= right:
    mid = (left+right)//2
    cnt = 0
    for x in line:
        cnt += x//mid
    if cnt>=n:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)