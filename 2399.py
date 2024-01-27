# Baekjoon_Bronze2_2399: 거리의 합

import sys
n = int(sys.stdin.readline())
dot = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(n):
    for j in range(n):
        res += abs(dot[i]-dot[j])
print(res)
# 그러나 위의 풀이는 답은 나오지만 시간초과가 뜬다. n이 1만까지 갈 수 있어서 O(n**2)으로 풀면, 시간초과가 나올 수 밖에 없다.
# 따라서 시간복잡도를 줄여야한다
import sys
n = int(sys.stdin.readline())
dot = list(map(int, sys.stdin.readline().split()))
dot.sort()
res = 0
for i in range(n):
    res += dot[i]*i - dot[i]*(n-i-1)
    # 현재점의 값*현재인덱스하면 현재점이 정렬된 상태에서 몇번째 위치에 있는지에 따른 거리차이가 계산된다.
    # - 뒤부분은 현재점이 정렬된 순서에서 뒤쪽에있는 모든 원소들과의 거리를 계산한다.  
print(res*2)