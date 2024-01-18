# Baekjoon_CLASS2_Silver5_1436: 영화감독 숌

import sys
n = int(sys.stdin.readline())
cnt = 0
res = 666
# 무식하게 전부 탐색하는 브루트포스 알고리즘을 이용했다. 
while True:
    if '666' in str(res):
        cnt += 1
    if cnt==n:
        print(res)
        break
    res += 1