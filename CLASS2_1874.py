# Baekjoon_CLASS2_Silver2_1874: 스택 수열

import sys
n = int(sys.stdin.readline())
stack = []
maxx = 1
answer = []
for i in range(n):
    num = int(sys.stdin.readline())
    for j in range(maxx,num+1):
        stack.append(j)
        maxx = max(maxx, j+1)       # 지금까지 스택에 쌓거나 뺀 수들을 제외하고 가장 큰 수부터 다시 스택에 쌓아야한다. 
        answer.append('+')
    if stack[-1]==num:
        stack.pop()
        answer.append('-')
    else:
        answer.append('NO')

if 'NO' in answer:
    print('NO')
else:
    print(*answer, sep='\n')