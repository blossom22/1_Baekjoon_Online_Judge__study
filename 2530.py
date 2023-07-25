# Baekjoon_BRONZE4_2530: 인공지능 시계

import sys 
a,b,c = map(int, sys.stdin.readline().split())
second = int(sys.stdin.readline())
result = second + a*3600 + b*60 + c
hour = []
hour.append((result//3600)%24)
hour.append((result%3600)//60)
hour.append((result%3600)%60)

print(*hour)