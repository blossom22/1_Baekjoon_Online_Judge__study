# Baekjoon_Silver5_1417: 국회의원 선거

import sys
n = int(sys.stdin.readline())
poll = [int(sys.stdin.readline()) for _ in range(n)]
cnt = 0

if len(poll)==1 or (max(poll)==poll[0] and poll.count(max(poll))==1):
    print(0)
elif poll.count(max(poll)) == n:
    print(1)
else:
    while True:
        poll[poll.index(max(poll))] -= 1
        poll[0] += 1
        cnt += 1 
        if poll[0] == max(poll):
            break
    if poll.count(max(poll))>1:
        cnt += 1
    print(cnt)