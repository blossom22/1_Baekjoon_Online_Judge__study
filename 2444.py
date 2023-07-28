# Baekjoon_BRONZE3_2444: 별 찍기 - 7


n = int(input())
[print(' '*(n-1-i)+'*'*(2*i+1)) for i in range(n-1)]
[print(' '*(n-i-1)+'*'*(2*i+1)) for i in range(n-1,-1,-1)]