# Baekjoon_Silver3_11899: 괄호 끼워넣기

from collections import deque
import sys
s = list(sys.stdin.readline().strip())
stack = deque()

for i in s:
    if i==')':
        if stack and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
    elif i=='(':
        stack.append(i)
print(len(stack))