# Baekjoon_BRONZE3_7130: Milk and Honey 

import sys 
m,h = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
happy = 0
for i in range(n):
    c,b = map(int, sys.stdin.readline().split())
    happy += max(c*m, b*h)
print(happy)