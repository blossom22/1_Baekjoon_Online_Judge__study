# Baekjoon_CLASS1_10250: ACM 호텔 

import sys
t = int(input())
a = []
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor = (n - 1) % h + 1
    room = (n - 1) // h + 1
    room_number = floor * 100 + room
    a.append(room_number)
print(*a, sep='\n')