# Baekjoon_Silver5_14582: 오늘도 졌다

import sys
o = list(map(int, sys.stdin.readline().split()))
s = list(map(int, sys.stdin.readline().split()))
o_score = 0
s_score = 0
mark = 0    # o가 한번이라도 s를 이기고 있던 적이 있었는지 체크하는 변수

for i in range(9):
    o_score += o[i]
    if o_score > s_score:
        mark = 1        # o가 s를 한번이라도 이긴적이 있었다면 mark=1로 만든다
    s_score += s[i]

if mark == 1:
    print('Yes')
else:
    print('No')
