# Baekjoon_CLASS3_Silver3_11659: 구간 합 구하기 4
# n,m이 10만이나 되므로, 시간복잡도 고려해야한다. 
# 인덱스0~1, 0~2, 0~3...이렇게 부분합을 미리 구해두고 계산을 하자. 

def hap(v):
    mat = [0]*(v+1)
    mat[1] = nl[0]
    for i in range(2,v+1):
        mat[i] = mat[i-1] + nl[i-1]
    return mat

import sys
n,m = map(int, sys.stdin.readline().split())
nl = list(map(int, sys.stdin.readline().split()))
answer = hap(n)
for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(answer[j]-answer[i-1])
