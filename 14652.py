# Baekjoon_BRONZE5_14652: 나는 행복합니다~

import sys
n, m, k = map(int, sys.stdin.readline().split())
a = 0
for i in range(n):
    for j in range(m):
        if a == k:
            print(i, j)
            break
        a += 1
    else:
        continue
    break

# 이렇게 풀 수도 있다
n, m, k = map(int, input().split())
i = k // m
j = k % m
print(i, j)