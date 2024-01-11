# Baekjoon_Silver3_29813: 최애의 팀원

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque(list(map(str, sys.stdin.readline().split())) for _ in range(n))
while len(queue)>1:
    tmp = queue.popleft()
    queue.rotate(-int(tmp[1])+1)
    queue.popleft()
print(queue[0][0])
