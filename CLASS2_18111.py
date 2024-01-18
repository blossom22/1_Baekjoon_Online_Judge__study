# Baekjoon_CLASS2_Silver2_18111: 마인크래프트

import sys
n,m,b = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 2147483647
level = 0

for i in range(257):        # 땅 높이는 0~256 중 하나이다
    placing = 0             # 블록 하나를 올리는 개수
    taking = 0              # 블록 하나를 제거하는 개수
    for x in range(n):
        for y in range(m):
            if land[x][y] > i:              # 가정한 땅 높이보다 현재높이가 크면, 블록을 제거해야한다
                taking += land[x][y] - i
            elif land[x][y] < i:            # 가정한 땅 높이보다 현재 높이가 낮으면, 블록을 추가해야한다
                placing += i - land[x][y]

    if placing > taking + b:        # 만약 추가되어야하는 블록개수가, 이미 존재했던 b개의 블록+기존의 땅에서 뜯어낸 블록개수보다 크면 진행. 아니면 안돼
        continue
    time = taking * 2 + placing
    if time <= ans:
        ans = time
        level = i
print(ans, level)