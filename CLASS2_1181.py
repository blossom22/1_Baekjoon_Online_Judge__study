# Baekjoon_CLASS2_1181: 단어 정렬

import sys
n = int(sys.stdin.readline())
m = [str(sys.stdin.readline()).strip('\n') for _ in range(n)]
m = list(set(m))
m.sort(key=lambda v : (len(v), v))      # 먼저 길이순으로 정렬후, 사전순 정렬을 한다. 
for i in m:
    print(i)