# Baekjoon_BRONZE3_2446: 별 찍기 - 9 

n = int(input())

for i in range(n):
    print(' '*i + '*'*(2*(n-i)-1))
for j in range(n-2,-1,-1):
    print(' '*j + '*'*(2*(n-j)-1))