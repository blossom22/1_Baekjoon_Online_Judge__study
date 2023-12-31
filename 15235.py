# Baekjoon_Silver5_15235: Olympiad Pizza 

from collections import deque
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a = [[x+1,y] for x,y in enumerate(a)]
m = deque(a)
cnt = []
i = 0       # 시간을 세는 변수
while m:
    if m[0][1]>1:
        m[0][1] -= 1
        i += 1
        m.rotate(-1)
    else:
        m[0][1] -= 1
        i+=1
        cnt.append([m[0][0], i])
        m.popleft()
cnt.sort(key=lambda v: v[0])    # 인덱스값을 기준으로 오름차순 정렬후, 각 값들의 소요된 시간(cnt[i][1])을 출력한다.
for i in range(n):
    print(cnt[i][1], end=' ')