# Baekjoon_BRONZE3_10991: Practice: 별 찍기 - 16

n = int(input())
for i in range(n):
    print(' '*(n-i-1) + '*' + ' *'*(i))