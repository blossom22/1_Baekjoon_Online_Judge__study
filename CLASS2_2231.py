# Baekjoon_CLASS2_Bronze2_2231: 분해합

import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    num = 0
    for j in str(i):    # 각 자릿수를 더한 값 + 온전한 i가 n이 되나 검사하자
        num += int(j)
    num += i
    if num == n:
        print(i)
        break
    if i==n:
        print(0)