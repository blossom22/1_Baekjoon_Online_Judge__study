# Baekjoon_Silver5_2161: 카드1

from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque(i for i in range(1,n+1))
a = deque()
while q:
    a.append(q.popleft())
    if q:
        q.append(q.popleft())
print(*list(a))


# 그냥 새로운 리스트(a)를 만들지 않고 바로 print해도 된다. 
from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque(i for i in range(1,n+1))
while q:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())
