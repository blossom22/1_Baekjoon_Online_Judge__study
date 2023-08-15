# Baekjoon_BRONZE4_15372: A Simple Problem.   

import sys
t = int(sys.stdin.readline())
n = [int(sys.stdin.readline()) for _ in range(t)]
for i in range(t):
    print(n[i]**2)