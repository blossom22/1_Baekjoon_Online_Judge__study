# Baekjoon_Silver4_28278: 스택 2

import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0]==1:
        stack.append(a[1])
    elif a==[5]:
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a==[2]:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a==[3]:
        print(len(stack))
    elif a==[4]:
        if stack:
            print(0)
        else:
            print(1)