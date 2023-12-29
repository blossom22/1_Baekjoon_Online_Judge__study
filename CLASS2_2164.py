# Baekjoon_CLASS2_Silver4_2164: 카드 2

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque(i for i in range(1,n+1))
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())       # 이 부분은 queue.rotate(-1)로도 할 수 있다.
    # rotate(1)은 오른쪽으로이동(즉, 제일 뒤에 있던 것을 맨 앞으로) / rotate(-1)은 왼쪽으로 이동(즉, 제일 앞에 있던 것을 맨 뒤로)
print(queue[0])


