# Baekjoon_Silver4_4992: Hanafuda Shuffle 
from collections import deque
import sys
while True:
    n,r = map(int, sys.stdin.readline().split())
    if n==0 and r==0: 
        break
    else:
        stack = list(range(1,n+1))
        for i in range(r):
            p,c = map(int, sys.stdin.readline().split())
            st_1 = deque()
            st_2 = deque()
            for j in range(p-1):
                st_1.appendleft(stack.pop())
            for j in range(c):
                st_2.appendleft(stack.pop())
            for j in st_1:
                stack.append(j)
            for j in st_2:
                stack.append(j)
        print(stack[-1])