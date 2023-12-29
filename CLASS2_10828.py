# Baekjoon_CLASS2_Silver4_10828: 스택

import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    a = sys.stdin.readline().strip()        # 그냥 input쓰면 시간초과뜬다. sys라이브러리를 이용해서 시간을 줄이자. 
    if a[:4]=='push':
        stack.append(int(''.join(a[5:])))
    elif a=='top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a=='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a=='size':
        print(len(stack))
    elif a=='empty':
        if stack:
            print(0)
        else:
            print(1)