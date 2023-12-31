# Baekjoon_Silver4_1158: 요세푸스 문제

from collections import deque
import sys
n,k = map(int, sys.stdin.readline().split())
queue = deque(i for i in range(1,n+1))
a = deque()
while queue:
    # deque에서 rotate()은 괄호안의 수가 양수면 뒤의 숫자를 앞으로, 음수면 앞의 숫자를 뒤로 보낸다.
    queue.rotate(-(k-1))
    a.append(queue.popleft())
print('<',end='')
print(*a, sep=', ', end='')
print('>')
