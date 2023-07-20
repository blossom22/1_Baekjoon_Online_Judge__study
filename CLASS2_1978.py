# Baekjoon_CLASS2_1978: 소수 찾기

import sys
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = set()
for num in a:
    if is_prime(num):
        b.add(num)
print(len(b))