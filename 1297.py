# Baekjoon_BRONZE2_1297: TV 크기

import sys,math
d,h,w = map(int, sys.stdin.readline().split())
k = math.sqrt((d**2)/(h**2+w**2))
print(int(k*h), int(k*w))