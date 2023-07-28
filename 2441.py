# Baekjoon_BRONZE3_15964: 별 찍기 - 4

n = int(input())
[print(' '*(n-i)+'*'*i) for i in range(n,0,-1)]