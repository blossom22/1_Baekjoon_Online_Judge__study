# Baekjoon_CLASS2_Silver3_1966: 프린터 큐
# 중요도가 같은 문서들이 여러개 있을 수 있어서, 그냥 queue[x]값만 찾으려고 하면 안된다. queue[x]의 값과, 초기 인덱스값이 모두 필요하다 >> enumerate이용
from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, x = map(int, sys.stdin.readline().split())
    queue = deque(enumerate(map(int, sys.stdin.readline().split())))  # 문서의 중요도(초기입력되는 값들)와 인덱스(중요도가 같은 문서들이 있을 수 있어서)를 함께 저장
    target_index = x  # 목표하는 문서의 인덱스
    cnt = 0

    while True:
        if queue[0][1] < max(queue, key=lambda x: x[1])[1]:
            queue.append(queue.popleft())  # 현재 문서의 중요도가 최대가 아니라면 맨 뒤로 보낸다.
        else:
            if queue[0][0] == target_index:
                cnt += 1
                print(cnt)
                break
            else:
                queue.popleft()
                cnt += 1
