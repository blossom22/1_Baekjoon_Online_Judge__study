# Baekjoon_Silver5_5957: Cleaning the Dishes  

import sys
n = int(sys.stdin.readline())
stack1 = [i for i in range(n,0,-1)]
stack2, stack3 = [], []
while len(stack3)<n:
    c,d = map(int, sys.stdin.readline().split())
    if c==1:
        for j in range(d):
            stack2.append(stack1.pop())
    elif c==2:
        for j in range(d):
            stack3.append(stack2.pop())
for i in range(n-1,-1,-1):
    print(stack3[i])