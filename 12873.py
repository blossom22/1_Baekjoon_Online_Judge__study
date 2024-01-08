# Baekjoon_Silver4_12873: 기념품

from collections import deque
import sys
n = int(sys.stdin.readline())
nl = deque(i for i in range(1,n+1))
a = 1
t = 1
# while문 안쪽에서 rotate을 안쓰고 그냥 for i in range(1,a)해서 nl.append(nl.popleft())하면 시간초과된다.
# rotate함수를 써야 시간문제가 해결가능 
while len(nl)>1:
    nl.rotate(-(a-1))
    nl.popleft()
    a = (t+1)**3
    t += 1
print(*nl)
