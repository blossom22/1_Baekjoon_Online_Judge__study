# Baekjoon_BRONZE3_2547: 사탕 선생 고창영 

import sys
t = int(sys.stdin.readline())
answer = []
for _ in range(t):
    p = input()     # 빈줄 처리
    n = int(sys.stdin.readline())
    b = [int(sys.stdin.readline()) for j in range(n)]

    if sum(b) % n == 0:
        answer.append('YES')
    else:
        answer.append('NO')

print(*answer, sep='\n')