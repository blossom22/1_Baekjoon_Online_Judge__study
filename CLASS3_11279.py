# Baekjoon_CLASS3_Silver2_11279: 최대힙
# heapq는 기본적으로 최소힙을 기준으로 작동한다. 
# 따라서 입력되는 수의 부호를 바꾸고 나중에 출력할때 -붙이면 그게 최대힙이 된다.
import sys
import heapq as hq
tree = []
n = int(sys.stdin.readline())
for i in range(n):
    num = int(sys.stdin.readline())
    if num==0:
        if tree:
            print(-hq.heappop(tree))
        else:
            print(0)
    else:
        hq.heappush(tree, -num)