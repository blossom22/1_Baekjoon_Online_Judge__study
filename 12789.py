# Baekjoon_Silver3_12789: 도키도키 간식드리미

import sys
n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
line.reverse()
stack = []
i = 1
# line에 뭐라도 있을때는 이 while문을 따르게 한다. 
while line:
    if line and line[-1]==i:
        line.pop()
        i+=1
    elif stack and stack[-1]==i:
        stack.pop()
        i+=1
    else:
        stack.append(line.pop())
# line은 비었는데, stack에 뭐가 남아있는 경우 아래 while문으로 검사하여, 원했던 순서대로 뽑을 수 있으면 진행하고 아니면 break
while stack:
    if stack[-1]==i:
        stack.pop()
        i+=1 
    else:
        break
# 위의 while문을 다 돌았는데 stack에 뭐라도 있으면 잘못된 것>>Sad출력
if stack:
    print('Sad')
else:
    print('Nice')
