# Baekjoon_Bronze4_8674: Tabliczka 

import sys
a,b = map(int, sys.stdin.readline().split())
if a%2==1 and b%2==1:   # 모두 홀수인경우, 결국 차이가 생기며 그 차이는 a,b중 작은 값만큼 생김
    print(min(a,b))
else:       # 하나라도 짝수가 있으면, 짝수가 있는쪽으로 자르면 되어서 차이는 0
    print(0)