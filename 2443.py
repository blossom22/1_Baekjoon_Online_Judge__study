# Baekjoon_BRONZE3_2443: 별 찍기 - 6

n = int(input())
[print(' '*(n-i-1)+'*'*(2*i+1)) for i in range(n-1,-1,-1)]