# Baekjoon_BRONZE3_2953: 나는 요리사다    

import sys
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
hap = [sum(matrix[i]) for i in range(5)]
print(hap.index(max(hap))+1, max(hap))
