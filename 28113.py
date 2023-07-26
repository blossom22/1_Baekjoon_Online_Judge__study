# Baekjoon_BRONZE5_28113: 정보섬의 대중교통

import sys
n,a,b = map(int, sys.stdin.readline().split())
[print('Bus') if a<b else print('Subway') if a>b else print('Anything')]