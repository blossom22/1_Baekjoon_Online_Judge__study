# Baekjoon_CLASS2_Silver4_10866: 덱

from collections import deque
import sys
n = int(sys.stdin.readline())
d = deque()
for i in range(n):
    c = sys.stdin.readline().strip()
    if c[:10]=='push_front':
        d.appendleft(int(c[11:]))
    elif c[:9]=='push_back':
        d.append(int(c[10:]))
    elif c=='pop_front':
        print(d.popleft()) if len(d)>0 else print(-1)
    elif c=='pop_back':
        print(d.pop()) if len(d)>0 else print(-1)
    elif c=='size':
        print(len(d))
    elif c=='empty':
        print(0) if len(d)>0 else print(1)
    elif c=='front':
        print(d[0]) if len(d)>0 else print(-1)
    elif c=='back':
        print(d[-1]) if len(d)>0 else print(-1)
