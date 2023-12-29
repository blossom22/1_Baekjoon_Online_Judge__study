# Baekjoon_CLASS2_Silver4_10773: 제로 

import sys
k = int(sys.stdin.readline())
stack = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n==0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))
