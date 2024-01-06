# Baekjoon_Silver5_17857: Musical Chairs 

from collections import deque
import sys
n = int(sys.stdin.readline())
nl = list(map(int, sys.stdin.readline().split()))
temp = deque([[a+1,b] for a,b in enumerate(nl)])
while len(temp)>1:
    idx = temp[0][1]
    temp.rotate(-idx)   # rotate괄호 안이 음수면 왼쪽으로 회전 / 양수면 오른쪽으로 회전
    temp.pop()          # rotate해서 마지막 값을 제거
print(temp[0][0])