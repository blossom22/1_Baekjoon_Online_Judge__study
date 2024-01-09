# Baekjoon_Silver3_2346: 풍선 터뜨리기

from collections import deque
import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
b = deque([i+1, num[i]] for i in range(n))

while len(b)>0:
    dir = b[0][1]
    print(b.popleft()[0], end=' ')
    if dir>0:
        # 그냥 -dir하면 안된다. 한칸 덜 가야함(popleft를 먼저해서 원소가 하나 부족했기 때문)
        b.rotate(-(dir-1))
    else:
        b.rotate(-dir)
    dir = 0
