# Baekjoon_CLASS2_Silver4_10845: 큐

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()
for i in range(n):
    c = sys.stdin.readline().strip()
    if c[:4]=='push':
        queue.append(int(c[5:]))
    elif c=='pop':
        if len(queue)>0:
            print(queue.popleft())
        else:
            print(-1)
    elif c=='size':
        print(len(queue))
    elif c=='empty':
        if len(queue)>0:
            print(0)
        else:
            print(1)
    elif c=='front':
        if len(queue)>0:
            print(queue[0])
        else:
            print(-1)
    elif c=='back':
        if len(queue)>0:
            print(queue[-1])
        else:
            print(-1)