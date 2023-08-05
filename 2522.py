# Baekjoon_BRONZE3_2522: 별 찍기 - 12

n = int(input())
for i in range(n-1,-1,-1):
    print(' '*i + '*'*(n-i))
for j in range(1,n):
    print(' '*j + '*'*(n-j))