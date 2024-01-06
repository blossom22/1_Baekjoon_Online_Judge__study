# Baekjoon_Silver5_9863: Calling All Programmers 

from collections import deque
import sys

# deque의 rotate은 음수면 앞의 것을 뒤로 보내고 / 양수면 뒤의 것을 앞으로 보낸다. 
while True:
    n,m,k = map(int, sys.stdin.readline().split())
    temp = [i for i in range(1,n+1)]
    nl = deque([[a+1,b] for a,b in enumerate(temp)])
    if n!=0 and m!=0 and k!=0: 
        for i in range(k-1):
            nl.rotate(-m)
            nl.pop()
        nl.rotate(-m)
        print(nl[-1][0])
    else:
        break