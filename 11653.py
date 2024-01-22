# Baekjoon_Bronze1_11653: 소인수분해

import sys
n = int(sys.stdin.readline())
for i in range(2,int(n**0.5)+1):
    while n % i ==0:
        print(i)
        n /= i
if n != 1:
    print(int(n))