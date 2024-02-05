# Baekjoon_Bronze4_15128: Congruent Numbers

import sys
p1, q1, p2, q2 = map(int, sys.stdin.readline().split())
res = p1*p2/q1/q2/2     # 부동소수점 오차 때문에 연산 순서를 이렇게 해야한다. 괄호가 없다면 순차적으로 연산하여 딱 나눠지지만, 괄호가 생기면 우선순위가 바뀌어 연산에 오차가 있을 수 있다.
if res == int(res):
    print(1)
else:
    print(0)