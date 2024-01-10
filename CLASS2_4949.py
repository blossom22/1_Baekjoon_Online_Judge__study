# Baekjoon_CLASS2_Silver4_4949: 균형잡힌 세상

import sys
while True:
    stack = []
    n = list(sys.stdin.readline().rstrip())
    if n != ['.']:
        for i in n:
            if i=='(' or i=='[':
                stack.append(i)
            elif i==')' and stack:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
            elif i==')' and len(stack)==0:
                stack.append(i)
            elif i==']' and len(stack)==0:
                stack.append(i)
            elif i==']' and stack:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack)==0:
            print('yes')
        else:
            print('no')
    else:
        break