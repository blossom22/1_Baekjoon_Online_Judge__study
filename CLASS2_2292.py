# Baekjoon_CLASS2_Bronze2_2292: 벌집

import sys
n = int(sys.stdin.readline())
stair = 0   # n이 위치한 층
check = 1   # 해당 층에서 최고값

while check < n:
    check += 6*stair    # 각 층에서 최고값을 구하는 식이다
    stair += 1          # 한 층을 갈때마다 stair+=1
if n!=1:
    print(stair)
else:
    print(1)
