# Baekjoon_BRONZE3_2445: 별 찍기 - 8

n = int(input())
[print('*'*i + ' '*(2*(n-i)) + '*'*i ) for i in range(1,n+1)]
[print('*'*(n-i) + ' '*(2*i) + '*'*(n-i)) for i in range(1,n)]