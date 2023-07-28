# Baekjoon_BRONZE3_2442: 별 찍기 - 5

n = int(input())
[print(' '*(n-1-i)+'*'*(2*i+1)) for i in range(n)]
