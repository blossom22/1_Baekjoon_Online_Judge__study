# Baekjoon_BRONZE2_3943: 헤일스톤 수열 

import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    a = [n]
    while n != 1:
        if n%2==0:
            n //= 2
            a.append(n)
        else:
            n = n*3+1
            a.append(n)
    print(max(a))