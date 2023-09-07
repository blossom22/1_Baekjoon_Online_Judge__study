# Baekjoon_BRONZE5_29263: Счастье Мистера Бина 

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
even = 0
odd = 0
for i in range(n):
    if a[i]%2==0:
        even+=1
    else:
        odd+=1
print('Happy') if even>odd else print('Sad')