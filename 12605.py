# Baekjoon_BRONZE2_12605: 단어순서 뒤집기 

import sys
n = int(sys.stdin.readline())
i = 1
for _ in range(n):
    stack = [] 
    s = list(sys.stdin.readline().split())
    for _ in range(len(s)):
        stack.append(s.pop())
    print('Case #%d: %s' %(i, ' '.join(stack)))
    i+=1

