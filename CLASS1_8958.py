# Baekjoon_CLASS1_8958: OX퀴즈  

import sys
n = int(input())
a = [sys.stdin.readline().strip('\n') for i in range(n)]

for i in range(n):
    score = 0
    k = 0           # 연속되는 O가 올경우, 그 O의 점수는 연속될때마다 1씩 증가시킨다.
    for j in a[i]:
        if j =='O':
            k += 1
            score += k
        else:
            k = 0
    print(score)
