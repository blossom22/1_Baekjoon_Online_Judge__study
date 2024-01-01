# Baekjoon_Silver4_18258: 큐 2

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    c = sys.stdin.readline().strip()
    if c[:4]=='push':
        queue.append(int(c[5:]))
    elif c=='pop':
        print(queue.popleft()) if len(queue)>0 else print(-1)
    elif c=='size':
        print(len(queue))
    elif c=='empty':
        print(0) if len(queue)>0 else print(1)
    elif c=='front':
        print(queue[0]) if len(queue)>0 else print(-1)
    elif c=='back':
        print(queue[-1]) if len(queue)>0 else print(-1)