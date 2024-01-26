# Baekjoon_CLASS3_Silver2_1927: 최소힙

import sys
import heapq as hq
n = int(sys.stdin.readline())
tree = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num==0:
        if tree:    # 만약 tree가 비어있었다면, 0을 출력해라(문제 조건)
            print(hq.heappop(tree))
        else:
            print(0)
    else:
        hq.heappush(tree, num)
