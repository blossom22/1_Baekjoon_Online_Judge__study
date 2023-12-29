# Baekjoon_CLASS2_Silver4_11866: 요세푸스 문제 0

from collections import deque
import sys
n,k = map(int, sys.stdin.readline().split())
queue = deque(i for i in range(1,n+1))
a = []
while True:
    if len(queue)>1:
        queue.rotate(-(k-1))
        a.append(queue.popleft())
    else:
        a.append(queue[0])
        break
print('<', end='')
print(*a, sep=', ', end='')
print('>')